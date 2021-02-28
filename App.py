from kivymd.app import MDApp
from kivy.lang import Builder


kv = """
FloatLayout:   
    MDIconButton:
        icon: 'language-python'
        size_hint_x: 1.
        size_hint_y: 1.
    
            
    

"""

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(kv)



MyApp().run()
