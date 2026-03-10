#!/usr/bin/env python3
"""
Keynote-MCP 基本使用示例
"""

import asyncio
import json
from pathlib import Path

# 这是一个演示如何使用 Keynote-MCP 的示例
# 在实际使用中，您需要通过 MCP 客户端连接到服务器

async def demo_presentation_workflow():
    """演示完整的演示文稿工作流程"""
    
    print("🎯 Keynote-MCP 使用示例")
    print("=" * 50)
    
    # 1. 创建新演示文稿
    print("\n📝 1. 创建新演示文稿")
    create_command = {
        "tool": "create_presentation",
        "arguments": {
            "title": "我的第一个演示文稿",
            "theme": "白色"
        }
    }
    print(f"命令: {json.dumps(create_command, indent=2, ensure_ascii=False)}")
    
    # 2. 添加幻灯片
    print("\n📄 2. 添加新幻灯片")
    add_slide_command = {
        "tool": "add_slide",
        "arguments": {
            "layout": "标题幻灯片"
        }
    }
    print(f"命令: {json.dumps(add_slide_command, indent=2, ensure_ascii=False)}")
    
    # 3. 添加标题文本
    print("\n✏️ 3. 添加标题文本")
    add_text_command = {
        "tool": "add_text_box",
        "arguments": {
            "slide_number": 1,
            "text": "欢迎使用 Keynote-MCP",
            "x": 100,
            "y": 200
        }
    }
    print(f"命令: {json.dumps(add_text_command, indent=2, ensure_ascii=False)}")
    
    # 4. 添加内容幻灯片
    print("\n📄 4. 添加内容幻灯片")
    add_content_slide_command = {
        "tool": "add_slide",
        "arguments": {
            "layout": "标题与内容"
        }
    }
    print(f"命令: {json.dumps(add_content_slide_command, indent=2, ensure_ascii=False)}")
    
    # 5. 添加图片（如果有的话）
    print("\n🖼️ 5. 添加图片")
    add_image_command = {
        "tool": "add_image",
        "arguments": {
            "slide_number": 2,
            "image_path": "/path/to/your/image.png",
            "x": 300,
            "y": 250
        }
    }
    print(f"命令: {json.dumps(add_image_command, indent=2, ensure_ascii=False)}")
    
    # 6. 获取演示文稿信息
    print("\n📊 6. 获取演示文稿信息")
    get_info_command = {
        "tool": "get_presentation_info"
    }
    print(f"命令: {json.dumps(get_info_command, indent=2, ensure_ascii=False)}")
    
    # 7. 截图幻灯片
    print("\n📸 7. 截图幻灯片")
    screenshot_command = {
        "tool": "screenshot_slide",
        "arguments": {
            "slide_number": 1,
            "output_path": "/tmp/slide1.png",
            "format": "png"
        }
    }
    print(f"命令: {json.dumps(screenshot_command, indent=2, ensure_ascii=False)}")
    
    # 8. 导出 PDF
    print("\n📄 8. 导出 PDF")
    export_pdf_command = {
        "tool": "export_pdf",
        "arguments": {
            "output_path": "/tmp/presentation.pdf"
        }
    }
    print(f"命令: {json.dumps(export_pdf_command, indent=2, ensure_ascii=False)}")
    
    # 9. 保存演示文稿
    print("\n💾 9. 保存演示文稿")
    save_command = {
        "tool": "save_presentation"
    }
    print(f"命令: {json.dumps(save_command, indent=2, ensure_ascii=False)}")
    
    print("\n✅ 演示文稿工作流程完成!")
    print("\n📝 使用说明:")
    print("1. 启动 Keynote-MCP 服务器: keynote-mcp (or python -m keynote_mcp)")
    print("2. 通过 MCP 客户端连接并发送上述命令")
    print("3. 确保 Keynote 应用已安装并有必要的权限")


def demo_batch_operations():
    """演示批量操作"""
    
    print("\n🔄 批量操作示例")
    print("=" * 30)
    
    # 批量创建幻灯片
    slides_data = [
        {"title": "第一章：介绍", "content": "项目背景和目标"},
        {"title": "第二章：方案", "content": "技术方案和架构"},
        {"title": "第三章：实施", "content": "实施计划和时间表"},
        {"title": "第四章：总结", "content": "项目总结和展望"}
    ]
    
    print("\n📚 批量创建幻灯片:")
    for i, slide_data in enumerate(slides_data, 1):
        print(f"\n幻灯片 {i + 1}:")
        
        # 添加幻灯片
        add_slide_cmd = {
            "tool": "add_slide",
            "arguments": {"layout": "标题与内容"}
        }
        print(f"  添加幻灯片: {json.dumps(add_slide_cmd, ensure_ascii=False)}")
        
        # 添加标题
        add_title_cmd = {
            "tool": "add_text_box",
            "arguments": {
                "slide_number": i + 1,
                "text": slide_data["title"],
                "x": 100,
                "y": 100
            }
        }
        print(f"  添加标题: {json.dumps(add_title_cmd, ensure_ascii=False)}")
        
        # 添加内容
        add_content_cmd = {
            "tool": "add_text_box",
            "arguments": {
                "slide_number": i + 1,
                "text": slide_data["content"],
                "x": 100,
                "y": 300
            }
        }
        print(f"  添加内容: {json.dumps(add_content_cmd, ensure_ascii=False)}")


def demo_available_tools():
    """演示可用工具列表"""
    
    print("\n🛠️ 可用工具列表")
    print("=" * 30)
    
    tools_by_category = {
        "演示文稿管理": [
            "create_presentation - 创建新演示文稿",
            "open_presentation - 打开现有演示文稿",
            "save_presentation - 保存演示文稿",
            "close_presentation - 关闭演示文稿",
            "list_presentations - 列出所有打开的演示文稿",
            "set_presentation_theme - 设置演示文稿主题",
            "get_presentation_info - 获取演示文稿信息",
            "get_available_themes - 获取可用主题列表"
        ],
        "幻灯片操作": [
            "add_slide - 添加新幻灯片",
            "delete_slide - 删除幻灯片",
            "duplicate_slide - 复制幻灯片",
            "move_slide - 移动幻灯片位置",
            "get_slide_count - 获取幻灯片数量",
            "select_slide - 选择指定幻灯片",
            "set_slide_layout - 设置幻灯片布局",
            "get_slide_info - 获取幻灯片信息",
            "get_available_layouts - 获取可用布局列表"
        ],
        "内容管理": [
            "add_text_box - 添加文本框",
            "add_image - 添加图片"
        ],
        "导出和截图": [
            "screenshot_slide - 截图单个幻灯片",
            "export_pdf - 导出演示文稿为PDF",
            "export_images - 导出演示文稿为图片序列"
        ]
    }
    
    for category, tools in tools_by_category.items():
        print(f"\n📂 {category}:")
        for tool in tools:
            print(f"  • {tool}")


async def main():
    """主函数"""
    await demo_presentation_workflow()
    demo_batch_operations()
    demo_available_tools()
    
    print("\n" + "=" * 50)
    print("🎉 示例演示完成！")
    print("请参考 README.md 获取更多详细信息。")


if __name__ == "__main__":
    asyncio.run(main()) 