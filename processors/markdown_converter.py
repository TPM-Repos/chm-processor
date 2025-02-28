#!/usr/bin/env python3

from typing import Optional
from logging import Logger
from bs4 import BeautifulSoup
import re

class MarkdownConverter:
    def __init__(self, logger: Logger):
        self.logger = logger

    def convert(self, html_content: str) -> str:
        """Convert HTML content to Wiki.js compatible Markdown."""
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            markdown_content = self._process_element(soup.body)
            return self._post_process(markdown_content)
        except Exception as e:
            self.logger.error(f"Error converting HTML to Markdown: {str(e)}")
            raise

    def _process_element(self, element) -> str:
        """Process HTML elements recursively and convert to Markdown."""
        if element is None:
            return ""

        content = []
        for child in element.children:
            if child.name is None:  # Text node
                text = child.string
                if text and not text.isspace():
                    content.append(text.strip())
            else:
                content.append(self._convert_element(child))

        return '\n'.join(filter(None, content))

    def _convert_element(self, element) -> str:
        """Convert specific HTML elements to Markdown format."""
        tag = element.name

        # Handle headers
        if tag and tag.startswith('h') and len(tag) == 2:
            level = int(tag[1])
            return f"{'#' * level} {element.get_text().strip()}"

        # Handle paragraphs
        if tag == 'p':
            return f"\n{self._process_element(element)}\n"

        # Handle lists
        if tag == 'ul':
            items = [f"- {self._process_element(li)}" for li in element.find_all('li', recursive=False)]
            return '\n'.join(items)
        if tag == 'ol':
            items = [f"{i+1}. {self._process_element(li)}" for i, li in enumerate(element.find_all('li', recursive=False))]
            return '\n'.join(items)

        # Handle code blocks
        if tag == 'pre':
            code = element.find('code')
            if code:
                return f"```\n{code.get_text()}\n```"
            return f"```\n{element.get_text()}\n```"

        # Handle inline code
        if tag == 'code':
            return f"`{element.get_text()}`"

        # Handle links
        if tag == 'a':
            href = element.get('href', '')
            text = element.get_text() or href
            return f"[{text}]({href})"

        # Handle images
        if tag == 'img':
            src = element.get('src', '')
            alt = element.get('alt', '')
            return f"![{alt}]({src})"

        # Handle tables
        if tag == 'table':
            return self._convert_table(element)

        # Handle blockquotes
        if tag == 'blockquote':
            lines = self._process_element(element).split('\n')
            return '\n'.join(f"> {line}" for line in lines)

        # Default case: process children
        return self._process_element(element)

    def _convert_table(self, table) -> str:
        """Convert HTML table to Markdown table format."""
        rows = []
        headers = []

        # Process headers
        for th in table.find_all('th'):
            headers.append(th.get_text().strip())

        if headers:
            rows.append('| ' + ' | '.join(headers) + ' |')
            rows.append('| ' + ' | '.join(['---'] * len(headers)) + ' |')

        # Process rows
        for tr in table.find_all('tr'):
            cells = [td.get_text().strip() for td in tr.find_all('td')]
            if cells:  # Skip empty rows and header rows
                rows.append('| ' + ' | '.join(cells) + ' |')

        return '\n'.join(rows)

    def _post_process(self, content: str) -> str:
        """Clean up and format the final Markdown content."""
        # Remove multiple blank lines
        content = re.sub(r'\n{3,}', '\n\n', content)
        
        # Ensure proper spacing around headers
        content = re.sub(r'([^\n])\n(#+\s)', r'\1\n\n\2', content)
        
        # Ensure proper spacing around code blocks
        content = re.sub(r'```\n*([^`]+)\n*```', r'\n```\n\1\n```\n', content)
        
        return content.strip()