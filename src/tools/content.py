"""
内容管理工具
"""

from typing import Any, Dict, List, Optional
from mcp.types import Tool, TextContent
from ..utils import AppleScriptRunner, validate_slide_number, validate_coordinates, validate_file_path, ParameterError


class ContentTools:
    """内容管理工具类"""
    
    def __init__(self):
        self.runner = AppleScriptRunner()
    
    def get_tools(self) -> List[Tool]:
        """获取所有内容管理工具"""
        return [
            Tool(
                name="add_text_box",
                description="Add a text box to a slide",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "slide_number": {
                            "type": "integer",
                            "description": "Slide number"
                        },
                        "text": {
                            "type": "string",
                            "description": "Text content"
                        },
                        "x": {
                            "type": "number",
                            "description": "X coordinate in pixels (optional). Origin (0,0) is top-left. Suggested: 50-950px"
                        },
                        "y": {
                            "type": "number",
                            "description": "Y coordinate in pixels (optional). Origin (0,0) is top-left. Suggested: 50-650px"
                        }
                    },
                    "required": ["slide_number", "text"]
                }
            ),
            Tool(
                name="add_title",
                description="Add a title to a slide",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "slide_number": {
                            "type": "integer",
                            "description": "Slide number"
                        },
                        "title": {
                            "type": "string",
                            "description": "Title text"
                        },
                        "x": {
                            "type": "number",
                            "description": "X coordinate in pixels (optional). Suggested for title: 100-200"
                        },
                        "y": {
                            "type": "number",
                            "description": "Y coordinate in pixels (optional). Suggested for title: 50-100"
                        },
                        "font_size": {
                            "type": "number",
                            "description": "Font size (optional, default 36)"
                        },
                        "font_name": {
                            "type": "string",
                            "description": "Font name (optional)"
                        }
                    },
                    "required": ["slide_number", "title"]
                }
            ),
            Tool(
                name="add_subtitle",
                description="Add a subtitle to a slide",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "slide_number": {
                            "type": "integer",
                            "description": "Slide number"
                        },
                        "subtitle": {
                            "type": "string",
                            "description": "Subtitle text"
                        },
                        "x": {
                            "type": "number",
                            "description": "X coordinate in pixels (optional). Suggested for subtitle: 100-200"
                        },
                        "y": {
                            "type": "number",
                            "description": "Y coordinate in pixels (optional). Suggested for subtitle: 120-180"
                        },
                        "font_size": {
                            "type": "number",
                            "description": "Font size (optional, default 24)"
                        },
                        "font_name": {
                            "type": "string",
                            "description": "Font name (optional)"
                        }
                    },
                    "required": ["slide_number", "subtitle"]
                }
            ),
            Tool(
                name="add_bullet_list",
                description="Add a bullet list to a slide",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "slide_number": {
                            "type": "integer",
                            "description": "Slide number"
                        },
                        "items": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List items"
                        },
                        "x": {
                            "type": "number",
                            "description": "X coordinate in pixels (optional). Suggested for list: 100-150"
                        },
                        "y": {
                            "type": "number",
                            "description": "Y coordinate in pixels (optional). Suggested for list: 200-300"
                        },
                        "font_size": {
                            "type": "number",
                            "description": "Font size (optional, default 18)"
                        },
                        "font_name": {
                            "type": "string",
                            "description": "Font name (optional)"
                        }
                    },
                    "required": ["slide_number", "items"]
                }
            ),
            Tool(
                name="add_numbered_list",
                description="Add a numbered list to a slide",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "slide_number": {
                            "type": "integer",
                            "description": "Slide number"
                        },
                        "items": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List items"
                        },
                        "x": {
                            "type": "number",
                            "description": "X coordinate in pixels (optional). Suggested for list: 100-150"
                        },
                        "y": {
                            "type": "number",
                            "description": "Y coordinate in pixels (optional). Suggested for list: 200-300"
                        },
                        "font_size": {
                            "type": "number",
                            "description": "Font size (optional, default 18)"
                        },
                        "font_name": {
                            "type": "string",
                            "description": "Font name (optional)"
                        }
                    },
                    "required": ["slide_number", "items"]
                }
            ),
            Tool(
                name="add_code_block",
                description="Add a code block to a slide",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "slide_number": {
                            "type": "integer",
                            "description": "Slide number"
                        },
                        "code": {
                            "type": "string",
                            "description": "Code content"
                        },
                        "x": {
                            "type": "number",
                            "description": "X coordinate in pixels (optional). Suggested for code: 100-200"
                        },
                        "y": {
                            "type": "number",
                            "description": "Y coordinate in pixels (optional). Suggested for code: 250-350"
                        },
                        "font_size": {
                            "type": "number",
                            "description": "Font size (optional, default 14)"
                        },
                        "font_name": {
                            "type": "string",
                            "description": "Font name (optional, default Monaco)"
                        }
                    },
                    "required": ["slide_number", "code"]
                }
            ),
            Tool(
                name="add_quote",
                description="Add a quote to a slide",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "slide_number": {
                            "type": "integer",
                            "description": "Slide number"
                        },
                        "quote": {
                            "type": "string",
                            "description": "Quote text"
                        },
                        "x": {
                            "type": "number",
                            "description": "X coordinate in pixels (optional). Suggested for quote: 150-250"
                        },
                        "y": {
                            "type": "number",
                            "description": "Y coordinate in pixels (optional). Suggested for quote: 300-400"
                        },
                        "font_size": {
                            "type": "number",
                            "description": "Font size (optional, default 20)"
                        },
                        "font_name": {
                            "type": "string",
                            "description": "Font name (optional)"
                        }
                    },
                    "required": ["slide_number", "quote"]
                }
            ),
            Tool(
                name="add_image",
                description="Add an image to a slide",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "slide_number": {
                            "type": "integer",
                            "description": "Slide number"
                        },
                        "image_path": {
                            "type": "string",
                            "description": "Path to the image file"
                        },
                        "x": {
                            "type": "number",
                            "description": "X coordinate in pixels (optional). Suggested for image: 400-600"
                        },
                        "y": {
                            "type": "number",
                            "description": "Y coordinate in pixels (optional). Suggested for image: 200-400"
                        }
                    },
                    "required": ["slide_number", "image_path"]
                }
            )
        ]
    
    async def add_text_box(self, slide_number: int, text: str, x: Optional[float] = None, y: Optional[float] = None, doc_name: str = "") -> List[TextContent]:
        """添加文本框"""
        try:
            validate_slide_number(slide_number)
            x_pos, y_pos = validate_coordinates(x, y)
            
            # 处理文本中的引号
            escaped_text = text.replace('"', '\\"')
            
            # 使用内联脚本，语法正确
            result = self.runner.run_inline_script(f'''
                tell application "Keynote"
                    activate
                    if "{doc_name}" is not "" then
                        set targetDoc to document "{doc_name}"
                    else
                        set targetDoc to front document
                    end if
                    
                    tell targetDoc
                        tell slide {slide_number}
                            -- 创建文本框
                            set newTextBox to make new text item with properties {{object text:"{escaped_text}"}}
                            
                            -- 设置位置（如果指定了x或y坐标）
                            {"" if x is None and y is None else f"set position of newTextBox to {{{x_pos}, {y_pos}}}"}
                        end tell
                    end tell
                    
                    return "success"
                end tell
            ''')
            
            return [TextContent(
                type="text",
                text=f"✅ 成功在幻灯片 {slide_number} 添加文本框"
            )]
            
        except Exception as e:
            return [TextContent(
                type="text",
                text=f"❌ 添加文本框失败: {str(e)}"
            )]
    
    async def add_title(self, slide_number: int, title: str, x: Optional[float] = None, y: Optional[float] = None, 
                       font_size: Optional[int] = None, font_name: str = "", doc_name: str = "") -> List[TextContent]:
        """添加标题"""
        try:
            validate_slide_number(slide_number)
            x_pos, y_pos = validate_coordinates(x, y)
            
            # 处理文本中的引号
            escaped_title = title.replace('"', '\\"')
            
            # 构建字体设置命令
            font_command = f'set font of object text to "{font_name}"' if font_name else ""
            
            result = self.runner.run_inline_script(f'''
                tell application "Keynote"
                    activate
                    if "{doc_name}" is not "" then
                        set targetDoc to document "{doc_name}"
                    else
                        set targetDoc to front document
                    end if
                    
                    tell targetDoc
                        tell slide {slide_number}
                            set newTitle to make new text item with properties {{object text:"{escaped_title}"}}
                            
                            -- 设置位置（如果指定了x或y坐标）
                            {"" if x is None and y is None else f"set position of newTitle to {{{x_pos}, {y_pos}}}"}
                            
                            tell newTitle
                                set size of object text to {font_size if font_size else 36}
                                {font_command if font_command else "-- no font specified"}
                            end tell
                        end tell
                    end tell
                    
                    return "success"
                end tell
            ''')
            
            return [TextContent(
                type="text",
                text=f"✅ 成功在幻灯片 {slide_number} 添加标题"
            )]
            
        except Exception as e:
            return [TextContent(
                type="text",
                text=f"❌ 添加标题失败: {str(e)}"
            )]
    
    async def add_subtitle(self, slide_number: int, subtitle: str, x: Optional[float] = None, y: Optional[float] = None, 
                          font_size: Optional[int] = None, font_name: str = "", doc_name: str = "") -> List[TextContent]:
        """添加副标题"""
        try:
            validate_slide_number(slide_number)
            x_pos, y_pos = validate_coordinates(x, y)
            
            # 处理文本中的引号
            escaped_subtitle = subtitle.replace('"', '\\"')
            
            # 构建字体设置命令
            font_command = f'set font of object text to "{font_name}"' if font_name else ""
            
            result = self.runner.run_inline_script(f'''
                tell application "Keynote"
                    activate
                    if "{doc_name}" is not "" then
                        set targetDoc to document "{doc_name}"
                    else
                        set targetDoc to front document
                    end if
                    
                    tell targetDoc
                        tell slide {slide_number}
                            set newSubtitle to make new text item with properties {{object text:"{escaped_subtitle}"}}
                            
                            -- 设置位置（如果指定了x或y坐标）
                            {"" if x is None and y is None else f"set position of newSubtitle to {{{x_pos}, {y_pos}}}"}
                            
                            tell newSubtitle
                                set size of object text to {font_size if font_size else 24}
                                {font_command if font_command else "-- no font specified"}
                            end tell
                        end tell
                    end tell
                    
                    return "success"
                end tell
            ''')
            
            return [TextContent(
                type="text",
                text=f"✅ 成功在幻灯片 {slide_number} 添加副标题"
            )]
            
        except Exception as e:
            return [TextContent(
                type="text",
                text=f"❌ 添加副标题失败: {str(e)}"
            )]
    
    async def add_bullet_list(self, slide_number: int, items: List[str], x: Optional[float] = None, y: Optional[float] = None, 
                             font_size: Optional[int] = None, font_name: str = "", doc_name: str = "") -> List[TextContent]:
        """添加项目符号列表"""
        try:
            validate_slide_number(slide_number)
            x_pos, y_pos = validate_coordinates(x, y)
            
            # 构建列表文本
            list_text = ""
            for i, item in enumerate(items):
                escaped_item = item.replace('"', '\\"')
                list_text += f"• {escaped_item}"
                if i < len(items) - 1:
                    list_text += "\\n"
            
            # 构建字体设置命令
            font_command = f'set font of object text to "{font_name}"' if font_name else ""
            
            result = self.runner.run_inline_script(f'''
                tell application "Keynote"
                    activate
                    if "{doc_name}" is not "" then
                        set targetDoc to document "{doc_name}"
                    else
                        set targetDoc to front document
                    end if
                    
                    tell targetDoc
                        tell slide {slide_number}
                            set newList to make new text item with properties {{object text:"{list_text}"}}
                            
                            -- 设置位置（如果指定了x或y坐标）
                            {"" if x is None and y is None else f"set position of newList to {{{x_pos}, {y_pos}}}"}
                            
                            tell newList
                                set size of object text to {font_size if font_size else 18}
                                {font_command if font_command else "-- no font specified"}
                            end tell
                        end tell
                    end tell
                    
                    return "success"
                end tell
            ''')
            
            return [TextContent(
                type="text",
                text=f"✅ 成功在幻灯片 {slide_number} 添加项目符号列表（{len(items)} 项）"
            )]
            
        except Exception as e:
            return [TextContent(
                type="text",
                text=f"❌ 添加项目符号列表失败: {str(e)}"
            )]
    
    async def add_numbered_list(self, slide_number: int, items: List[str], x: Optional[float] = None, y: Optional[float] = None, 
                               font_size: Optional[int] = None, font_name: str = "", doc_name: str = "") -> List[TextContent]:
        """添加编号列表"""
        try:
            validate_slide_number(slide_number)
            x_pos, y_pos = validate_coordinates(x, y)
            
            # 构建编号列表文本
            list_text = ""
            for i, item in enumerate(items):
                escaped_item = item.replace('"', '\\"')
                list_text += f"{i+1}. {escaped_item}"
                if i < len(items) - 1:
                    list_text += "\\n"
            
            # 构建字体设置命令
            font_command = f'set font of object text to "{font_name}"' if font_name else ""
            
            result = self.runner.run_inline_script(f'''
                tell application "Keynote"
                    activate
                    if "{doc_name}" is not "" then
                        set targetDoc to document "{doc_name}"
                    else
                        set targetDoc to front document
                    end if
                    
                    tell targetDoc
                        tell slide {slide_number}
                            set newList to make new text item with properties {{object text:"{list_text}"}}
                            
                            -- 设置位置（如果指定了x或y坐标）
                            {"" if x is None and y is None else f"set position of newList to {{{x_pos}, {y_pos}}}"}
                            
                            tell newList
                                set size of object text to {font_size if font_size else 18}
                                {font_command if font_command else "-- no font specified"}
                            end tell
                        end tell
                    end tell
                    
                    return "success"
                end tell
            ''')
            
            return [TextContent(
                type="text",
                text=f"✅ 成功在幻灯片 {slide_number} 添加编号列表（{len(items)} 项）"
            )]
            
        except Exception as e:
            return [TextContent(
                type="text",
                text=f"❌ 添加编号列表失败: {str(e)}"
            )]
    
    async def add_code_block(self, slide_number: int, code: str, x: Optional[float] = None, y: Optional[float] = None, 
                            font_size: Optional[int] = None, font_name: str = "", doc_name: str = "") -> List[TextContent]:
        """添加代码块"""
        try:
            validate_slide_number(slide_number)
            x_pos, y_pos = validate_coordinates(x, y)
            
            # 处理代码中的引号和换行
            escaped_code = code.replace('"', '\\"').replace('\n', '\\n')
            
            result = self.runner.run_inline_script(f'''
                tell application "Keynote"
                    activate
                    if "{doc_name}" is not "" then
                        set targetDoc to document "{doc_name}"
                    else
                        set targetDoc to front document
                    end if
                    
                    tell targetDoc
                        tell slide {slide_number}
                            set newCodeBlock to make new text item with properties {{object text:"{escaped_code}"}}
                            
                            -- 设置位置（如果指定了x或y坐标）
                            {"" if x is None and y is None else f"set position of newCodeBlock to {{{x_pos}, {y_pos}}}"}
                            
                            tell newCodeBlock
                                set size of object text to {font_size if font_size else 14}
                                set font of object text to "{font_name if font_name else 'Monaco'}"
                            end tell
                        end tell
                    end tell
                    
                    return "success"
                end tell
            ''')
            
            return [TextContent(
                type="text",
                text=f"✅ 成功在幻灯片 {slide_number} 添加代码块"
            )]
            
        except Exception as e:
            return [TextContent(
                type="text",
                text=f"❌ 添加代码块失败: {str(e)}"
            )]
    
    async def add_quote(self, slide_number: int, quote: str, x: Optional[float] = None, y: Optional[float] = None, 
                       font_size: Optional[int] = None, font_name: str = "", doc_name: str = "") -> List[TextContent]:
        """添加引用文本"""
        try:
            validate_slide_number(slide_number)
            x_pos, y_pos = validate_coordinates(x, y)
            
            # 处理引用文本中的引号
            escaped_quote = quote.replace('"', '\\"')
            # 使用单引号包围，避免嵌套引号问题
            formatted_quote = f"'{escaped_quote}'"
            
            # 构建字体设置命令
            font_command = f'set font of object text to "{font_name}"' if font_name else ""
            
            result = self.runner.run_inline_script(f'''
                tell application "Keynote"
                    activate
                    if "{doc_name}" is not "" then
                        set targetDoc to document "{doc_name}"
                    else
                        set targetDoc to front document
                    end if
                    
                    tell targetDoc
                        tell slide {slide_number}
                            set newQuote to make new text item with properties {{object text:"{formatted_quote}"}}
                            
                            -- 设置位置（如果指定了x或y坐标）
                            {"" if x is None and y is None else f"set position of newQuote to {{{x_pos}, {y_pos}}}"}
                            
                            tell newQuote
                                set size of object text to {font_size if font_size else 20}
                                {font_command if font_command else "-- no font specified"}
                            end tell
                        end tell
                    end tell
                    
                    return "success"
                end tell
            ''')
            
            return [TextContent(
                type="text",
                text=f"✅ 成功在幻灯片 {slide_number} 添加引用文本"
            )]
            
        except Exception as e:
            return [TextContent(
                type="text",
                text=f"❌ 添加引用文本失败: {str(e)}"
            )]
    
    async def add_image(self, slide_number: int, image_path: str, x: Optional[float] = None, y: Optional[float] = None) -> List[TextContent]:
        """添加图片"""
        try:
            validate_slide_number(slide_number)
            validate_file_path(image_path)
            x_pos, y_pos = validate_coordinates(x, y)
            
            # 构建位置参数
            position_params = ""
            if x is not None and y is not None:
                position_params = f", position:{{{x_pos}, {y_pos}}}"
            
            result = self.runner.run_inline_script(f'''
                tell application "Keynote"
                    activate
                    set targetDoc to front document
                    
                    tell targetDoc
                        tell slide {slide_number}
                            -- 使用正确的alias语法
                            set imageFile to POSIX file "{image_path}" as alias
                            
                            -- 方法1: 尝试标准image对象
                            try
                                set newImage to make new image with properties {{file:imageFile{position_params}}}
                                return "image_success"
                            on error
                                -- 方法2: 尝试movie对象（适用于某些Keynote版本）
                                try
                                    set newMovie to make new movie with properties {{file:imageFile{position_params}}}
                                    return "movie_success"
                                on error
                                    -- 方法3: 使用剪贴板方法
                                    try
                                        tell application "Finder"
                                            select imageFile
                                            copy selection
                                        end tell
                                        
                                        delay 0.5
                                        paste
                                        
                                        return "clipboard_success"
                                    on error
                                        error "所有图片添加方法都失败"
                                    end try
                                end try
                            end try
                        end tell
                    end tell
                end tell
            ''')
            
            return [TextContent(
                type="text",
                text=f"✅ 成功在幻灯片 {slide_number} 添加图片 (方法: {result})"
            )]
            
        except Exception as e:
            return [TextContent(
                type="text",
                text=f"❌ 添加图片失败: {str(e)}"
            )] 