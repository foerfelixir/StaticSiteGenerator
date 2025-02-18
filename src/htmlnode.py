
class HTMLNode:
    def __init__(self,tag:str=None,value:str=None,children:list=None,props:dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        return_result = ""
        for prop_key,prop_value in self.props.items():
            return_result = f'{return_result} {prop_key}="{prop_value}"'
        return return_result[1:]
    
    def __repr__(self):
        return f"HTMLNode(\n\ttag={self.tag},\n\tvalue={self.value},\n\tchildren={self.children},\n\tprops={self.props})"

class LeafNode(HTMLNode):
    def __init__(self,tag:str,value:str,props:dict=None):
        self.tag= tag
        self.value= value
        self.props=props
        super()

    def to_html(self):
        if self.value == None or self.value == "":
            raise ValueError
        html_string = ''
        if self.tag == None or self.tag == "":
            html_string = self.value
        else :
            html_string = f'<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>'       

        return html_string
    
    def __repr__(self):
        return f"LEAFNode(\n\ttag={self.tag},\n\tvalue={self.value},\n\tprops={self.props})"
