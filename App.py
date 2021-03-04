from kivymd.app import MDApp
from kivy.lang import Builder


kv = """
FloatLayout:
  
    MDIconButton:
        pos_hint: {'center_x':.5,'center_y':.8 }
        icon: 'language-python'
        user_font_size: '80sp'
    MDTextField:
        size_hint: 1, None
        hint_text: 'Email'
        size_hint_x: .6
        pos_hint: {'center_x':.5,'center_y':.5 }
        height: "30dp"
    MDTextField:
        size_hint: 1, None
        hint_text: 'Senha'
        size_hint_x: .6
        pos_hint: {'center_x':.5,'center_y':.4 }
        height: "30dp"

    
            
    

"""

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(kv)



MyApp().run()
