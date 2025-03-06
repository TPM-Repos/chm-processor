import os
import subprocess
import sys
from bs4 import BeautifulSoup
import html2text

def find_7zip():
    """Find 7-Zip executable in common installation locations."""
    # Check if 7z is in PATH
    try:
        subprocess.run(['7z', '--help'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        return '7z'
    except FileNotFoundError:
        pass
    
    # Common installation paths for 7-Zip on Windows
    common_paths = [
        r'C:\Program Files\7-Zip\7z.exe',
        r'C:\Program Files (x86)\7-Zip\7z.exe',
    ]
    
    for path in common_paths:
        if os.path.exists(path):
            return path
    
    return None

def extract_chm(chm_file, extract_folder):
    if not os.path.exists(extract_folder):
        os.makedirs(extract_folder)
    
    # Find 7-Zip executable
    seven_zip = find_7zip()
    if not seven_zip:
        print("Error: 7-Zip is required but not found. Please install 7-Zip and ensure it's in your PATH.")
        print("You can download 7-Zip from https://www.7-zip.org/")
        sys.exit(1)
    
    # Run 7-Zip to extract CHM file
    try:
        if seven_zip == '7z':
            subprocess.run(['7z', 'x', chm_file, '-o' + extract_folder], check=True)
        else:
            subprocess.run([seven_zip, 'x', chm_file, '-o' + extract_folder], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error extracting CHM file: {e}")
        sys.exit(1)

def sanitize_filename(filename):
    """Sanitize filename to remove invalid characters for Windows."""
    # Replace invalid characters with underscores
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    
    # Ensure filename is not too long (Windows has a 255 character limit)
    if len(filename) > 240:  # Leave some room for the extension
        filename = filename[:240]
    
    return filename

def process_html_files(extract_folder, partial_folder):
    if not os.path.exists(partial_folder):
        os.makedirs(partial_folder)
    
    # Keep track of processed files to handle duplicates
    processed_titles = {}
    
    for root, _, files in os.walk(extract_folder):
        for file in files:
            if file.endswith('.html'):
                try:
                    html_path = os.path.join(root, file)
                    with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
                        html_content = f.read()
                    
                    soup = BeautifulSoup(html_content, 'html.parser')
                    title = soup.title.string if soup.title else 'No Title'
                    
                    # Sanitize the title for use as a filename
                    safe_title = sanitize_filename(title)
                    
                    # Handle duplicate titles by adding a suffix
                    if safe_title in processed_titles:
                        processed_titles[safe_title] += 1
                        safe_title = f"{safe_title}_{processed_titles[safe_title]}"
                    else:
                        processed_titles[safe_title] = 0
                    
                    # Convert HTML to markdown
                    h = html2text.HTML2Text()
                    h.ignore_links = False
                    h.ignore_images = False
                    h.ignore_tables = False
                    h.body_width = 0  # No wrapping
                    
                    # Get the HTML content of the body if it exists
                    body = soup.body
                    html_content = str(body) if body else html_content
                    
                    # Convert to markdown
                    markdown_content = h.handle(html_content)
                    markdown_file = os.path.join(partial_folder, f"{safe_title}.md")
                    
                    with open(markdown_file, 'w', encoding='utf-8') as f:
                        f.write(markdown_content)
                    
                    print(f"Processed: {file} -> {safe_title}.md")
                except Exception as e:
                    print(f"Error processing {file}: {e}")

def update_crosslinks(partial_folder):
    for root, _, files in os.walk(partial_folder):
        for file in files:
            if file.endswith('.md'):
                markdown_file = os.path.join(root, file)
                with open(markdown_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Update crosslinks
                updated_content = content.replace('.html', '.md')
                
                with open(markdown_file, 'w', encoding='utf-8') as f:
                    f.write(updated_content)

def main(chm_file, extract_folder, partial_folder):
    extract_chm(chm_file, extract_folder)
    process_html_files(extract_folder, partial_folder)
    update_crosslinks(partial_folder)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 4:
        print("Usage: python chm_to_markdown.py <chm_file> <extract_folder> <partial_folder>")
        sys.exit(1)
    
    chm_file = sys.argv[1]
    extract_folder = sys.argv[2]
    partial_folder = sys.argv[3]
    
    main(chm_file, extract_folder, partial_folder)