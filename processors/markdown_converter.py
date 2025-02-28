#!/usr/bin/env python3

from typing import Optional
from logging import Logger
from bs4 import BeautifulSoup
import re
from markdownify import markdownify as md
import os

class MarkdownConverter:
    def __init__(self, logger: Logger):
        self.logger = logger
        self.processed_images = set()

    def convert(self, html_content: str, base_path: str = "", output_assets_dir: str = "") -> str:
        """
        Convert HTML content to Wiki.js compatible Markdown.
        
        Args:
            html_content: The HTML content to convert
            base_path: Base path for resolving relative URLs
            output_assets_dir: Directory to save extracted assets
        """
        try:
            # Parse HTML with BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Process images if output_assets_dir is provided
            if output_assets_dir:
                self._process_images(soup, base_path, output_assets_dir)
            
            # Convert to Markdown using markdownify
            markdown_content = md(str(soup), heading_style="ATX")
            
            # Apply Wiki.js specific post-processing
            return self._post_process(markdown_content)
            
        except Exception as e:
            self.logger.error(f"Error converting HTML to Markdown: {str(e)}")
            raise

    def _process_images(self, soup, base_path: str, output_assets_dir: str) -> None:
        """Process images to follow Wiki.js conventions."""
        for img in soup.find_all('img'):
            src = img.get('src', '')
            if not src:
                continue
                
            try:
                # Resolve relative URLs
                if not src.startswith(('http://', 'https://', '/')):
                    src = os.path.join(base_path, src)
                
                # Generate Wiki.js compatible path
                filename = os.path.basename(src)
                wiki_path = f"/assets/images/{filename}"
                
                # Update image src to use Wiki.js path
                img['src'] = wiki_path
                
                # Track processed image for potential extraction
                self.processed_images.add((src, os.path.join(output_assets_dir, 'images', filename)))
                
            except Exception as e:
                self.logger.warning(f"Error processing image {src}: {str(e)}")

    def _post_process(self, content: str) -> str:
        """Clean up and format the final Markdown content for Wiki.js."""
        # Remove multiple blank lines
        content = re.sub(r'\n{3,}', '\n\n', content)
        
        # Ensure proper spacing around headers
        content = re.sub(r'([^\n])\n(#+\s)', r'\1\n\n\2', content)
        
        # Ensure proper spacing around code blocks
        content = re.sub(r'```\n*([^`]+)\n*```', r'\n```\n\1\n```\n', content)
        
        # Fix list formatting
        content = re.sub(r'^(\s*)[*+](\s)', r'\1-\2', content, flags=re.MULTILINE)
        
        # Ensure tables have proper formatting
        content = re.sub(r'\n(\|[^\n]+\|)\n', r'\n\1\n', content)
        
        # Fix blockquote formatting
        content = re.sub(r'^(\s*)>\s*$', r'\1>', content, flags=re.MULTILINE)
        
        return content.strip()
        
    def get_processed_images(self):
        """Return the set of processed images for extraction."""
        return self.processed_images