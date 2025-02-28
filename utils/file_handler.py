#!/usr/bin/env python3

from pathlib import Path
from typing import Optional
from logging import Logger

class FileHandler:
    def __init__(self, logger: Logger):
        self.logger = logger

    def save_markdown(self, file_path: Path, content: str) -> None:
        """Save Markdown content to file, creating directories as needed."""
        try:
            # Ensure parent directories exist
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Write content to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
                
            self.logger.debug(f"Saved Markdown file: {file_path}")
            
        except Exception as e:
            self.logger.error(f"Error saving file {file_path}: {str(e)}")
            raise

    def ensure_directory(self, directory: Path) -> None:
        """Ensure directory exists, create if necessary."""
        try:
            directory.mkdir(parents=True, exist_ok=True)
            self.logger.debug(f"Ensured directory exists: {directory}")
        except Exception as e:
            self.logger.error(f"Error creating directory {directory}: {str(e)}")
            raise