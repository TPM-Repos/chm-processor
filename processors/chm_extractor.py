#!/usr/bin/env python3

import os
from pathlib import Path
from typing import Dict, Generator
import pychm as chm  # Import pychm as chm for compatibility
from logging import Logger

class CHMExtractor:
    def __init__(self, logger: Logger):
        self.logger = logger
        self._processed_files = set()

    def extract(self, chm_dir: str) -> Dict[str, str]:
        """Extract content from CHM directory using streaming approach."""
        self.logger.info(f"Extracting CHM content from: {chm_dir}")
        content_map = {}

        try:
            chm_files = self._find_chm_files(chm_dir)
            for chm_file in chm_files:
                self.logger.debug(f"Processing CHM file: {chm_file}")
                content_map.update(self._process_chm_file(chm_file))

        except Exception as e:
            self.logger.error(f"Error extracting CHM content: {str(e)}")
            raise

        return content_map

    def _find_chm_files(self, directory: str) -> Generator[Path, None, None]:
        """Find all .chm files in the given directory."""
        for root, _, files in os.walk(directory):
            for file in files:
                if file.lower().endswith('.chm'):
                    yield Path(root) / file

    def _process_chm_file(self, chm_path: Path) -> Dict[str, str]:
        """Process a single CHM file using streaming approach."""
        content_map = {}
        chm_obj = chm.chm(str(chm_path))

        try:
            # Get the CHM index
            index = chm_obj.GetIndex()
            if not index:
                self.logger.warning(f"No index found in {chm_path}")
                return content_map

            # Process each topic in the index
            for topic in index:
                if topic.path in self._processed_files:
                    continue

                try:
                    # Extract content in chunks to minimize memory usage
                    content = self._extract_topic_content(chm_obj, topic.path)
                    if content:
                        # Use relative path as key, strip leading slash
                        key = topic.path.lstrip('/')
                        content_map[key] = content
                        self._processed_files.add(topic.path)

                except Exception as e:
                    self.logger.warning(f"Error processing topic {topic.path}: {str(e)}")
                    continue

        finally:
            chm_obj.close()

        return content_map

    def _extract_topic_content(self, chm_obj: chm.chm, topic_path: str, chunk_size: int = 8192) -> str:
        """Extract topic content in chunks to minimize memory usage."""
        try:
            content = []
            ui = chm_obj.ResolveObject(topic_path)
            if not ui:
                return ""

            # Read content in chunks
            while True:
                chunk = ui.Read(chunk_size)
                if not chunk:
                    break
                content.append(chunk.decode('utf-8', errors='ignore'))

            return ''.join(content)

        except Exception as e:
            self.logger.warning(f"Error extracting content from {topic_path}: {str(e)}")
            return ""