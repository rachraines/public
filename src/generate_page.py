import os
from markdown_to_html import markdown_to_html, LeafNode, ParentNode
from extract_title import extract_title
from htmlnode import HTMLNode

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

