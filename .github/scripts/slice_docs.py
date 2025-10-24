#!/usr/bin/env python3
"""
Documentation Slicer Script
Automatically slices Markdown documents by heading hierarchy and saves to dsm/ directory
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Dict, Optional


class MarkdownSection:
    """
    Represents a section in a Markdown document
    
    Attributes:
        level: Heading level (1 for H1, 2 for H2, etc.)
        title: The heading text
        line_number: Line number where this heading appears
        markdown: The original markdown heading line
        content: Full content of this section
        children: Child sections (sub-headings)
        path: File path segments for this section
    """
    
    def __init__(self, level: int, title: str, line_number: int, markdown: str):
        self.level = level
        self.title = title
        self.line_number = line_number
        self.markdown = markdown
        self.content = markdown
        self.children = []
        self.path = []
    
    def __repr__(self):
        return f"Section(level={self.level}, title='{self.title}')"


def parse_markdown(content: str) -> List[MarkdownSection]:
    """
    Parse a Markdown file and extract heading hierarchy
    
    Args:
        content: Markdown file content as string
        
    Returns:
        List of MarkdownSection objects representing all headings found
    """
    lines = content.split('\n')
    sections = []
    current_section = None
    current_content = []
    
    for i, line in enumerate(lines):
        # Match headings: # Title, ## Title, ### Title, etc.
        heading_match = re.match(r'^(#{1,6})\s+(.+)$', line)
        
        if heading_match:
            # Save the previous section if it exists
            if current_section:
                current_section.content = '\n'.join(current_content)
                sections.append(current_section)
            
            # Start a new section
            level = len(heading_match.group(1))  # Count the # symbols
            title = heading_match.group(2).strip()
            
            current_section = MarkdownSection(
                level=level,
                title=title,
                line_number=i,
                markdown=line
            )
            current_content = [line]
        elif current_section:
            # Accumulate content lines for the current section
            current_content.append(line)
    
    # Save the last section
    if current_section:
        current_section.content = '\n'.join(current_content)
        sections.append(current_section)
    
    return sections


def build_hierarchy(flat_sections: List[MarkdownSection]) -> List[MarkdownSection]:
    """
    Build a hierarchical tree structure from flat list of sections
    
    Args:
        flat_sections: Flat list of MarkdownSection objects
        
    Returns:
        List of root-level sections (each may have children)
    """
    # Create a virtual root node to hold top-level sections
    root = MarkdownSection(level=0, title='root', line_number=-1, markdown='')
    stack = [root]
    
    for section in flat_sections:
        # Find the parent node by popping from stack until we find 
        # a node with level less than current section
        while len(stack) > 1 and stack[-1].level >= section.level:
            stack.pop()
        
        parent = stack[-1]
        # Build the file path by appending sanitized title to parent's path
        section.path = parent.path + [sanitize_filename(section.title)]
        parent.children.append(section)
        stack.append(section)
    
    return root.children


def sanitize_filename(name: str) -> str:
    """
    Clean filename by replacing special characters
    Converts "Basic Usage" to "basic_usage"
    
    Args:
        name: Original heading text
        
    Returns:
        Sanitized filename safe for file systems
    """
    # Convert to lowercase
    name = name.lower()
    # Replace spaces with underscores
    name = re.sub(r'\s+', '_', name)
    # Remove special characters, keep only alphanumeric, underscore, and hyphen
    name = re.sub(r'[^a-z0-9_-]', '', name)
    # Merge multiple consecutive underscores into one
    name = re.sub(r'_+', '_', name)
    # Strip leading/trailing underscores
    name = name.strip('_')
    
    return name


def extract_section_content(content: str, sections: List[MarkdownSection], 
                           section_index: int) -> str:
    """
    Extract the full content of a section (until the next same-level or higher heading)
    
    Args:
        content: Complete Markdown content
        sections: List of all sections
        section_index: Index of the current section
        
    Returns:
        Complete content string for this section
    """
    section = sections[section_index]
    start_line = section.line_number
    
    # Find the next heading at same level or higher
    lines = content.split('\n')
    end_line = len(lines)  # Default to end of file
    
    for i in range(section_index + 1, len(sections)):
        if sections[i].level <= section.level:
            end_line = sections[i].line_number
            break
    
    section_content = '\n'.join(lines[start_line:end_line]).strip()
    
    # Remove trailing horizontal rule (---) if present
    # Check for various markdown horizontal rule formats at the end
    section_lines = section_content.split('\n')
    while section_lines:
        last_line = section_lines[-1].strip()
        # Check if last line is a horizontal rule: ---, ***, ___, or variations
        if re.match(r'^[-*_]{3,}


def collect_leaf_sections(section: MarkdownSection, 
                         leaf_sections: Optional[List[MarkdownSection]] = None) -> List[MarkdownSection]:
    """
    Recursively collect only leaf sections (sections without children)
    
    Args:
        section: Current section node
        leaf_sections: Accumulator list for collecting leaf sections
        
    Returns:
        Flattened list of leaf sections only
    """
    if leaf_sections is None:
        leaf_sections = []
    
    # Skip virtual root
    if section.title == 'root':
        for child in section.children:
            collect_leaf_sections(child, leaf_sections)
    # If this section has no children, it's a leaf node
    elif not section.children:
        leaf_sections.append(section)
    # If this section has children, recursively process them
    else:
        for child in section.children:
            collect_leaf_sections(child, leaf_sections)
    
    return leaf_sections


def collect_all_sections(section: MarkdownSection, 
                        all_sections: Optional[List[MarkdownSection]] = None) -> List[MarkdownSection]:
    """
    Recursively collect all sections (including parent sections with children)
    
    Args:
        section: Current section node
        all_sections: Accumulator list for collecting sections
        
    Returns:
        Flattened list of all sections in the tree
    """
    if all_sections is None:
        all_sections = []
    
    # Add current section (skip virtual root)
    if section.title != 'root':
        all_sections.append(section)
    
    # Recursively add all children
    for child in section.children:
        collect_all_sections(child, all_sections)
    
    return all_sections


def save_slice(component_dir: Path, path_segments: List[str], 
              filename: str, content: str) -> None:
    """
    Save a slice file to the dsm/ directory
    
    Args:
        component_dir: Component directory path
        path_segments: List of path segments (e.g., ['h1_title', 'h2_title'])
        filename: Name of the output file (without .md extension)
        content: File content to write
    """
    dsm_dir = component_dir / 'dsm'
    
    # Build target directory (excluding last segment which is the filename)
    if len(path_segments) > 1:
        target_dir = dsm_dir / Path(*path_segments[:-1])
    else:
        target_dir = dsm_dir
    
    # Create directories if they don't exist
    target_dir.mkdir(parents=True, exist_ok=True)
    
    # Write the slice file
    file_path = target_dir / f"{filename}.md"
    file_path.write_text(content, encoding='utf-8')
    
    # Print relative path for logging
    relative_path = file_path.relative_to(component_dir)
    print(f"  ✓ Created slice: {relative_path}")


def clean_dsm_directory(component_dir: Path) -> None:
    """
    Remove the entire dsm/ directory to start fresh
    
    Args:
        component_dir: Component directory path
    """
    dsm_dir = component_dir / 'dsm'
    if dsm_dir.exists():
        import shutil
        shutil.rmtree(dsm_dir)


def process_component_doc(file_path: Path) -> None:
    """
    Process a single component documentation file
    Validates path format, parses markdown, and generates slices
    
    Args:
        file_path: Path to the component markdown file
    """
    print(f"\nProcessing: {file_path}")
    
    # Validate file path format: components/[control_type]/[control_name]/[control_name].md
    parts = file_path.parts
    
    if len(parts) < 4 or parts[0] != 'components':
        print(f"  ⚠ Skipping: Invalid path format")
        return
    
    control_type = parts[1]  # e.g., "control"
    control_name = parts[2]  # e.g., "text_input"
    file_name = parts[3]     # e.g., "text_input.md"
    
    # Verify filename matches control name
    expected_filename = f"{control_name}.md"
    if file_name != expected_filename:
        print(f"  ⚠ Skipping: Expected {expected_filename}, got {file_name}")
        return
    
    component_dir = file_path.parent
    
    # Read file content
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"  ❌ Error reading file: {e}")
        return
    
    # Parse markdown structure
    flat_sections = parse_markdown(content)
    
    if not flat_sections:
        print(f"  ⚠ No headings found in document")
        return
    
    # Build hierarchy tree
    hierarchy = build_hierarchy(flat_sections)
    
    # Clean old slices
    clean_dsm_directory(component_dir)
    
    # Collect only leaf sections (sections without children)
    leaf_sections = []
    for root_section in hierarchy:
        collect_leaf_sections(root_section, leaf_sections)
    
    print(f"  Found {len(leaf_sections)} leaf sections to slice")
    print(f"  Control Type: {control_type}, Control Name: {control_name}")
    
    # Create a slice file only for leaf sections
    for section in leaf_sections:
        # Find this section's index in the flat list
        section_index = None
        for i, flat_section in enumerate(flat_sections):
            if (flat_section.title == section.title and 
                flat_section.level == section.level):
                section_index = i
                break
        
        if section_index is not None:
            # Extract full content for this section
            section_content = extract_section_content(content, flat_sections, section_index)
            filename = sanitize_filename(section.title)
            save_slice(component_dir, section.path, filename, section_content)
    
    print(f"  ✓ Completed slicing")


def main():
    """
    Main entry point
    Reads list of changed files and processes each one
    """
    print("🔪 Starting documentation slicer...\n")
    
    # Read the list of changed files (created by GitHub Actions)
    changed_files_path = Path('changed_files.txt')
    
    if not changed_files_path.exists():
        print("No changed files detected")
        return
    
    changed_files_content = changed_files_path.read_text(encoding='utf-8')
    changed_files = [f.strip() for f in changed_files_content.split('\n') if f.strip()]
    
    if not changed_files:
        print("No markdown files to process")
        return
    
    print(f"Found {len(changed_files)} file(s) to process")
    
    # Process each changed file
    for file_str in changed_files:
        try:
            file_path = Path(file_str)
            if file_path.exists():
                process_component_doc(file_path)
            else:
                print(f"\n⚠ File not found: {file_path}")
        except Exception as e:
            print(f"\n❌ Error processing {file_str}: {e}")
            # Print full stack trace for debugging
            import traceback
            traceback.print_exc()
    
    print("\n✅ Documentation slicing completed!")


if __name__ == "__main__":
    main()
, last_line):
            section_lines.pop()
        else:
            break
    
    return '\n'.join(section_lines).rstrip()


def collect_all_sections(section: MarkdownSection, 
                        all_sections: Optional[List[MarkdownSection]] = None) -> List[MarkdownSection]:
    """
    Recursively collect all sections (including parent sections with children)
    
    Args:
        section: Current section node
        all_sections: Accumulator list for collecting sections
        
    Returns:
        Flattened list of all sections in the tree
    """
    if all_sections is None:
        all_sections = []
    
    # Add current section (skip virtual root)
    if section.title != 'root':
        all_sections.append(section)
    
    # Recursively add all children
    for child in section.children:
        collect_all_sections(child, all_sections)
    
    return all_sections


def save_slice(component_dir: Path, path_segments: List[str], 
              filename: str, content: str) -> None:
    """
    Save a slice file to the dsm/ directory
    
    Args:
        component_dir: Component directory path
        path_segments: List of path segments (e.g., ['h1_title', 'h2_title'])
        filename: Name of the output file (without .md extension)
        content: File content to write
    """
    dsm_dir = component_dir / 'dsm'
    
    # Build target directory (excluding last segment which is the filename)
    if len(path_segments) > 1:
        target_dir = dsm_dir / Path(*path_segments[:-1])
    else:
        target_dir = dsm_dir
    
    # Create directories if they don't exist
    target_dir.mkdir(parents=True, exist_ok=True)
    
    # Write the slice file
    file_path = target_dir / f"{filename}.md"
    file_path.write_text(content, encoding='utf-8')
    
    # Print relative path for logging
    relative_path = file_path.relative_to(component_dir)
    print(f"  ✓ Created slice: {relative_path}")


def clean_dsm_directory(component_dir: Path) -> None:
    """
    Remove the entire dsm/ directory to start fresh
    
    Args:
        component_dir: Component directory path
    """
    dsm_dir = component_dir / 'dsm'
    if dsm_dir.exists():
        import shutil
        shutil.rmtree(dsm_dir)


def process_component_doc(file_path: Path) -> None:
    """
    Process a single component documentation file
    Validates path format, parses markdown, and generates slices
    
    Args:
        file_path: Path to the component markdown file
    """
    print(f"\nProcessing: {file_path}")
    
    # Validate file path format: components/[control_type]/[control_name]/[control_name].md
    parts = file_path.parts
    
    if len(parts) < 4 or parts[0] != 'components':
        print(f"  ⚠ Skipping: Invalid path format")
        return
    
    control_type = parts[1]  # e.g., "control"
    control_name = parts[2]  # e.g., "text_input"
    file_name = parts[3]     # e.g., "text_input.md"
    
    # Verify filename matches control name
    expected_filename = f"{control_name}.md"
    if file_name != expected_filename:
        print(f"  ⚠ Skipping: Expected {expected_filename}, got {file_name}")
        return
    
    component_dir = file_path.parent
    
    # Read file content
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"  ❌ Error reading file: {e}")
        return
    
    # Parse markdown structure
    flat_sections = parse_markdown(content)
    
    if not flat_sections:
        print(f"  ⚠ No headings found in document")
        return
    
    # Build hierarchy tree
    hierarchy = build_hierarchy(flat_sections)
    
    # Clean old slices
    clean_dsm_directory(component_dir)
    
    # Collect all sections (both parent and leaf nodes)
    all_sections = []
    for root_section in hierarchy:
        collect_all_sections(root_section, all_sections)
    
    print(f"  Found {len(all_sections)} sections to slice")
    print(f"  Control Type: {control_type}, Control Name: {control_name}")
    
    # Create a slice file for each section
    for section in all_sections:
        # Find this section's index in the flat list
        section_index = None
        for i, flat_section in enumerate(flat_sections):
            if (flat_section.title == section.title and 
                flat_section.level == section.level):
                section_index = i
                break
        
        if section_index is not None:
            # Extract full content for this section
            section_content = extract_section_content(content, flat_sections, section_index)
            filename = sanitize_filename(section.title)
            save_slice(component_dir, section.path, filename, section_content)
    
    print(f"  ✓ Completed slicing")


def main():
    """
    Main entry point
    Reads list of changed files and processes each one
    """
    print("🔪 Starting documentation slicer...\n")
    
    # Read the list of changed files (created by GitHub Actions)
    changed_files_path = Path('changed_files.txt')
    
    if not changed_files_path.exists():
        print("No changed files detected")
        return
    
    changed_files_content = changed_files_path.read_text(encoding='utf-8')
    changed_files = [f.strip() for f in changed_files_content.split('\n') if f.strip()]
    
    if not changed_files:
        print("No markdown files to process")
        return
    
    print(f"Found {len(changed_files)} file(s) to process")
    
    # Process each changed file
    for file_str in changed_files:
        try:
            file_path = Path(file_str)
            if file_path.exists():
                process_component_doc(file_path)
            else:
                print(f"\n⚠ File not found: {file_path}")
        except Exception as e:
            print(f"\n❌ Error processing {file_str}: {e}")
            # Print full stack trace for debugging
            import traceback
            traceback.print_exc()
    
    print("\n✅ Documentation slicing completed!")


if __name__ == "__main__":
    main()