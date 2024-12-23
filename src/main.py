from textnode import TextNode, TextType

def main():
    # create a new TextNode object with sample values
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

main()