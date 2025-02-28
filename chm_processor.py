#!/usr/bin/env python3

import click
import os
from pathlib import Path
from typing import Optional
from tqdm import tqdm
from git import Repo
import time

from processors.chm_extractor import CHMExtractor
from processors.markdown_converter import MarkdownConverter
from utils.file_handler import FileHandler
from utils.logger import setup_logger

@click.command()
@click.option('--input', '-i', required=True, type=click.Path(exists=True),
              help='Path to the unzipped CHM directory')
@click.option('--output', '-o', required=True, type=click.Path(),
              help='Path to the output Markdown GitHub repository')
@click.option('--assets', '-a', is_flag=True, help='Extract and process assets (images, etc.)')
@click.option('--git', '-g', is_flag=True, help='Commit changes to Git repository')
@click.option('--log', '-l', is_flag=True, help='Enable verbose logging')
def process_chm(input: str, output: str, assets: bool, git: bool, log: bool) -> None:
    """Process CHM files to Wiki.js compatible Markdown."""
    # Setup logging
    logger = setup_logger(log)
    logger.info(f"Starting CHM processing: {input} -> {output}")
    start_time = time.time()
    
    # Initialize components
    file_handler = FileHandler(logger)
    chm_extractor = CHMExtractor(logger)
    markdown_converter = MarkdownConverter(logger)
    
    try:
        # Ensure output directory exists
        output_path = Path(output)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Create assets directory if needed
        assets_dir = output_path / "assets"
        if assets:
            assets_dir.mkdir(parents=True, exist_ok=True)
            (assets_dir / "images").mkdir(exist_ok=True)
        
        # Process CHM content
        logger.info("Extracting CHM content...")
        chm_content = chm_extractor.extract(input)
        logger.info(f"Found {len(chm_content)} HTML files to process")
        
        # Convert and save markdown files
        processed_count = 0
        for html_file, content in tqdm(chm_content.items(), desc="Converting files"):
            # Skip already processed files
            output_file = output_path / f"{html_file}.md"
            if file_handler.is_file_processed(str(output_file)):
                logger.debug(f"Skipping already processed file: {html_file}")
                continue
                
            # Convert HTML to Markdown
            markdown_content = markdown_converter.convert(
                content,
                base_path=os.path.dirname(os.path.join(input, html_file)),
                output_assets_dir=str(assets_dir) if assets else ""
            )
            
            # Save Markdown file
            file_handler.save_markdown(output_file, markdown_content)
            processed_count += 1
            
        # Extract assets if enabled
        if assets:
            logger.info("Extracting assets...")
            file_handler.extract_assets(markdown_converter.get_processed_images())
        
        # Git operations if output is a repository and git flag is set
        if git and os.path.exists(output_path / '.git'):
            logger.info("Committing changes to Git repository...")
            repo = Repo(output_path)
            repo.git.add(A=True)  # Add all changes including new files
            
            # Only commit if there are changes
            if repo.is_dirty() or len(repo.untracked_files) > 0:
                commit_message = f"Updated Markdown files from CHM conversion ({processed_count} files)"
                repo.index.commit(commit_message)
                
                # Push if remote exists
                if len(repo.remotes) > 0:
                    logger.info("Pushing changes to remote repository...")
                    origin = repo.remotes.origin
                    origin.push()
            else:
                logger.info("No changes to commit")
        
        # Log completion statistics
        elapsed_time = time.time() - start_time
        logger.info(f"CHM processing completed successfully in {elapsed_time:.2f} seconds")
        logger.info(f"Processed {processed_count} files out of {len(chm_content)} total files")
        
    except Exception as e:
        logger.error(f"Error processing CHM: {str(e)}")
        raise click.ClickException(str(e))

if __name__ == '__main__':
    process_chm()