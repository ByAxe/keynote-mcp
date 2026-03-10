#!/usr/bin/env python3
"""
Keynote-MCP Setup Script (legacy - pyproject.toml is the primary config)
"""

from setuptools import setup, find_packages
import os


def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()


def read_requirements():
    try:
        with open("requirements.txt", "r", encoding="utf-8") as fh:
            return [line.strip() for line in fh if line.strip() and not line.startswith("#")]
    except FileNotFoundError:
        return [
            "mcp>=1.0.0",
            "typing-extensions>=4.0.0",
            "aiohttp>=3.8.0",
            "aiofiles>=0.8.0",
            "Pillow>=9.0.0",
            "python-dotenv>=1.0.0",
        ]


def read_version():
    version_file = os.path.join("src", "keynote_mcp", "__init__.py")
    if os.path.exists(version_file):
        with open(version_file, "r", encoding="utf-8") as fh:
            for line in fh:
                if line.startswith("__version__"):
                    return line.split("=")[1].strip().strip('"').strip("'")
    return "1.0.0"


setup(
    name="keynote-mcp",
    version=read_version(),
    author="easychen",
    author_email="easychen@gmail.com",
    description="An MCP server for controlling Apple Keynote presentations via AppleScript",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/easychen/keynote-mcp",
    project_urls={
        "Bug Reports": "https://github.com/easychen/keynote-mcp/issues",
        "Source": "https://github.com/easychen/keynote-mcp",
        "Documentation": "https://github.com/easychen/keynote-mcp/blob/main/docs/README.md",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Graphics :: Presentation",
        "Topic :: Office/Business :: Office Suites",
    ],
    python_requires=">=3.10",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "isort>=5.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
            "bandit>=1.7.0",
            "safety>=2.0.0",
        ],
        "docs": [
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
            "sphinx-autodoc-typehints>=1.19.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "keynote-mcp=keynote_mcp.server:main",
        ],
    },
    include_package_data=True,
    package_data={
        "keynote_mcp": ["applescript/*.scpt", "applescript/*.applescript"],
    },
    zip_safe=False,
    keywords=[
        "keynote",
        "mcp",
        "model-context-protocol",
        "applescript",
        "automation",
        "presentation",
        "macos",
        "ai",
        "llm",
    ],
    platforms=["macOS"],
)
