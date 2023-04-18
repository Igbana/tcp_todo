from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from datetime import datetime
from kivy.properties import ObjectProperty

kv = """
<Entry@MDCard>:
	size_hint_y: None
	height: dp(40)
	radius: dp(10)
	md_bg_color: [0.3,0.3,0.3,0.06]
	padding: dp(10)
	text: text_input.text
	TextInput:
		id: text_input
		hint_text: "Add a todo item"
		size_hint_y: None
		height: self.minimum_height
		background_color: 0,0,0,0
		font_size: sp(16)
		pos_hint: {'center_y': 0.5}
		foreground_color: 1,1,1,1
		multiline: False
		focus: True
		
<Car@Carousel>:
	direction: 'bottom'
	loop: True
	size_hint: None, None
	size: dp(30), dp(40)
	pos_hint: {'center_y': 0.6}
		
<Bottomsheet>:
	orientation: "vertical"
	padding: dp(10), dp(20)
	size_hint_y: None
	height: dp(130)
	spacing: dp(8)
	BoxLayout:
		spacing: dp(8)
		Entry:
			id: task_name
			pos_hint: {'center_y': 0.6}
		MDBoxLayout:
			adaptive_width: True
			Car:
				id: hr_car
			MDLabel:
				text: ":"
				size_hint_x: None
				width: dp(2)
				pos_hint: {'center_y': 0.6}
			Car:
				id: min_car
	AnchorLayout:
		anchor_x: 'right'
		MDRaisedButton:
			text: "Save"
			on_release: print(root.kwargs['on_submit'](task_name.text))
"""

class Bottomsheet(BoxLayout):
	#on_submit = ObjectProperty()
	Builder.load_string(kv)
	def __init__(self, *args, **kwargs):
		super().__init__()
		self.kwargs = kwargs
		for i in range(24):
			self.ids.hr_car.add_widget(
				MDLabel(
					text = str(i) if i > 9 else f"0{i}",
					halign = 'center',
					font_size = "20sp"
				)
			)
		for i in range(60):
			self.ids.min_car.add_widget(
				MDLabel(
				text = str(i) if i > 9 else f"0{i}",
				halign = 'center',
				font_size = "20sp"
			)
		)
		self.ids.hr_car.load_slide(
			self.ids.hr_car.slides[
				datetime.now().hour
			]
		)
		self.ids.min_car.load_slide(
			self.ids.min_car.slides[
				datetime.now().minute
			]
		)
	def submit(self):
		print(self.ids.task_name.text)
		print(self.on_submit())
		#self.on_submit(self.ids.task_name.text)