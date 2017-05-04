from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from page1 import Page1
from page2 import Page2

class ExampleScreensApp(App):
    def build(self):
        screenManager = ScreenManager()
        screenManager.add_widget(Page1(name='page1'))
        screenManager.add_widget(Page2(name='page2'))
        return screenManager

if __name__ == '__main__':
    ExampleScreensApp().run()