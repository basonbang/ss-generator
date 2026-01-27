from textnode import *

def main():
    # Create a new TextNode object with dummy values
    node = TextNode("Hello World", TextType.PLAIN_TEXT)
    node_2 = TextNode("This is some anchor text", TextType.LINK, "https://boot.dev")

    print("TextNode objects created:")
    print(node)
    print(node_2)

if __name__ == "__main__":
    main()