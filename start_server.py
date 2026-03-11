#!/usr/bin/env python3
"""
Keynote-MCP server startup script
"""

import sys
import os
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def get_messages():
    """Get startup messages"""
    return {
        "starting": "Starting Keynote-MCP Server...",
        "ensure_keynote": "Ensure Keynote application is installed",
        "ensure_permissions": "Ensure necessary system permissions are granted",
        "mcp_ready": "MCP clients can connect to this server",
        "unsplash_enabled": "Unsplash image feature is enabled",
        "unsplash_disabled": "UNSPLASH_KEY environment variable not detected",
        "unsplash_note1": "   Unsplash image feature will be unavailable",
        "unsplash_note2": "   Get API key: https://unsplash.com/developers",
        "env_loaded": "Environment variables loaded from file",
        "env_not_found": ".env file not found, using system environment variables",
        "dotenv_not_installed": "python-dotenv not installed, using system environment variables only",
        "server_stopped": "\nServer stopped",
        "server_failed": "\nServer startup failed"
    }

messages = get_messages()

# Load environment variables
try:
    from dotenv import load_dotenv
    env_path = project_root / '.env'
    if env_path.exists():
        load_dotenv(env_path)
        print(f"{messages['env_loaded']}: {env_path}")
    else:
        print(messages['env_not_found'])
except ImportError:
    print(messages['dotenv_not_installed'])

# Import and run server
from keynote_mcp.server import main

if __name__ == "__main__":
    print(messages['starting'])
    print("=" * 50)
    print(messages['ensure_keynote'])
    print(messages['ensure_permissions'])
    print(messages['mcp_ready'])

    # Check Unsplash configuration
    if os.getenv('UNSPLASH_KEY'):
        print(messages['unsplash_enabled'])
    else:
        print(messages['unsplash_disabled'])
        print(messages['unsplash_note1'])
        print(messages['unsplash_note2'])

    print("=" * 50)

    try:
        main()
    except KeyboardInterrupt:
        print(messages['server_stopped'])
    except Exception as e:
        print(f"{messages['server_failed']}: {e}")
        sys.exit(1)
