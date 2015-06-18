from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from random import random


class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(random(), random(), random())
            d = 10.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud["line"] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class MyPaintApp(App):
    def build(self):
        parent = Widget()
        painter = MyPaintWidget()
        parent.add_widget(painter)
        button = Button(text="Clear")
        parent.add_widget(button)

        def clear_paint(obj):
            print(obj)  # the button object
            painter.canvas.clear()

        button.bind(on_release=clear_paint)
        return parent


if __name__ == '__main__':
    MyPaintApp().run()
