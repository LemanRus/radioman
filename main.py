import os

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

import screens

backs = {"resistors_markings_select_screen": "markings_screen",
         "th_resistors_marking_screen": "resistors_markings_select_screen",
         "smd_resistors_marking_screen": "resistors_markings_select_screen",
         "capacitors_marking_screen": "markings_screen"}


class RadioMan(MDApp):
    def build(self):
        Window.bind(on_keyboard=self.android_back_click)
        Window.softinput_mode = 'below_target'
        self.theme_cls.primary_palette = "DeepPurple"
        self.load_all_kv_files("kv")
        return Builder.load_file("kv/main.kv")

    def back_to_screen(self):
        try:
            markings_tab_sm = self.root.children[1].children[0].children[0]
        except IndexError:
            pass
        else:
            if markings_tab_sm.current in backs:
                markings_tab_sm.current = backs[markings_tab_sm.current]

    def android_back_click(self, window, key, *args):
        if key == 27:
            self.back_to_screen()
        return True


RadioMan().run()
