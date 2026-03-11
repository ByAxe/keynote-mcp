#!/usr/bin/env python3
"""
Keynote-MCP basic usage examples
"""

import asyncio
import json
from pathlib import Path


async def demo_presentation_workflow():
    """Demonstrate a complete presentation workflow"""

    print("Keynote-MCP Usage Examples")
    print("=" * 50)

    # 1. Create a new presentation
    print("\n1. Create a new presentation")
    create_command = {
        "tool": "create_presentation",
        "arguments": {
            "title": "My First Presentation",
            "theme": "White"
        }
    }
    print(f"Command: {json.dumps(create_command, indent=2)}")

    # 2. Add a slide
    print("\n2. Add a new slide")
    add_slide_command = {
        "tool": "add_slide",
        "arguments": {
            "layout": "Title Slide"
        }
    }
    print(f"Command: {json.dumps(add_slide_command, indent=2)}")

    # 3. Add title text
    print("\n3. Add title text")
    add_text_command = {
        "tool": "add_text_box",
        "arguments": {
            "slide_number": 1,
            "text": "Welcome to Keynote-MCP",
            "x": 100,
            "y": 200
        }
    }
    print(f"Command: {json.dumps(add_text_command, indent=2)}")

    # 4. Add a content slide
    print("\n4. Add a content slide")
    add_content_slide_command = {
        "tool": "add_slide",
        "arguments": {
            "layout": "Title & Content"
        }
    }
    print(f"Command: {json.dumps(add_content_slide_command, indent=2)}")

    # 5. Add an image
    print("\n5. Add an image")
    add_image_command = {
        "tool": "add_image",
        "arguments": {
            "slide_number": 2,
            "image_path": "/path/to/your/image.png",
            "x": 300,
            "y": 250
        }
    }
    print(f"Command: {json.dumps(add_image_command, indent=2)}")

    # 6. Get presentation info
    print("\n6. Get presentation info")
    get_info_command = {
        "tool": "get_presentation_info"
    }
    print(f"Command: {json.dumps(get_info_command, indent=2)}")

    # 7. Screenshot a slide
    print("\n7. Screenshot a slide")
    screenshot_command = {
        "tool": "screenshot_slide",
        "arguments": {
            "slide_number": 1,
            "output_path": "/tmp/slide1.png",
            "format": "png"
        }
    }
    print(f"Command: {json.dumps(screenshot_command, indent=2)}")

    # 8. Export PDF
    print("\n8. Export PDF")
    export_pdf_command = {
        "tool": "export_pdf",
        "arguments": {
            "output_path": "/tmp/presentation.pdf"
        }
    }
    print(f"Command: {json.dumps(export_pdf_command, indent=2)}")

    # 9. Save presentation
    print("\n9. Save presentation")
    save_command = {
        "tool": "save_presentation"
    }
    print(f"Command: {json.dumps(save_command, indent=2)}")

    print("\nWorkflow complete!")
    print("\nUsage instructions:")
    print("1. Start the Keynote-MCP server: keynote-mcp (or python -m keynote_mcp)")
    print("2. Connect via an MCP client and send the above commands")
    print("3. Ensure Keynote is installed and has necessary permissions")


def demo_batch_operations():
    """Demonstrate batch operations"""

    print("\nBatch Operations Example")
    print("=" * 30)

    # Batch create slides
    slides_data = [
        {"title": "Chapter 1: Introduction", "content": "Project background and goals"},
        {"title": "Chapter 2: Solution", "content": "Technical solution and architecture"},
        {"title": "Chapter 3: Implementation", "content": "Implementation plan and timeline"},
        {"title": "Chapter 4: Summary", "content": "Project summary and outlook"}
    ]

    print("\nBatch create slides:")
    for i, slide_data in enumerate(slides_data, 1):
        print(f"\nSlide {i + 1}:")

        add_slide_cmd = {
            "tool": "add_slide",
            "arguments": {"layout": "Title & Content"}
        }
        print(f"  Add slide: {json.dumps(add_slide_cmd)}")

        add_title_cmd = {
            "tool": "add_text_box",
            "arguments": {
                "slide_number": i + 1,
                "text": slide_data["title"],
                "x": 100,
                "y": 100
            }
        }
        print(f"  Add title: {json.dumps(add_title_cmd)}")

        add_content_cmd = {
            "tool": "add_text_box",
            "arguments": {
                "slide_number": i + 1,
                "text": slide_data["content"],
                "x": 100,
                "y": 300
            }
        }
        print(f"  Add content: {json.dumps(add_content_cmd)}")


def demo_available_tools():
    """Show available tools"""

    print("\nAvailable Tools")
    print("=" * 30)

    tools_by_category = {
        "Presentation Management": [
            "create_presentation - Create a new presentation",
            "open_presentation - Open an existing presentation",
            "save_presentation - Save presentation",
            "close_presentation - Close presentation",
            "list_presentations - List all open presentations",
            "set_presentation_theme - Set presentation theme",
            "get_presentation_info - Get presentation info",
            "get_available_themes - Get available themes"
        ],
        "Slide Operations": [
            "add_slide - Add a new slide",
            "delete_slide - Delete a slide",
            "duplicate_slide - Duplicate a slide",
            "move_slide - Move slide position",
            "get_slide_count - Get slide count",
            "select_slide - Select a specific slide",
            "set_slide_layout - Set slide layout",
            "get_slide_info - Get slide info",
            "get_available_layouts - Get available layouts"
        ],
        "Content Management": [
            "add_text_box - Add a text box",
            "add_image - Add an image"
        ],
        "Export & Screenshots": [
            "screenshot_slide - Screenshot a single slide",
            "export_pdf - Export presentation as PDF",
            "export_images - Export presentation as image sequence"
        ]
    }

    for category, tools in tools_by_category.items():
        print(f"\n{category}:")
        for tool in tools:
            print(f"  - {tool}")


async def main():
    """Main function"""
    await demo_presentation_workflow()
    demo_batch_operations()
    demo_available_tools()

    print("\n" + "=" * 50)
    print("Demo complete!")
    print("See README.md for more details.")


if __name__ == "__main__":
    asyncio.run(main())
