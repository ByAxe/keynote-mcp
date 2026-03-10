"""Shared fixtures for keynote-mcp tests."""

import subprocess
from unittest.mock import MagicMock, patch

import pytest

from keynote_mcp.utils.applescript_runner import AppleScriptRunner
from keynote_mcp.tools.content import ContentTools


@pytest.fixture
def mock_subprocess_run():
    """Patch subprocess.run to prevent real osascript calls."""
    with patch("keynote_mcp.utils.applescript_runner.subprocess.run") as mock_run:
        mock_run.return_value = subprocess.CompletedProcess(
            args=["osascript", "-e", ""],
            returncode=0,
            stdout="success",
            stderr="",
        )
        yield mock_run


@pytest.fixture
def runner(mock_subprocess_run):
    """AppleScriptRunner with mocked subprocess."""
    return AppleScriptRunner()


@pytest.fixture
def content_tools(mock_subprocess_run):
    """ContentTools with mocked AppleScript runner."""
    return ContentTools()
