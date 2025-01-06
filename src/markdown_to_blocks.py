from textnode import TextNode, TextType

def markdown_to_blocks(markdown):
    blocks = []
    # strip leading/trailing whitespace for the entire string
    markdown = markdown.strip()

    # split by 2 or more consecutive new lines
    for p in markdown.split("\n\n"):
        # strip each block again
        block = p.strip()
        if block:
            # strip each line in the block, then join them back together
            block_lines = "\n".join([line.strip() for line in block.split("\n")])
            blocks.append(block_lines)
    
    return blocks