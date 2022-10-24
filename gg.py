from kivy.app import App
from kivy.uix.button import Button
class HelloApp(App):
    def build(self):
        return Button(text='Hello Berlin')
HelloApp().run()

% buildozer android debug deploy run