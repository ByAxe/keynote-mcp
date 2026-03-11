---
name: keynote-presentation
description: Creates polished Keynote presentations via keynote-mcp MCP tools with correct layout, font sizing, and theme selection. Use when user says "create a presentation", "make slides", "build a deck", or asks to use Keynote MCP tools. Handles font clipping bugs, theme pitfalls, coordinate math, and landing-page-style slide design.
license: MIT
compatibility: Requires macOS with Keynote installed and keynote-mcp MCP server connected. Works with Claude Code and Claude.ai.
metadata:
    author: ByAxe
    version: 1.0.0
    mcp-server: keynote-mcp
---

# Keynote Presentation Builder

Build polished, visually correct Keynote presentations using the keynote-mcp MCP tools. This skill encodes hard-won layout rules, font sizing workarounds, theme pitfalls, and design patterns from real production use.

## Instructions

### Step 1: Setup and slide size

Always start by confirming the canvas dimensions and picking a theme.

```
get_slide_size()
get_available_themes()
create_presentation(title="...", theme="Slate")
```

Use "Slate" theme by default — it applies a dark gradient background to all slide layouts including Blank. Consult `references/theme-reference.md` for the full compatibility table.

After creating the presentation, set slide 1 to "Blank" layout to remove invisible theme placeholder elements that overlap your content:

```
set_slide_layout(slide_number=1, layout="Blank")
```

### Step 2: Add all slides at once

Batch-create all slides before adding content. This avoids index confusion.

```
add_slide(position=2)
add_slide(position=3)
# ... etc
```

### Step 3: Add content following the font size rules

**CRITICAL BUG**: `add_title` with `font_size` greater than 48 creates a default-sized text box that clips the text. You will see only 1-2 characters.

**Workaround for large titles (font_size over 48):**

1. Add the title at the desired font size (text will be clipped):
```
add_title(slide_number=1, title="Keynote MCP", x=480, y=260, font_size=96)
```

2. Get the element index:
```
get_slide_content(slide_number=1)
# Find: TEXT:N:::r:::480,260:::43,123 (text is truncated)
```

3. Resize the text box to fit:
```
resize_element(slide_number=1, element_type="text", element_index=N, width=900, height=140)
```

4. Restore the truncated text:
```
edit_text_item(slide_number=1, item_index=N, new_text="Keynote MCP")
```

**Safe font sizes (no workaround needed):**
- add_title: up to 48pt
- add_subtitle: up to 32pt
- add_bullet_list / add_numbered_list: up to 28pt
- add_code_block: up to 20pt

### Step 4: Center text manually

There is no text-align property. Text is always left-aligned within its box. To visually center, estimate the rendered width and offset x.

Consult `references/coordinate-reference.md` for per-character width estimates and centering formulas.

Quick reference for a 1920x1080 slide (center at 960, 540):
- Short title at 64pt (~12 chars): x = 660
- Medium subtitle at 28pt (~25 chars): x = 560
- Footer text: y = 950-960

### Step 5: Detect and fix overlaps

After adding elements, verify positions:

```
get_slide_content(slide_number=N)
```

Calculate: if element A is at y=300 with height=638, it extends to y=938. Any element placed at y less than 938 will overlap. Fix with:

```
move_element(slide_number=N, element_type="text", element_index=M, x=..., y=940)
```

When deleting multiple elements, always delete from highest index to lowest to avoid index shifting.

### Step 6: Screenshot and verify every slide

After building each slide:

```
screenshot_slide(slide_number=N, output_path="/tmp/slideN.png")
```

Then read the image to visually verify. Check for:
- Text clipping (only partial text visible)
- Element overlaps
- Content overflowing slide edges
- Alignment issues

Fix problems before moving to the next slide.

## Design Patterns: Landing Page Style

Treat each slide as one section of a landing page. One idea per slide. Max content:
- 1 title + 1 subtitle + 3-5 bullets, OR
- 1 title + 1 code block (6 lines max), OR
- 1 centered quote/statement

### Font hierarchy
- 96pt: Hero title only (requires resize workaround)
- 64-72pt: Section titles
- 48pt: Large statements or quotes
- 28-32pt: Subtitles
- 24-26pt: Body text and bullets
- 20pt: Code blocks
- 18pt: Footnotes and captions

### Recommended fonts
- Titles: "Helvetica Neue Bold" or "Helvetica Neue"
- Subtitles/body: "Helvetica Neue Light"
- Code: "Menlo" or "Monaco"

## Slide Templates

### Hero slide
```
add_title(slide=1, title="Product Name", x=CENTER, y=260, font_size=96)
# Then resize + edit_text_item to fix clipping
add_subtitle(slide=1, subtitle="One-line tagline", x=CENTER, y=440, font_size=32)
add_text_box(slide=1, text="tag1 // tag2 // tag3", x=CENTER, y=520)
add_text_box(slide=1, text="github.com/org/repo", x=CENTER, y=960)
```

### Statement slide
```
add_quote(slide=2, quote="Provocative question?", x=280, y=380, font_size=48)
```

### Title + bullets slide
```
add_title(slide=N, title="Section Name", x=CENTER, y=100, font_size=64)
add_subtitle(slide=N, subtitle="Context line", x=CENTER, y=190, font_size=26)
add_bullet_list(slide=N, items=[...], x=350, y=340, font_size=26)
```

### Code demo slide
```
add_title(slide=N, title="How It Works", x=CENTER, y=80, font_size=56)
add_subtitle(slide=N, subtitle="Short explainer", x=CENTER, y=165, font_size=28)
add_code_block(slide=N, code="...", x=350, y=300, font_size=20, font_name="Menlo")
```

### Closing slide
```
add_title(slide=N, title="Big closing statement.", x=CENTER, y=340, font_size=56)
add_subtitle(slide=N, subtitle="Supporting line.", x=CENTER, y=430, font_size=30)
add_text_box(slide=N, text="repo link", x=CENTER, y=580)
add_text_box(slide=N, text="License // Credits", x=CENTER, y=960)
```

## Build Animations (Appear One-by-One)

To make bullet lists or other elements appear incrementally during the slideshow:

```
# Make bullets appear one at a time on click
add_build_in(slide_number=10, element_type="text", element_index=18, effect="Appear", delivery="By Paragraph")

# Remove animation
remove_build_in(slide_number=10, element_type="text", element_index=18)
```

Effects: `Appear`, `Dissolve`, `Move In`, `Fade and Move`, `Scale`, `Pop`, `Typewriter`

Delivery: `All at Once`, `By Paragraph` (for bullet-by-bullet), `By Highlighted Paragraph`

**Notes**: Uses UI scripting — Keynote must be active with accessibility permissions. For PDF with build stages: File > Export to > PDF > check "Print each stage of builds".

## Common Issues

### Text shows only 1-2 characters
Cause: Font size too large for auto-sized text box.
Solution: `resize_element` to make box bigger, then `edit_text_item` to restore text.

### Theme background not visible
Cause: Some themes (Gradient, Minimalist Dark) don't apply backgrounds to Blank slides.
Solution: Use "Slate", "Bold Colour", or "Basic Black" themes. See `references/theme-reference.md`.

### Elements overlap
Cause: Multi-line text (bullets, code) takes more vertical space than estimated.
Solution: `get_slide_content` to check actual heights, then `move_element` to fix.

### Cannot delete empty elements
Cause: Theme placeholder artifacts at position (0,0). They are invisible and harmless.
Solution: Ignore them.

### MCP server returns old behavior after code changes
Cause: MCP server process is still running old code.
Solution: Restart Claude Code session or use `/mcp` to restart the server.

## Checklist

1. `get_slide_size` to confirm 1920x1080
2. `get_available_themes` and pick theme (Slate recommended)
3. `create_presentation` with theme
4. Add all slides in batch
5. Set slide 1 to "Blank" layout if not already
6. Build content using templates above
7. For large titles: add, get index, resize box, edit text if truncated
8. Screenshot each slide and read image to verify
9. Fix overlaps via get_slide_content + move_element
10. Final screenshot pass of all slides
