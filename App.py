from kivymd.app import MDApp
from kivy.lang import Builder


kv = """
FloatLayout:
    MDRaisedButton:
        text: 'Clica em mim'
        # size_hint_x: .5 
        size_hint_y: .12 
        pos_hint: {'center_x':.5}
    

"""

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(kv)



MyApp().run()
