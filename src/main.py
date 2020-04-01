# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 00:05:36 2020

@author: Rybakov
"""

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import Line
from kivy.graphics import Color
from kivy.graphics import Rectangle

import draw

#---------------------------------------------------------------------------------------------------
# GUI.
#---------------------------------------------------------------------------------------------------

class GUI(Widget):
    """
    GUI.
    """

#---------------------------------------------------------------------------------------------------

    def __init__(self, **kwargs):
        """
        Constructor.

        Arguments:
            kwargs -- Arguments.
        """

        super(GUI, self).__init__(**kwargs)

        # Initialize drawer.
        # We draw in (0, 100) * (0, 100) area in physical world.
        # It is impossible to set painting area yet, because window is not created.
        phys_area = draw.Area((0.0, 100.0), (0.0, 100.0))
        self.Drawer = draw.Drawer(phys_area, self, None)

#---------------------------------------------------------------------------------------------------

    def OnClickA(self):
        """
        Button A OnClick.
        """

        self.Drawer.Clean()

        print("button A clicked")

#---------------------------------------------------------------------------------------------------

    def OnClickB(self):
        """
        Button B OnClick.
        """

        self.Drawer.SetColor((1.0, 0.0, 0.0, 1.0))
        self.Drawer.Line((50.0, 0.0, 100.0, 50.0))

        print("button B clicked")

#---------------------------------------------------------------------------------------------------

    def OnClickC(self):
        """
        Button C OnClick.
        """

        print("button C clicked")

#---------------------------------------------------------------------------------------------------

    def OnClickD(self):
        """
        Button D OnClick.
        """

        print("button D clicked")

#---------------------------------------------------------------------------------------------------

    def OnClickE(self):
        """
        Button E OnClick.
        """

        print("button E clicked")

#---------------------------------------------------------------------------------------------------
# Application class.
#---------------------------------------------------------------------------------------------------

class MainApp(App):
    """
    Main application.
    """

#---------------------------------------------------------------------------------------------------

    def build(self):
        """
        Build.
        """

        return GUI()

#---------------------------------------------------------------------------------------------------
# Run.
#---------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    MainApp().run()

#---------------------------------------------------------------------------------------------------
