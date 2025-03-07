import os
import re

def remove_image_references(directory):
    # Define all patterns to remove/replace
    patterns = [
        # Simple image references
        (r'!\[\]\(dotnetimages/\w+\.gif\)\s*', ''),
        # Copyright text
        (r'©2024 DriveWorks Ltd\. All Rights Reserved\.', ''),
        # Feedback line
        (r'See Also \[Send Feedback\]\(mailto:apisupport@driveworks\.co\.uk\?subject=Documentation Feedback: topic\d+\.md\)\n*', ''),
        # Members options and Language filter lines with possible images
        (r'!\[\]\(dotnetimages/\w+\.gif\)\s*Collapse All Expand All\s*!\[\]\(dotnetimages/\w+\.gif\)\s*(?:Members Options: Show All  Members Options: Filtered|Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic \(Declaration\) Language Filter: Visual Basic \(Usage\) Language Filter: C#)\s*', ''),
        # DriveWorks header with flexible whitespace
        (r'^\s*\n\s*\n.*?\n---  \n\s*DriveWorks SDK Documentation  \|   \n---\|---  \n', '', re.DOTALL),
        # Method images
        (r'!\[(Public|Protected) Method\]\(dotnetimages/\w+Method\.gif\)', r'\1 Method'),
        # Copy Code references
        (r'!\[\]\(dotnetimages/copycode\.gif\)Copy Code', ''),
        # Collapse/Expand headers
        (r'# !\[\]\(dotnetimages/collapse\.gif\)', '#'),
    ]
    
    # Get absolute path of directory
    abs_directory = os.path.abspath(directory)
    print(f"Processing directory: {abs_directory}")
    
    # Count files for tracking
    total_files = 0
    processed_files = 0
    
    # Walk through all files in the directory
    for root, _, files in os.walk(abs_directory):
        md_files = [f for f in files if f.lower().endswith('.md')]
        total_files += len(md_files)
        
        for file in md_files:
            filepath = os.path.join(root, file)
            print(f"Processing file: {filepath}")
            
            # Read file content
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Apply all patterns
                new_content = content
                for pattern, replacement, *flags in patterns:
                    if flags:
                        new_content = re.sub(pattern, replacement, new_content, flags=flags[0])
                    else:
                        new_content = re.sub(pattern, replacement, new_content)
                
                # Only write if content changed
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated file: {filepath}")
                    processed_files += 1
                
            except Exception as e:
                print(f"Error processing {filepath}: {str(e)}")
    
    print(f"\nProcessing complete:")
    print(f"Total MD files found: {total_files}")
    print(f"Files updated: {processed_files}")

if __name__ == '__main__':
    remove_image_references('markdown_output')