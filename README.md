# CHM to Wiki.js Markdown Converter

A command-line tool for converting CHM (Compiled HTML Help) files to Wiki.js-compatible Markdown format.

## Features

- Extracts content from CHM files using disk-based processing (minimizes memory usage)
- Converts HTML to Wiki.js-compatible Markdown
- Handles assets (images, etc.) with proper Wiki.js paths
- Supports Git integration for automatic commits to a separate Markdown repository
- Provides detailed logging and error handling
- Optimized for large CHM files with streaming processing

## Installation

### Prerequisites

- Python 3.7 or higher
- Git (for repository integration)

### Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd chm-processor
   ```

2. Create and activate a virtual environment:
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/macOS
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

```bash
python chm_processor.py --input "/path/to/extracted_chm" --output "/path/to/markdown_repo"
```

### Command-line Options

- `--input`, `-i`: Path to the unzipped CHM directory (required)
- `--output`, `-o`: Path to the output Markdown GitHub repository (required)
- `--assets`, `-a`: Extract and process assets (images, etc.)
- `--git`, `-g`: Commit changes to Git repository
- `--log`, `-l`: Enable verbose logging

### Examples

Process a CHM file and extract assets:
```bash
python chm_processor.py -i "./extracted_chm" -o "./markdown_output" --assets
```

Process a CHM file and commit to Git repository:
```bash
python chm_processor.py -i "./extracted_chm" -o "./markdown_repo" --assets --git
```

## Workflow

1. **Extract CHM Files**: The tool processes CHM files from the input directory.
2. **Convert to Markdown**: HTML content is converted to Wiki.js-compatible Markdown.
3. **Process Assets**: Images and other assets are extracted and paths are updated to follow Wiki.js conventions.
4. **Save to Repository**: Markdown files are saved to the output directory.
5. **Git Integration**: Changes can be automatically committed and pushed to a Git repository.

## Wiki.js Compatibility

The generated Markdown follows Wiki.js standards:
- Headers use ATX style (`# Header`)
- Lists use hyphens for unordered lists (`- Item`)
- Code blocks use triple backticks
- Images use the `/assets/images/` path convention
- Tables use standard Markdown table syntax

For more details on Wiki.js Markdown formatting, see:
- [MarkDownTips.md](MarkDownTips.md)
- [Wiki_Authoring_Standards.md](Wiki_Authoring_Standards.md)

## Project Structure

- `chm_processor.py`: Main entry point and CLI interface
- `processors/`: Core processing modules
  - `chm_extractor.py`: Extracts content from CHM files
  - `markdown_converter.py`: Converts HTML to Markdown
- `utils/`: Utility modules
  - `file_handler.py`: Handles file operations
  - `logger.py`: Logging configuration
- `PLAN.md`: Project implementation plan

## Performance Considerations

- The tool processes one CHM file at a time to minimize memory usage
- Content is read and written in chunks to avoid loading large files into memory
- A hash map tracks processed files to avoid redundant work
- Assets are processed efficiently with proper error handling

## License

[MIT License](LICENSE)