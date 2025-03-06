import os
import re

def remove_image_references(directory):
    # Pattern to match the copyright string
    pattern = r'©2024 DriveWorks Ltd\. All Rights Reserved\.'
    
    # Walk through all files in the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                
                # Read file content
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Remove the pattern and ensure newlines are preserved
                    new_content = re.sub(pattern, '', content)
                    
                    # Only write if content changed
                    if new_content != content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        
                except Exception as e:
                    print(f"Error processing {filepath}: {str(e)}")

if __name__ == '__main__':
    remove_image_references('markdown_output')