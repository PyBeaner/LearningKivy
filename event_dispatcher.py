__author__ = 'PyBeaner'

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty


class CustomBtn(Widget):
    # define a property
    pressed = ListProperty([0,0])

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            # property changed,event dispatched to children
            self.pressed = touch.pos
            # we consumed the touch. return False here to propagate
            # the touch further to the children.
            return True
        return super(CustomBtn,self).on_touch_down(touch)

    # event on_<some_property>
    def on_pressed(self,instance,pos):
        print("pressed at {pos}".format(pos=pos))


class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Button(text="btn 1"))
        cb = CustomBtn()
        cb.bind(pressed=self.btn_pressed)
        self.add_widget(cb)
        self.add_widget(Button(text="btn 2"))

    def btn_pressed(self,instance,pos):
        print("pos:printed from root widget:{pos}".format(pos=pos))


class  MyApp(App):
    def build(self):
        return RootWidget()


if __name__=="__main__":
    MyApp().run()