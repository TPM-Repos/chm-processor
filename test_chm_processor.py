#!/usr/bin/env python3

import os
import sys
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from processors.chm_extractor import CHMExtractor
from processors.markdown_converter import MarkdownConverter
from utils.file_handler import FileHandler
from utils.logger import setup_logger


class TestCHMProcessor(unittest.TestCase):
    """Test cases for CHM Processor components."""

    def setUp(self):
        """Set up test environment."""
        self.logger = setup_logger(verbose=True)
        self.test_dir = Path("test_output")
        self.test_dir.mkdir(exist_ok=True)

    def tearDown(self):
        """Clean up test environment."""
        # Remove test files
        for file in self.test_dir.glob("*"):
            if file.is_file():
                file.unlink()
        
        # Remove test directory
        if self.test_dir.exists():
            self.test_dir.rmdir()

    @patch('pychm.chm')
    def test_chm_extractor(self, mock_chm):
        """Test CHM extraction functionality."""
        # Mock CHM object
        mock_chm_instance = MagicMock()
        mock_chm.return_value = mock_chm_instance
        
        # Mock index and content
        mock_topic = MagicMock()
        mock_topic.path = "/test.html"
        mock_chm_instance.GetIndex.return_value = [mock_topic]
        
        # Mock ResolveObject and Read
        mock_ui = MagicMock()
        mock_ui.Read.return_value = b"<html><body><h1>Test</h1><p>Content</p></body></html>"
        mock_chm_instance.ResolveObject.return_value = mock_ui
        
        # Create extractor and test
        extractor = CHMExtractor(self.logger)
        
        # Mock finding CHM files
        with patch.object(extractor, '_find_chm_files') as mock_find:
            mock_find.return_value = [Path("test.chm")]
            content = extractor.extract("dummy_path")
            
            # Verify content
            self.assertIn("test.html", content)
            self.assertIn("<h1>Test</h1>", content["test.html"])

    def test_markdown_converter(self):
        """Test Markdown conversion functionality."""
        converter = MarkdownConverter(self.logger)
        
        # Test basic HTML conversion
        html = "<html><body><h1>Test Heading</h1><p>Test paragraph</p><ul><li>Item 1</li><li>Item 2</li></ul></body></html>"
        markdown = converter.convert(html)
        
        # Verify conversion
        self.assertIn("# Test Heading", markdown)
        self.assertIn("Test paragraph", markdown)
        self.assertIn("- Item 1", markdown)
        self.assertIn("- Item 2", markdown)

    def test_file_handler(self):
        """Test file handling functionality."""
        handler = FileHandler(self.logger)
        
        # Test saving markdown
        test_file = self.test_dir / "test.md"
        test_content = "# Test\n\nThis is a test."
        handler.save_markdown(test_file, test_content)
        
        # Verify file was saved
        self.assertTrue(test_file.exists())
        
        # Verify content
        with open(test_file, 'r', encoding='utf-8') as f:
            content = f.read()
            self.assertEqual(content, test_content)
        
        # Test file hash
        file_hash = handler.get_file_hash(str(test_file))
        self.assertTrue(len(file_hash) > 0)
        
        # Test is_file_processed
        self.assertTrue(handler.is_file_processed(str(test_file)))


if __name__ == "__main__":
    unittest.main()