from kivymd.uix.card import MDCard
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty

kv = """
<TaskCard>:
	checkbox: checkbox
	size_hint_y: None
	height: dp(65)
	radius: dp(10)
	md_bg_color: [0.5,0.5,0.5,0.2]
	spacing: dp(8)
	MDCheckbox:
		id: checkbox
		checkbox_icon_normal: 'checkbox-blank-circle-outline'
		checkbox_icon_down: 'check-circle'
		ripple_scale: 0
		size_hint: None, None
		size: dp(38), dp(38)
		pos_hint: {'center_y': 0.5}
		on_active:
			task_lbl.text = f"[s]{root.task}[/s]" if checkbox.active else root.task
			root.on_checked()
	MDLabel:
		id: task_lbl
		markup: True
		text: root.task
"""

class TaskCard(MDCard):
	Builder.load_string(kv)
	on_checked = ObjectProperty()
	task = StringProperty()
	def is_done(self):
		return self.ids.checkbox.active