import re

def extract_title(markdown):
    h1_header =  re.match(r"^(#{1})\s*(.+)", markdown)
    if h1_header:
        return h1_header.group(2).strip()
    else:
        raise Exception("No h1 header found")
            
        