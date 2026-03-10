# CLAUDE.md — keynote-mcp

## What this is

An MCP (Model Context Protocol) server that controls Apple Keynote via AppleScript. It exposes tools for creating presentations, managing slides, adding content (text, images, lists, code blocks), exporting, and fetching images from Unsplash.

## How to run

```bash
cd /Users/alekseilitvinau/src/keynote-mcp
.venv/bin/python -m keynote_mcp
```

Registered in Claude Code as:
```
keynote-mcp: bash -c cd /Users/alekseilitvinau/src/keynote-mcp && .venv/bin/python -m keynote_mcp
```

**After any code changes, the MCP server must be restarted** (exit/re-enter the Claude Code session or use `/mcp` to restart).

## Project structure

```
src/
  keynote_mcp/             — Installable Python package
    __init__.py            — Package version
    __main__.py            — python -m keynote_mcp entry point
    server.py              — Main MCP server: registers handlers, routes tool calls
    tools/
      presentation.py      — create/open/save/close/list presentations, themes, resolution
      slide.py             — add/delete/duplicate/move slides, layouts
      content.py           — add text boxes/titles/subtitles/lists/code/quotes/images,
                             edit/delete/move/resize elements, speaker notes, get_slide_content
      export.py            — screenshot slides, export PDF
      unsplash.py          — search/add Unsplash images (requires UNSPLASH_KEY env var)
    utils/
      applescript_runner.py — Executes AppleScript via osascript subprocess (30s timeout)
      error_handler.py     — Exception hierarchy + validation functions
    applescript/
      keynote_base.applescript   — Base helpers (get doc reference)
      presentation.applescript   — Presentation operations
      slide.applescript          — Slide operations
      content.applescript        — Content manipulation (text, images, lists)
      export.applescript         — Export/screenshot operations
tests/                     — Test scaffolding (unit/ and integration/)
```

## Architecture

1. **server.py** — Single `KeynoteMCPServer` class. Uses `mcp` library's `Server` with stdio transport. All tool calls go through one big if/elif dispatch in `call_tool()`.
2. **Tool classes** — Each `*Tools` class has `get_tools()` (returns `List[Tool]` with schemas) and async methods per tool. They use `AppleScriptRunner` to execute scripts.
3. **AppleScriptRunner** — Runs AppleScript via `osascript -e` subprocess. Can run inline scripts or load `.scpt` files. Scripts are in `src/keynote_mcp/applescript/`.
4. **Error hierarchy** — `KeynoteError` base → `AppleScriptError`, `FileOperationError`, `ParameterError`. Validation helpers: `validate_slide_number`, `validate_coordinates`, `validate_file_path`, `validate_element_type`, `validate_dimensions`.

## Key patterns

- **All tool methods are async** but the actual AppleScript execution is synchronous (subprocess). The async is for MCP protocol compatibility.
- **Tool schemas** are defined inline in each `get_tools()` method as `inputSchema` dicts. If you add a new tool, add the schema there AND the routing in `server.py:call_tool()`.
- **AppleScript files** use `.applescript` extension for source but `.scpt` for compiled. The runner looks for `.scpt` files. After editing `.applescript` sources, they need to be compiled (`osacompile`).
- **doc_name parameter** — Most tools accept an optional `doc_name` to target a specific open presentation. Empty string defaults to the frontmost document.
- **Coordinate system** — Origin (0,0) is top-left of the slide. Default Keynote slide is 1920x1080 (check with `get_slide_size`).
- **Content indexing** — `get_slide_content` returns pipe-delimited text with element types, indices, text, position, and size. Use these indices for `edit_text_item`, `delete_element`, `move_element`, `resize_element`.

## Development

```bash
# Activate venv
source .venv/bin/activate

# Install deps
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Run tests
pytest tests/ -v

# Lint
flake8 src/ tests/
mypy src/

# Format
black src/ tests/
isort src/ tests/
```

## Environment variables

- `UNSPLASH_KEY` — Required only for Unsplash image tools. Get from https://unsplash.com/developers

## Common pitfalls

- Editing `.applescript` files won't take effect until they're compiled to `.scpt` and the MCP server is restarted.
- Keynote must be running and have accessibility permissions for AppleScript to work.
- The `osascript` subprocess has a 30-second timeout — complex operations on large presentations may fail.
- The Makefile still has Chinese comments — translate if touching it.
- `env.example` still has Chinese comments — translate if touching it.

## Adding a new tool

1. Add the tool schema in the appropriate `*Tools.get_tools()` method
2. Add the async handler method in the same class
3. Add the routing case in `server.py:call_tool()`
4. If it needs AppleScript, add the function in the corresponding `.applescript` file and compile it
5. Restart the MCP server
