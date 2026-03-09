"""
幻灯片操作工具
"""

from typing import Any, Dict, List, Optional
from mcp.types import Tool, TextContent
from ..utils import AppleScriptRunner, validate_slide_number, ParameterError


class SlideTools:
    """幻灯片操作工具类"""
    
    def __init__(self):
        self.runner = AppleScriptRunner()
    
    def get_tools(self) -> List[Tool]:
        """获取所有幻灯片操作工具"""
        return [
            Tool(
                name="add_slide",
                description="Add a new slide to the presentation",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "doc_name": {
                            "type": "string",
                            "description": "Document name (optional, defaults to front document)"
                        },
                        "position": {
                            "type": "integer",
                            "description": "Insert position (optional, 0 = append at end)"
                        },
                        "layout": {
                            "type": "string",
                            "description": "Layout type (optional)"
                        }
                    }
                }
            ),
            Tool(
                name="delete_slide",
                description="Delete a slide",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "doc_name": {
                            "type": "string",
                            "description": "Document name (optional, defaults to front document)"
                        },
                        "slide_number": {
                            "type": "integer",
                            "description": "Slide number to delete"
                        }
                    },
                    "required": ["slide_number"]
                }
            ),
            Tool(
                name="duplicate_slide",
                description="Duplicate a slide",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "doc_name": {
                            "type": "string",
                            "description": "Document name (optional, defaults to front document)"
                        },
                        "slide_number": {
                            "type": "integer",
                            "description": "Slide number to duplicate"
                        },
                        "new_position": {
                            "type": "integer",
                            "description": "New position (optional, 0 = append at end)"
                        }
                    },
                    "required": ["slide_number"]
                }
            ),
            Tool(
                name="move_slide",
                description="Move a slide to a different position",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "doc_name": {
                            "type": "string",
                            "description": "Document name (optional, defaults to front document)"
                        },
                        "from_position": {
                            "type": "integer",
                            "description": "Source position"
                        },
                        "to_position": {
                            "type": "integer",
                            "description": "Target position"
                        }
                    },
                    "required": ["from_position", "to_position"]
                }
            ),
            Tool(
                name="get_slide_count",
                description="Get slide count",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "doc_name": {
                            "type": "string",
                            "description": "Document name (optional, defaults to front document)"
                        }
                    }
                }
            ),
            Tool(
                name="select_slide",
                description="Select a specific slide",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "doc_name": {
                            "type": "string",
                            "description": "Document name (optional, defaults to front document)"
                        },
                        "slide_number": {
                            "type": "integer",
                            "description": "Slide number"
                        }
                    },
                    "required": ["slide_number"]
                }
            ),
            Tool(
                name="set_slide_layout",
                description="Set slide layout",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "doc_name": {
                            "type": "string",
                            "description": "Document name (optional, defaults to front document)"
                        },
                        "slide_number": {
                            "type": "integer",
                            "description": "Slide number"
                        },
                        "layout": {
                            "type": "string",
                            "description": "Layout type"
                        }
                    },
                    "required": ["slide_number", "layout"]
                }
            ),
            Tool(
                name="get_slide_info",
                description="Get slide info (number, layout, text item count)",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "doc_name": {
                            "type": "string",
                            "description": "Document name (optional, defaults to front document)"
                        },
                        "slide_number": {
                            "type": "integer",
                            "description": "Slide number"
                        }
                    },
                    "required": ["slide_number"]
                }
            ),
            Tool(
                name="get_available_layouts",
                description="Get list of available slide layouts",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "doc_name": {
                            "type": "string",
                            "description": "Document name (optional, defaults to front document)"
                        }
                    }
                }
            )
        ]
    
    async def add_slide(self, doc_name: str = "", position: int = 0, layout: str = "", clear_default_content: bool = True) -> List[TextContent]:
        """添加新幻灯片"""
        try:
            # 如果启用清除默认内容且没有指定布局，使用 Blank 布局
            if clear_default_content and layout == "":
                layout = "Blank"
            
            result = self.runner.run_inline_script(f'''
                tell application "Keynote"
                    activate
                    if "{doc_name}" is "" then
                        set targetDoc to front document
                    else
                        set targetDoc to document "{doc_name}"
                    end if
                    
                    if {position} is 0 then
                        set newSlide to make new slide at end of slides of targetDoc
                    else
                        set newSlide to make new slide at slide {position} of targetDoc
                    end if
                    
                    if "{layout}" is not "" then
                        try
                            set base slide of newSlide to master slide "{layout}" of targetDoc
                        on error
                            -- 如果布局不存在，尝试使用 Blank 布局
                            try
                                set base slide of newSlide to master slide "Blank" of targetDoc
                                log "Layout {layout} not found, using Blank layout"
                            on error
                                log "Neither {layout} nor Blank layout found, using default layout"
                            end try
                        end try
                    end if
                    
                    return slide number of newSlide
                end tell
            ''')
            
            layout_info = f" (布局: {layout})" if layout else " (默认布局)"
            return [TextContent(
                type="text",
                text=f"✅ 成功添加幻灯片，编号: {result}{layout_info}"
            )]
            
        except Exception as e:
            return [TextContent(
                type="text",
                text=f"❌ 添加幻灯片失败: {str(e)}"
            )]
    
    async def delete_slide(self, slide_number: int, doc_name: str = "") -> List[TextContent]:
        """删除幻灯片"""
        try:
            validate_slide_number(slide_number)
            
            self.runner.run_inline_script(f'''
                tell application "Keynote"
                    if "{doc_name}" is "" then
                        set targetDoc to front document
                    else
                        set targetDoc to document "{doc_name}"
                    end if
                    
                    delete slide {slide_number} of targetDoc
                end tell
            ''')
            
            return [TextContent(
                type="text",
                text=f"✅ 成功删除幻灯片 {slide_number}"
            )]
            
        except Exception as e:
            return [TextContent(
                type="text",
                text=f"❌ 删除幻灯片失败: {str(e)}"
            )]
    
    async def duplicate_slide(self, slide_number: int, doc_name: str = "", new_position: int = 0) -> List[TextContent]:
        """复制幻灯片"""
        try:
            validate_slide_number(slide_number)
            
            result = self.runner.run_inline_script(f'''
                tell application "Keynote"
                    if "{doc_name}" is "" then
                        set targetDoc to front document
                    else
                        set targetDoc to document "{doc_name}"
                    end if
                    
                    set sourceSlide to slide {slide_number} of targetDoc
                    set newSlide to duplicate sourceSlide
                    
                    if {new_position} is not 0 then
                        move newSlide to slide {new_position} of targetDoc
                    end if
                    
                    return slide number of newSlide
                end tell
            ''')
            
            return [TextContent(
                type="text",
                text=f"✅ 成功复制幻灯片，新编号: {result}"
            )]
            
        except Exception as e:
            return [TextContent(
                type="text",
                text=f"❌ 复制幻灯片失败: {str(e)}"
            )]
    
    async def move_slide(self, from_position: int, to_position: int, doc_name: str = "") -> List[TextContent]:
        """移动幻灯片位置"""
        try:
            validate_slide_number(from_position)
            validate_slide_number(to_position)
            
            self.runner.run_inline_script(f'''
                tell application "Keynote"
                    if "{doc_name}" is "" then
                        set targetDoc to front document
                    else
                        set targetDoc to document "{doc_name}"
                    end if
                    
                    set sourceSlide to slide {from_position} of targetDoc
                    move sourceSlide to slide {to_position} of targetDoc
                end tell
            ''')
            
            return [TextContent(
                type="text",
                text=f"✅ 成功移动幻灯片从位置 {from_position} 到位置 {to_position}"
            )]
            
        except Exception as e:
            return [TextContent(
                type="text",
                text=f"❌ 移动幻灯片失败: {str(e)}"
            )]
    
    async def get_slide_count(self, doc_name: str = "") -> List[TextContent]:
        """获取幻灯片数量"""
        try:
            result = self.runner.run_inline_script(f'''
                tell application "Keynote"
                    if "{doc_name}" is "" then
                        set targetDoc to front document
                    else
                        set targetDoc to document "{doc_name}"
                    end if
                    
                    return count of slides of targetDoc
                end tell
            ''')
            
            return [TextContent(
                type="text",
                text=f"📊 幻灯片数量: {result}"
            )]
            
        except Exception as e:
            return [TextContent(
                type="text",
                text=f"❌ 获取幻灯片数量失败: {str(e)}"
            )]
    
    async def select_slide(self, slide_number: int, doc_name: str = "") -> List[TextContent]:
        """选择指定幻灯片"""
        try:
            validate_slide_number(slide_number)
            
            self.runner.run_inline_script(f'''
                tell application "Keynote"
                    if "{doc_name}" is "" then
                        set targetDoc to front document
                    else
                        set targetDoc to document "{doc_name}"
                    end if
                    
                    set current slide of targetDoc to slide {slide_number} of targetDoc
                end tell
            ''')
            
            return [TextContent(
                type="text",
                text=f"✅ 成功选择幻灯片 {slide_number}"
            )]
            
        except Exception as e:
            return [TextContent(
                type="text",
                text=f"❌ 选择幻灯片失败: {str(e)}"
            )]
    
    async def set_slide_layout(self, slide_number: int, layout: str, doc_name: str = "") -> List[TextContent]:
        """设置幻灯片布局"""
        try:
            validate_slide_number(slide_number)
            
            result = self.runner.run_inline_script(f'''
                tell application "Keynote"
                    if "{doc_name}" is "" then
                        set targetDoc to front document
                    else
                        set targetDoc to document "{doc_name}"
                    end if
                    
                    try
                        -- 找到目标布局
                        set targetLayout to missing value
                        repeat with masterSlide in master slides of targetDoc
                            if name of masterSlide is "{layout}" then
                                set targetLayout to masterSlide
                                exit repeat
                            end if
                        end repeat
                        
                        if targetLayout is missing value then
                            return "layout_not_found"
                        end if
                        
                        -- 设置幻灯片布局（使用正确的语法：base slide）
                        set base slide of slide {slide_number} of targetDoc to targetLayout
                        return "success"
                    on error errMsg
                        return "error: " & errMsg
                    end try
                end tell
            ''')
            
            if result == "success":
                return [TextContent(
                    type="text",
                    text=f"✅ 成功设置幻灯片 {slide_number} 的布局为: {layout}"
                )]
            elif result == "layout_not_found":
                return [TextContent(
                    type="text",
                    text=f"❌ 布局不存在: {layout}"
                )]
            else:
                return [TextContent(
                    type="text",
                    text=f"❌ 设置布局失败: {result}"
                )]
                
        except Exception as e:
            return [TextContent(
                type="text",
                text=f"❌ 设置幻灯片布局失败: {str(e)}"
            )]
    
    async def get_slide_info(self, slide_number: int, doc_name: str = "") -> List[TextContent]:
        """获取幻灯片信息"""
        try:
            validate_slide_number(slide_number)
            
            result = self.runner.run_inline_script(f'''
                tell application "Keynote"
                    if "{doc_name}" is "" then
                        set targetDoc to front document
                    else
                        set targetDoc to document "{doc_name}"
                    end if
                    
                    set targetSlide to slide {slide_number} of targetDoc
                    set slideInfo to {{}}
                    
                    set end of slideInfo to slide number of targetSlide
                    
                    try
                        set end of slideInfo to name of master slide of targetSlide
                    on error
                        set end of slideInfo to "Unknown Layout"
                    end try
                    
                    try
                        set end of slideInfo to count of text items of targetSlide
                    on error
                        set end of slideInfo to 0
                    end try
                    
                    return slideInfo as string
                end tell
            ''')
            
            info_parts = result.replace("{", "").replace("}", "").split(", ")
            if len(info_parts) >= 3:
                number, layout, text_count = info_parts[0], info_parts[1], info_parts[2]
                return [TextContent(
                    type="text",
                    text=f"📊 幻灯片 {slide_number} 信息:\n• 编号: {number}\n• 布局: {layout}\n• 文本框数量: {text_count}"
                )]
            else:
                return [TextContent(
                    type="text",
                    text=f"📊 幻灯片 {slide_number} 信息: {result}"
                )]
                
        except Exception as e:
            return [TextContent(
                type="text",
                text=f"❌ 获取幻灯片信息失败: {str(e)}"
            )]
    
    async def get_available_layouts(self, doc_name: str = "") -> List[TextContent]:
        """获取可用布局列表"""
        try:
            result = self.runner.run_inline_script(f'''
                tell application "Keynote"
                    if "{doc_name}" is "" then
                        set targetDoc to front document
                    else
                        set targetDoc to document "{doc_name}"
                    end if
                    
                    set layoutList to {{}}
                    repeat with masterSlide in master slides of targetDoc
                        set end of layoutList to name of masterSlide
                    end repeat
                    
                    -- 使用特殊分隔符来避免布局名称中的逗号问题
                    set AppleScript's text item delimiters to "|||"
                    set layoutString to layoutList as string
                    set AppleScript's text item delimiters to ""
                    
                    return layoutString
                end tell
            ''')
            
            if result:
                layouts = result.split("|||")
                layout_list = "\n".join([f"• {layout.strip()}" for layout in layouts if layout.strip()])
                return [TextContent(
                    type="text",
                    text=f"📐 可用布局:\n{layout_list}"
                )]
            else:
                return [TextContent(
                    type="text",
                    text="📐 没有找到可用布局"
                )]
                
        except Exception as e:
            return [TextContent(
                type="text",
                text=f"❌ 获取布局列表失败: {str(e)}"
            )] 