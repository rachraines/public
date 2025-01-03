import re

def extract_markdown_images(text):
    # finds all text inside of []
    alt_text = re.findall(r"!\[(.*?)\]", text)
    # print(f"alt text: {alt_text}")
    # finds all text inside of ()
    image = re.findall(r"\((.*?)\)", text)
    # print(f"image: {image}")
    # print(list(zip(alt_text, image)))
    return list(zip(alt_text, image))