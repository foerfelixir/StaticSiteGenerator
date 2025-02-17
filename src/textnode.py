from enum import Enum

class TextType(Enum):
	NORMAL_TEXT = "Normal"
	BOLD_TEXT = "Bold"
	ITALIC_TEXT = "Italic"
	CODE_TEXT = "Code"
	LINKS_TEXT = "Links"
	IMAGES_TEXT = "Images"

class TextNode:
	def __init__(self,text,text_type,url=None):
		self.text = text
		self.text_type = text_type
		self.url = url
	
	def __eq__(self,target):
		if isinstance(target, TextNode) and self.text == target.text and self.url == target.url:
			return True
		return False

	def __repr__(self):
		return f"TextNode({self.text},{self.text_type.value},{self.url})"