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

#---------------------------------------------------------------------------------------------------
# GUI.
#---------------------------------------------------------------------------------------------------

class GUI(Widget):

#---------------------------------------------------------------------------------------------------

    def OnClickA(self):
        '''
        Button A OnClick.
        '''

        print("button A clicked")

#---------------------------------------------------------------------------------------------------

    def OnClickB(self):
        '''
        Button B OnClick.
        '''

        print("button B clicked")

#---------------------------------------------------------------------------------------------------

    def OnClickC(self):
        '''
        Button C OnClick.
        '''

        print("button C clicked")

#---------------------------------------------------------------------------------------------------

    def OnClickD(self):
        '''
        Button D OnClick.
        '''

        print("button D clicked")

#---------------------------------------------------------------------------------------------------

    def OnClickE(self):
        '''
        Button E OnClick.
        '''

        print("button E clicked")

#---------------------------------------------------------------------------------------------------
# Application class.
#---------------------------------------------------------------------------------------------------

class MainApp(App):

#---------------------------------------------------------------------------------------------------

    def build(self):
        '''
        Build.
        '''

        return GUI()

#---------------------------------------------------------------------------------------------------
# Run.
#---------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    MainApp().run()

#---------------------------------------------------------------------------------------------------
