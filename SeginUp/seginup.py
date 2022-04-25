import kivy.utils

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
from kivymd.toast import toast

class MyApp(MDApp):
    def __init__(self):
        MDApp.__init__(self)
        self.builder = Builder.load_file('style.kv')
    
    def name(self, name):
        if name == '':
            toast('Error')
            exit()
        
        with open('test.txt', 'w') as f:
            f.write(name.text)
        
        toast('Имя записан')
    
    def build(self):
        return self.builder

if __name__ == '__main__':
    MyApp().run()