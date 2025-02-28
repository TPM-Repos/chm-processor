#!/usr/bin/env python3

from pathlib import Path
import os
import shutil
from typing import Optional, Set, Tuple
from logging import Logger
import hashlib

class FileHandler:
    def __init__(self, logger: Logger):
        self.logger = logger
        self.processed_files = set()

    def save_markdown(self, file_path: Path, content: str) -> None:
        """Save Markdown content to file, creating directories as needed."""
        try:
            # Ensure parent directories exist
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Write content to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
                
            self.logger.debug(f"Saved Markdown file: {file_path}")
            self.processed_files.add(str(file_path))
            
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
            
    def extract_assets(self, assets: Set[Tuple[str, str]]) -> None:
        """
        Extract assets (images, etc.) to their target locations.
        
        Args:
            assets: Set of tuples (source_path, target_path)
        """
        for source_path, target_path in assets:
            try:
                # Ensure target directory exists
                target_dir = os.path.dirname(target_path)
                os.makedirs(target_dir, exist_ok=True)
                
                # Copy the file if it exists and is accessible
                if os.path.isfile(source_path):
                    shutil.copy2(source_path, target_path)
                    self.logger.debug(f"Copied asset: {source_path} -> {target_path}")
                else:
                    self.logger.warning(f"Asset not found: {source_path}")
                    
            except Exception as e:
                self.logger.warning(f"Error extracting asset {source_path}: {str(e)}")
                
    def get_file_hash(self, file_path: str) -> str:
        """Get MD5 hash of a file to track changes."""
        try:
            with open(file_path, 'rb') as f:
                return hashlib.md5(f.read()).hexdigest()
        except Exception as e:
            self.logger.warning(f"Error hashing file {file_path}: {str(e)}")
            return ""
            
    def is_file_processed(self, file_path: str) -> bool:
        """Check if a file has already been processed."""
        return file_path in self.processed_files