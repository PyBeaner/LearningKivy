__author__ = 'PyBeaner'

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty,ObjectProperty

class Controller(FloatLayout):
    info = StringProperty()
    label_wid = ObjectProperty()

    def do_action(self):
        self.label_wid.text = "My Label after button press"
        self.info = "New info text"

class ControllerApp(App):
    def build(self):
        return Controller(info="Hello World")

if __name__ == "__main__":
    ControllerApp().run()