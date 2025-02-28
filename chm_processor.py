#!/usr/bin/env python3

import click
import os
from pathlib import Path
from typing import Optional
from tqdm import tqdm
from git import Repo

from processors.chm_extractor import CHMExtractor
from processors.markdown_converter import MarkdownConverter
from utils.file_handler import FileHandler
from utils.logger import setup_logger

@click.command()
@click.option('--input', '-i', required=True, type=click.Path(exists=True),
              help='Path to the unzipped CHM directory')
@click.option('--output', '-o', required=True, type=click.Path(),
              help='Path to the output Markdown GitHub repository')
@click.option('--log', '-l', is_flag=True, help='Enable verbose logging')
def process_chm(input: str, output: str, log: bool) -> None:
    """Process CHM files to Wiki.js compatible Markdown."""
    # Setup logging
    logger = setup_logger(log)
    logger.info(f"Starting CHM processing: {input} -> {output}")
    
    # Initialize components
    file_handler = FileHandler(logger)
    chm_extractor = CHMExtractor(logger)
    markdown_converter = MarkdownConverter(logger)
    
    try:
        # Ensure output directory exists
        output_path = Path(output)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Process CHM content
        chm_content = chm_extractor.extract(input)
        
        # Convert and save markdown files
        for html_file, content in tqdm(chm_content.items(), desc="Converting files"):
            markdown_content = markdown_converter.convert(content)
            output_file = output_path / f"{html_file}.md"
            file_handler.save_markdown(output_file, markdown_content)
        
        # Git operations if output is a repository
        if os.path.exists(output_path / '.git'):
            repo = Repo(output_path)
            repo.index.add('*')
            repo.index.commit('Updated Markdown files from CHM conversion')
            
        logger.info("CHM processing completed successfully")
        
    except Exception as e:
        logger.error(f"Error processing CHM: {str(e)}")
        raise click.ClickException(str(e))

if __name__ == '__main__':
    process_chm()