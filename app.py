from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget

# Window size here
Window.size = (400, 600)


class Calculator(Widget):
	# erase everything and return 0
	def erase(self):
		self.ids.input.text = '0'

	# clear last element
	def clear(self):
		prior = self.ids.input.text
		if len(prior) > 1:
			self.ids.input.text = prior[:-1]
		else:
			self.ids.input.text = '0'

	def num(self, number):
		# saved whatever is in text field in 'prior'
		prior = self.ids.input.text
		# checking if there is an error already
		if prior == 'Error':
			prior = ''
		# actually function starts here
		if prior == '0':
			self.ids.input.text = ''
			self.ids.input.text = f"{number}"
		else:
			self.ids.input.text = f"{prior}{number}"

	def operation(self, sign):
		prior = self.ids.input.text
		self.ids.input.text = f"{prior}{sign}"

	def put_decimal(self):
		prior = self.ids.input.text

	def equal(self):
		try:
			prior = self.ids.input.text
			answer = eval(prior)
			self.ids.input.text = f"{answer}"
		except:
			self.ids.input.text = 'Error'


class WidgetsApp(App):
	def build(self):
		return Calculator()


WidgetsApp().run()
