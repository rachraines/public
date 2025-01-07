import re

def extract_title(markdown):
    # Match only lines that start with exactly one `#` followed by space
    h1_header = re.match(r"^#(?!#)\s*(.+)", markdown)
    
    # If the match is successful, return the matched group (title), stripped of leading/trailing spaces
    if h1_header:
        return h1_header.group(1).strip()
    else:
        raise Exception("No h1 header found")
