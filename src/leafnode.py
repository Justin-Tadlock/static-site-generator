from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value: str, tag=None, props=None):
        super().__init__(tag, value, None, props)
        self.tag = tag
        self.value = value

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode value cannot be None")
        if self.tag is None:
            return self.value
        if self.props is not None:
            attributes = self.props_to_html()
            return f'<{self.tag}{attributes}>{self.value}</{self.tag}>'
        return f'<{self.tag}>{self.value}</{self.tag}>'