import os
from markdown_to_html import markdown_to_html, LeafNode, ParentNode
from extract_title import extract_title
from htmlnode import HTMLNode
from pathlib import Path

def generate_page(from_path, template_path, dest_path):
    # Step 1: Print the message
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Step 2: Read the markdown file at from_path
    try:
        with open(from_path, 'r') as markdown_file:
            markdown_content = markdown_file.read()
    except FileNotFoundError:
        print(f"Error: Markdown file at {from_path} not found.")
        return

    # Step 3: Read the template file at template_path
    try:
        with open(template_path, 'r') as template_file:
            template_content = template_file.read()
    except FileNotFoundError:
        print(f"Error: Template file at {template_path} not found.")
        return

    # Step 4: Use the markdown_to_html function to convert markdown to HTML
    html_node = markdown_to_html(markdown_content)
    print(f"Generated node: {html_node}")
    print(f"Node type: {type(html_node)}")

    if isinstance(html_node, HTMLNode) and type(html_node) == HTMLNode:
        raise TypeError("html_node must be an instance of a subclass of HTMLNode")

    html_content = html_node.to_html()

    # Step 5: Extract the title from the markdown content using extract_title function
    try:
        title = extract_title(markdown_content)
    except Exception as e:
        print(f"Error: {str(e)}")
        return

    # Step 6: Replace {{ Title }} and {{ Content }} in the template
    page_content = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    # Step 7: Ensure the destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Step 8: Write the new HTML content to a file at dest_path
    with open(dest_path, 'w') as output_file:
        output_file.write(page_content)
    
    print(f"Page successfully generated and saved to {dest_path}")

def generate_page_recursive(dir_path_content, template_path, set_dir_path):
    # Convert paths to Path objects and resolve absolute paths
    dir_path_content = Path(dir_path_content).resolve()
    dest_dir_path = Path(dest_dir_path).resolve()

    # Create the destination directory if it doesn't exist
    dest_dir_path.mkdir(parents=True, exist_ok=True)

    # Traverse the content directory recursively
    for root, dirs, files in os.walk(dir_path_content):
        # Compute the relative path from the content directory to the current root
        rel_path = Path(root).relative_to(dir_path_content)
        # Define the corresponding destination directory in the public directory
        dest_path = dest_dir_path / rel_path

        # Ensure the destination directory exists
        dest_path.mkdir(parents=True, exist_ok=True)

        for file in files:
            # Process only markdown files
            if file.endswith(".md"):
                # Determine input markdown path and output HTML path
                markdown_file_path = Path(root) / file
                html_file_name = markdown_file_path.stem + ".html"  # Replace .md with .html
                html_output_path = dest_path / html_file_name

                # Generate HTML file using the template
                print(f"Generating: {markdown_file_path} -> {html_output_path}")
                generate_page(markdown_file_path, template_path, html_output_path)
            else:
                # Log skipped non-markdown files
                print(f"Skipping non-markdown file: {Path(root) / file}")