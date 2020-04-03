# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 00:05:36 2020

@author: Rybakov
"""

# Outer modules.
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

# Own modules.
import draw
import petri_net

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

        # Create test net.
        net = petri_net.Net()

        # Fill net configuration.
        activities_list = ['a', 'b', 'c', 'd', 'e', 'f']
        input_activities_list = ['a']
        output_activities_list = ['f']
        y_list = [({'c'}, {'d'}), ({'a'}, {'e'}), ({'b'}, {'c', 'f'}),
                  ({'e'}, {'f'}), ({'a', 'd'}, {'b'})]

        # Construct net.
        net.ConstructFromAlphaAlgorithm((activities_list, input_activities_list,
                                         output_activities_list, y_list))

        net.Print()
        net.Nodes[0].Center = (10.0, 50.0)
        net.Nodes[1].Center = (90.0, 50.0)
        net.Nodes[2].Center = (20.0, 50.0)
        net.Nodes[3].Center = (50.0, 50.50)
        net.Nodes[4].Center = (65.0, 75.0)
        net.Nodes[5].Center = (35.0, 75.0)
        net.Nodes[6].Center = (50.0, 25.0)
        net.Nodes[7].Center = (80.0, 50.0)
        net.Nodes[8].Center = (50.0, 75.0)
        net.Nodes[9].Center = (35.0, 25.0)
        net.Nodes[10].Center = (65.0, 50.0)
        net.Nodes[11].Center = (65.0, 25.0)
        net.Nodes[12].Center = (35.0, 50.0)

        # Draw.
        self.Drawer.DrawPetriNet(net)

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
