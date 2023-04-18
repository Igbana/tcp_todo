from kivymd.uix.card import MDCard
from kivy.lang import Builder

kv = """
<EntryBox>:
	size_hint_y: None
	height: dp(50)
	radius: dp(10)
	md_bg_color: [0.3,0.3,0.3,0.06]
	MDIconButton:
		id: ico
		icon: 'magnify'
	TextInput:
		size_hint_y: None
		height: self.minimum_height
		background_color: 0,0,0,0
		font_size: sp(16)
		pos_hint: {'center_y': 0.5}
		foreground_color: 1,1,1,1
"""

class EntryBox(MDCard):
	Builder.load_string(kv)