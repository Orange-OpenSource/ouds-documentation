#!/usr/bin/env python3
"""
Image Markdown Generator Script
Automatically creates markdown files for new images in component images/ directories
Each markdown file contains an image reference: ![image_name](./image_name.ext)
"""

import os
import re
from pathlib import Path
from typing import List, Set

# Supported image extensions
IMAGE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp'}


def get_image_name_without_extension(filename: str) -> str:
    """
    Get the image filename without its extension
    
    Args:
        filename: Image filename (e.g., "my_image.png")
        
    Returns:
        Filename without extension (e.g., "my_image")
    """
    return Path(filename).stem


def generate_markdown_content(image_filename: str) -> str:
    """
    Generate markdown content for an image file
    
    Args:
        image_filename: Name of the image file (e.g., "screenshot.png")
        
    Returns:
        Markdown content with image reference
    """
    image_name = get_image_name_without_extension(image_filename)
    return f"![{image_name}](./{image_filename})\n"


def should_create_markdown(image_path: Path) -> bool:
    """
    Check if a markdown file should be created for this image
    
    Args:
        image_path: Path to the image file
        
    Returns:
        True if markdown file should be created, False otherwise
    """
    # Get the corresponding markdown file path
    md_filename = get_image_name_without_extension(image_path.name) + '.md'
    md_path = image_path.parent / md_filename
    
    # Only create if markdown file doesn't already exist
    return not md_path.exists()


def process_image_file(image_path: Path) -> bool:
    """
    Process a single image file and create its markdown file
    
    Args:
        image_path: Path to the image file
        
    Returns:
        True if markdown was created, False otherwise
    """
    # Validate it's an image file
    if image_path.suffix.lower() not in IMAGE_EXTENSIONS:
        print(f"  ⚠ Skipping: {image_path.name} - not a supported image format")
        return False
    
    # Check if we should create markdown
    if not should_create_markdown(image_path):
        print(f"  ⏭ Skipping: {image_path.name} - markdown file already exists")
        return False
    
    # Generate markdown content
    md_content = generate_markdown_content(image_path.name)
    
    # Create markdown file in the same directory as the image
    md_filename = get_image_name_without_extension(image_path.name) + '.md'
    md_path = image_path.parent / md_filename
    
    try:
        md_path.write_text(md_content, encoding='utf-8')
        print(f"  ✓ Created: {md_path}")
        return True
    except Exception as e:
        print(f"  ❌ Error creating {md_path}: {e}")
        return False


def validate_image_path(file_path: Path) -> bool:
    """
    Validate that the file path is in a valid component images/ directory
    
    Expected formats:
    - components/[type]/[name]/images/[image]
    - components/[type]/[group]/[name]/images/[image]
    
    Args:
        file_path: Path to validate
        
    Returns:
        True if valid, False otherwise
    """
    parts = file_path.parts
    
    # Must start with 'components' and contain 'images' directory
    if len(parts) < 5 or parts[0] != 'components':
        return False
    
    # 'images' should be the second-to-last part (parent directory of the image)
    if parts[-2] != 'images':
        return False
    
    return True


def main():
    """
    Main entry point
    Reads list of changed image files and processes each one
    """
    print("🖼️ Starting image markdown generator...\n")
    
    # Read the list of changed image files (created by GitHub Actions)
    changed_files_path = Path('changed_images.txt')
    
    if not changed_files_path.exists():
        print("No changed images file detected")
        return
    
    changed_files_content = changed_files_path.read_text(encoding='utf-8')
    changed_files = [f.strip() for f in changed_files_content.split('\n') if f.strip()]
    
    if not changed_files:
        print("No image files to process")
        return
    
    print(f"Found {len(changed_files)} image file(s) to process\n")
    
    created_count = 0
    skipped_count = 0
    error_count = 0
    
    # Process each changed file
    for file_str in changed_files:
        try:
            file_path = Path(file_str)
            print(f"Processing: {file_path}")
            
            # Validate path format
            if not validate_image_path(file_path):
                print(f"  ⚠ Skipping: Invalid path format")
                skipped_count += 1
                continue
            
            # Check if file exists
            if not file_path.exists():
                print(f"  ⚠ Skipping: File not found")
                skipped_count += 1
                continue
            
            # Process the image
            if process_image_file(file_path):
                created_count += 1
            else:
                skipped_count += 1
                
        except Exception as e:
            print(f"  ❌ Error processing {file_str}: {e}")
            error_count += 1
            # Print full stack trace for debugging
            import traceback
            traceback.print_exc()
    
    # Print summary
    print(f"\n{'='*50}")
    print(f"📊 Summary:")
    print(f"   ✓ Created: {created_count} markdown file(s)")
    print(f"   ⏭ Skipped: {skipped_count} file(s)")
    if error_count > 0:
        print(f"   ❌ Errors: {error_count} file(s)")
    print(f"{'='*50}")
    print("\n✅ Image markdown generation completed!")


if __name__ == "__main__":
    main()