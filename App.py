from kivymd.app import MDApp
from kivy.lang import Builder


kv = """
FloatLayout:
    
    BoxLayout:
        pos_hint: {'center_x':.5,'center_y':.5}
        MDRaisedButton:
            text: 'Clica em mim'
            size_hint_y: .12 
            pos_hint: {'center_x':.5,'center_y':.5}
            
    

"""

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(kv)



MyApp().run()
