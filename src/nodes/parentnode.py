from nodes import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict=None):
        super().__init__(tag, None, children, props)
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode tag cannot be None")
        if type(self.children) is not list:
            raise ValueError("ParentNode children must be a list of HTMLNodes")
        if self.children is None:
            raise ValueError("ParentNode children cannot be None")
        
        content = ""
        if len(self.children) > 0:
            for c in self.children:
                content += c.to_html()

        return f'<{self.tag}{self.props_to_html()}>{content}</{self.tag}>'

    def __repr__(self):
        return f'ParentNode({self.tag}, {self.children}, {self.props})'