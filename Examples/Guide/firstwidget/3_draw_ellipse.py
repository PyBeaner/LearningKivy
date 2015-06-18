__author__ = 'PyBeaner'

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse


class MyPaintWidget(Widget):
    touch_point_color = (1, 1, 0)
    touch_point_radius = 10.0
    previous_touch_point = None

    def on_touch_down(self, touch):
        with self.canvas:
            Color(*self.touch_point_color)  #
            Ellipse(pos=(touch.x - self.touch_point_radius, touch.y - self.touch_point_radius),
                    size=(self.touch_point_radius * 2, self.touch_point_radius * 2))
            self.previous_touch_point = touch.pos

    def on_touch_up(self, touch):
        with self.canvas:
            if self.previous_touch_point:
                Color(0, 0, 0)  #
                Ellipse(pos=(self.previous_touch_point[0] - self.touch_point_radius,
                             self.previous_touch_point[1] - self.touch_point_radius),
                        size=(self.touch_point_radius * 2, self.touch_point_radius * 2))


class MyPaintApp(App):
    def build(self):
        return MyPaintWidget()


if __name__ == "__main__":
    MyPaintApp().run()
