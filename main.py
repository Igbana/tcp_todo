from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.metrics import dp
from kivymd.uix.screen import MDScreen
from components.entrybox import EntryBox
from components.taskcard import TaskCard
from components.bottomsheet import Bottomsheet
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from test.data import demo_tasks

Window.softinput_mode ='pan'

class HomePage(MDScreen):
	def on_enter(self):
		for taskName in demo_tasks:
			wid = TaskCard(task = taskName)
			self.ids.task_lst.add_widget(wid, len(self.ids.task_lst.children))
			wid.on_checked = lambda: self.checked(wid)
		
	def popup(self):
		self.bottomSheet = MDCustomBottomSheet(
			screen = Bottomsheet(on_submit = self.add),
			duration_opening = 0.1,
			radius_from = 'top',
			radius = dp(10),
			animation = True
		)
		self.bottomSheet.open()
		
	def add(self, taskName):
		wid = TaskCard(task = taskName)
		self.ids.task_lst.add_widget(wid, len(self.ids.task_lst.children))
		wid.on_checked = lambda: self.checked(wid)
		self.bottomSheet.dismiss()

	def checked(self, wid):
		if wid.is_done():
			self.ids.task_lst.children.insert(
				0, 
				self.ids.task_lst.children.pop(
					self.ids.task_lst.children.index(wid)
				)
			)
		else:
			self.ids.task_lst.children.insert(
				self.ids.task_lst.children.index(self.ids.completed_lbl), 
				self.ids.task_lst.children.pop(
					self.ids.task_lst.children.index(wid)
				)
			)

class MainApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = 'Dark'
		self.theme_cls.primary_palette = 'DeepPurple'
		return HomePage()
	
MainApp().run()