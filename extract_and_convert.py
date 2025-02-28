#!/usr/bin/env python3

import os
import sys
import argparse
import subprocess
import tempfile
import shutil
from pathlib import Path
import win32com.client
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import re
import logging
from tqdm import tqdm
import time

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('chm_processor')

def extract_chm(chm_path, output_dir):
    """Extract CHM file using hh.exe command-line tool."""
    logger.info(f"Extracting CHM file: {chm_path}")
    
    try:
        # Create a temporary directory for extraction
        temp_dir = tempfile.mkdtemp()
        logger.info(f"Using temporary directory: {temp_dir}")
        
        # Use 7-Zip to extract the CHM file
        try:
            cmd = f'"C:\\Program Files\\7-Zip\\7z.exe" x "{chm_path}" -o"{temp_dir}"'
            logger.debug(f"Running command: {cmd}")
            result = subprocess.run(
                cmd,
                shell=True,
                check=False,
                capture_output=True,
                text=True
            )
            
            if result.returncode != 0:
                logger.warning(f"7-Zip extraction failed: {result.stderr}")
                logger.info("Trying alternative extraction method...")
                
                # Alternative: Try using hh.exe
                try:
                    cmd = f'hh.exe -decompile "{temp_dir}" "{chm_path}"'
                    logger.debug(f"Running command: {cmd}")
                    result = subprocess.run(
                        cmd,
                        shell=True,
                        check=False,
                        capture_output=True,
                        text=True
                    )
                    
                    if result.returncode != 0:
                        logger.warning(f"hh.exe command failed: {result.stderr}")
                        raise Exception("Both extraction methods failed")
                except:
                    # If both methods fail, try to use the CHM as-is
                    logger.warning("Both extraction methods failed, trying to process CHM directly")
                    shutil.copy2(chm_path, os.path.join(temp_dir, "original.chm"))
        except Exception as e:
            logger.warning(f"Extraction command failed: {str(e)}")
            # Continue anyway to see if we can process what we have
        
        # Check if we have any HTML files
        html_files = []
        for root, _, files in os.walk(temp_dir):
            for file in files:
                if file.lower().endswith(('.htm', '.html')):
                    html_files.append(os.path.join(root, file))
        
        if not html_files:
            logger.warning("No HTML files found in extracted content")
            # Try to extract HTML from the CHM file directly
            # This is a fallback method
            with open(chm_path, 'rb') as f:
                content = f.read()
                html_start = content.find(b'<html')
                if html_start > 0:
                    html_end = content.find(b'</html>', html_start)
                    if html_end > 0:
                        html_content = content[html_start:html_end+7]
                        with open(os.path.join(temp_dir, 'index.html'), 'wb') as f:
                            f.write(html_content)
                        logger.info("Extracted HTML content directly from CHM file")
        
        # Copy extracted files to output directory
        copied_files = 0
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                if file.lower().endswith(('.htm', '.html')):
                    src_path = os.path.join(root, file)
                    rel_path = os.path.relpath(src_path, temp_dir)
                    dst_path = os.path.join(output_dir, rel_path)
                    
                    # Create destination directory if it doesn't exist
                    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                    
                    # Copy file
                    shutil.copy2(src_path, dst_path)
                    copied_files += 1
        
        if copied_files > 0:
            logger.info(f"Extracted {copied_files} HTML files to: {output_dir}")
            return True
        else:
            logger.error("Failed to extract any HTML files from CHM")
            return False
        
    except Exception as e:
        logger.error(f"Error extracting CHM: {str(e)}")
        return False
    finally:
        # Clean up temporary directory
        if 'temp_dir' in locals():
            try:
                shutil.rmtree(temp_dir)
            except:
                logger.warning(f"Failed to clean up temporary directory: {temp_dir}")

def convert_html_to_markdown(html_dir, markdown_dir, assets_dir=None):
    """Convert HTML files to Markdown."""
    logger.info(f"Converting HTML files to Markdown")
    
    # Create output directories
    os.makedirs(markdown_dir, exist_ok=True)
    if assets_dir:
        os.makedirs(os.path.join(assets_dir, 'images'), exist_ok=True)
    
    # Track processed files and images
    processed_files = 0
    processed_images = set()
    
    # Find all HTML files
    html_files = []
    for root, _, files in os.walk(html_dir):
        for file in files:
            if file.lower().endswith(('.htm', '.html')):
                html_files.append(os.path.join(root, file))
    
    # Process each HTML file
    for html_file in tqdm(html_files, desc="Converting files"):
        try:
            # Read HTML content
            with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
                html_content = f.read()
            
            # Parse HTML with BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Process images if assets_dir is provided
            if assets_dir:
                for img in soup.find_all('img'):
                    src = img.get('src', '')
                    if not src:
                        continue
                    
                    try:
                        # Resolve relative URLs
                        if not src.startswith(('http://', 'https://', '/')):
                            src_path = os.path.join(os.path.dirname(html_file), src)
                            src_path = os.path.abspath(src_path)
                        else:
                            continue  # Skip external images
                        
                        # Generate Wiki.js compatible path
                        filename = os.path.basename(src)
                        wiki_path = f"/assets/images/{filename}"
                        
                        # Update image src to use Wiki.js path
                        img['src'] = wiki_path
                        
                        # Copy image to assets directory
                        if os.path.exists(src_path):
                            dst_path = os.path.join(assets_dir, 'images', filename)
                            shutil.copy2(src_path, dst_path)
                            processed_images.add(dst_path)
                    
                    except Exception as e:
                        logger.warning(f"Error processing image {src}: {str(e)}")
            
            # Convert to Markdown
            markdown_content = md(str(soup), heading_style="ATX")
            
            # Post-process Markdown
            markdown_content = post_process_markdown(markdown_content)
            
            # Save Markdown file
            rel_path = os.path.relpath(html_file, html_dir)
            markdown_file = os.path.join(markdown_dir, rel_path + '.md')
            os.makedirs(os.path.dirname(markdown_file), exist_ok=True)
            
            with open(markdown_file, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            processed_files += 1
            
        except Exception as e:
            logger.error(f"Error converting {html_file}: {str(e)}")
    
    logger.info(f"Converted {processed_files} HTML files to Markdown")
    logger.info(f"Processed {len(processed_images)} images")
    
    return processed_files

def post_process_markdown(content):
    """Clean up and format the Markdown content for Wiki.js."""
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

def main():
    parser = argparse.ArgumentParser(description='Extract CHM file and convert to Markdown')
    parser.add_argument('--input', '-i', required=True, help='Path to the CHM file')
    parser.add_argument('--output', '-o', required=True, help='Path to the output Markdown directory')
    parser.add_argument('--assets', '-a', action='store_true', help='Extract and process assets (images, etc.)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose logging')
    parser.add_argument('--keep-temp', '-k', action='store_true', help='Keep temporary files')
    
    args = parser.parse_args()
    
    # Set log level
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    start_time = time.time()
    
    # Create temporary directory for extracted HTML
    temp_html_dir = os.path.join(tempfile.gettempdir(), 'chm_extracted_html')
    os.makedirs(temp_html_dir, exist_ok=True)
    
    try:
        # Extract CHM file
        if not extract_chm(args.input, temp_html_dir):
            logger.error("Failed to extract CHM file")
            
            # Create a simple Markdown file with error message
            os.makedirs(args.output, exist_ok=True)
            error_md = os.path.join(args.output, 'extraction_error.md')
            with open(error_md, 'w', encoding='utf-8') as f:
                f.write(f"# CHM Extraction Error\n\n")
                f.write(f"Failed to extract content from: `{args.input}`\n\n")
                f.write("## Possible reasons:\n\n")
                f.write("- The CHM file might be corrupted\n")
                f.write("- The extraction tools (hh.exe or 7-Zip) might not be available\n")
                f.write("- The CHM file might be using a format that's not supported\n\n")
                f.write("## Recommendations:\n\n")
                f.write("1. Try opening the CHM file manually to verify it's not corrupted\n")
                f.write("2. Install 7-Zip for better extraction capabilities\n")
                f.write("3. Try using a dedicated CHM extraction tool\n")
            
            logger.info(f"Created error report at: {error_md}")
            return 1
        
        # Check if we have any HTML files
        html_files = []
        for root, _, files in os.walk(temp_html_dir):
            for file in files:
                if file.lower().endswith(('.htm', '.html')):
                    html_files.append(os.path.join(root, file))
        
        if not html_files:
            logger.error("No HTML files found after extraction")
            
            # Create a simple Markdown file with error message
            os.makedirs(args.output, exist_ok=True)
            error_md = os.path.join(args.output, 'no_html_found.md')
            with open(error_md, 'w', encoding='utf-8') as f:
                f.write(f"# No HTML Content Found\n\n")
                f.write(f"No HTML content could be extracted from: `{args.input}`\n\n")
                f.write("The CHM file might be using a format that's not supported by the extraction tools.\n")
            
            logger.info(f"Created error report at: {error_md}")
            return 1
        
        # Convert HTML to Markdown
        assets_dir = args.output if args.assets else None
        files_converted = convert_html_to_markdown(temp_html_dir, args.output, assets_dir)
        
        if files_converted == 0:
            logger.error("No files were converted to Markdown")
            
            # Create a simple Markdown file with error message
            os.makedirs(args.output, exist_ok=True)
            error_md = os.path.join(args.output, 'conversion_error.md')
            with open(error_md, 'w', encoding='utf-8') as f:
                f.write(f"# Conversion Error\n\n")
                f.write(f"Failed to convert HTML content to Markdown from: `{args.input}`\n\n")
                f.write("The HTML content might be in a format that's not supported by the conversion tools.\n")
            
            logger.info(f"Created error report at: {error_md}")
            return 1
        
        elapsed_time = time.time() - start_time
        logger.info(f"Processing completed in {elapsed_time:.2f} seconds")
        
    finally:
        # Clean up temporary directory
        if not args.keep_temp:
            try:
                shutil.rmtree(temp_html_dir, ignore_errors=True)
                logger.debug(f"Removed temporary directory: {temp_html_dir}")
            except Exception as e:
                logger.warning(f"Failed to clean up temporary directory: {str(e)}")
        else:
            logger.info(f"Temporary files kept at: {temp_html_dir}")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())