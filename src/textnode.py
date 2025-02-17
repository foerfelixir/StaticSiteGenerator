from enum import Enum

class TextType(Enum):
	NORMAL = "Normal"
	BOLD = "Bold"
	ITALIC = "Italic"
	CODE = "Code"
	LINKS = "Links"
	IMAGES = "Images"

class TextNode:
	def __init__(self,text,text_type,url=None):
		self.text = text
		self.text_type = text_type
		self.url = url
	
	def __eq__(self,target):
		if isinstance(target, TextNode)and self.text_type == target.text_type and self.text == target.text and self.url == target.url:
			return True
		return False

	def __repr__(self):
		return f"TextNode({self.text},{self.text_type.value},{self.url})"