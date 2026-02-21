# Static Site Generator

A Python-based static site generator that converts Markdown content into a fully-functional HTML website. This is a guided project from [Boot.dev](https://www.boot.dev/).

## What It Accomplishes

This project demonstrates how static site generators work by:
- Parsing Markdown files and converting them to HTML
- Processing inline formatting (bold, italic, code, links, images)
- Building an HTML site from templates
- Serving the generated site locally via HTTP

The generator takes raw Markdown content, applies a consistent HTML template, and produces a static website ready for deployment.

## Architecture

```
┌─────────────────┐
│    Browser      │ Displays generated site
└────────┬────────┘
         │ (http://localhost:8888)
┌────────▼────────────────┐
│   File Server           │ Serves HTML files
│ (python3 -m http.server)│
└────────┬────────────────┘
         │
    ┌────▼─────┐
    │  public/  │ Generated HTML output
    │  or docs/ │
    └────┬─────┘
         │
    ┌────▼──────────────────┐
    │   src/main.py         │ Main generator script
    │  - block_split.py     │
    │  - inline_split.py    │
    │  - generatepage.py    │
    │  - htmlnode.py        │
    │  - textnode.py        │
    └────┬──────────────────┘
         │
    ┌────▼──────────────┐
    │  static/          │ Static assets
    │  - index.css      │ (styles, images)
    │  - images/        │
    └───────────────────┘
         │
    ┌────▼──────────────────┐
    │  src/content/         │ Markdown files
    │  (provided by Boot.dev)
    │                       │
    └───────────────────────┘
         │
    ┌────▼──────────────────┐
    │  src/template.html    │ HTML template
    │                       │ (applied to all pages)
    └───────────────────────┘
```

## Running the Project

### Quick Start

```bash
./main.sh
```

This shell script:
1. **Builds the site**: Runs `python3 src/main.py` to generate HTML from Markdown
2. **Starts the server**: Launches a local HTTP server on port 8888
3. **Open in browser**: Visit `http://localhost:8888` to view the generated site

### Manual Steps

If you prefer to run components separately:

```bash
# Build the static site
python3 src/main.py

# Start the file server in the public directory
cd public && python3 -m http.server 8888

# Then visit http://localhost:8888 in your browser
```

## What I Learned

### Static Sites
- How static site generators work (markdown → HTML conversion)
- The benefits of static sites: fast, secure, simple deployment
- How to use templates to maintain consistent styling across pages

### Python OOP and Functional Programming
- **OOP Concepts**:
  - Class design and encapsulation (`TextNode`, `HTMLNode`, `LeafNode`, `ParentNode`)
  - Inheritance hierarchies for different node types
  - Using Enums for type safety (`TextType`, `BlockType`)
- **Functional Programming**:
  - Composable functions for text processing (`split_nodes_delimiter`, `split_nodes_image`, `split_nodes_link`)
  - Function chaining for sequential transformations
  - Recursive functions for directory traversal

### Python Unit Testing
- Writing comprehensive unit tests with `unittest`
- Testing edge cases and error conditions
- Using assertions and context managers for exception testing
- Organizing tests into logical test classes

## Notes & Potential Features

### Current Implementation
- **Markdown Source**: Currently uses Markdown files provided by Boot.dev
- **Single Deployment Target**: Generates a static site with a fixed basepath
- **GitHub Pages Support**: Configurable basepath for deploying to GitHub Pages subdirectories

### Future Enhancement Ideas

#### Short-term Improvements
- **Custom Markdown Support**: Add ability to include custom Markdown files alongside provided content
  - Allow users to create their own `.md` files in `src/content/`
  - Merge custom content with provided content during build
  
- **Nested Inline Element Support**: Currently inline elements (bold, italic, code) cannot be nested
  - Example: `***bold italic***` or `**bold with `code` inside**`
  - Requires parsing strategy update to handle precedence rules
  
- **Theming System**: Multiple CSS themes that users can select
  - Separate template files for different visual styles
  - Theme selection via CLI argument

#### Long-term Vision: Full Web Application
Transform this into a complete web platform with:
- **User Authentication**: Register, login, password management
- **Markdown Editor**: In-browser markdown editor with live preview
- **Content Management**: Users can create, edit, delete their own markdown notes
- **Database Storage**: Store user content in a database instead of filesystem
- **Sharing & Collaboration**: Share notes with other users, comments/feedback
- **Search Functionality**: Full-text search across all published notes
- **Multiple Export Formats**: Export to PDF, DOCX, etc.

#### Technical Debt & Improvements
- Implement full nested inline element parsing
- Add support for more Markdown features (tables, footnotes, etc.)
- Performance optimization for large sites
- Caching mechanisms for faster rebuilds
- Configuration file support (YAML/TOML)
