# Creating the APP and GUI

from ctypes import alignment, resize
import os
import time
import tkinter as tk
from tkinter import CENTER, filedialog, Text
import os
from tkinter import font
from turtle import color

from matplotlib.font_manager import font_family_aliases
import PySimpleGUI as sg
from main import feed_parse
from main import feed



def main():

    # Text Font
    font = ("Share Tech Mono", 11)
    # Background Color
    back_color = '#222'
    # Border Width
    borders = 0



    layout= [
        [sg.Text(feed_parse(), background_color=("#222"))],
        [sg.Button("Refresh", button_color=back_color, border_width = borders)],
        [sg.Button("OK", border_width= borders, button_color=back_color )]
    ]


    background = sg.theme_background_color("#222")

    # Create Window
    window = sg.Window("Feed",
        layout, 
        background, 
        font=font,
        no_titlebar=True,
        grab_anywhere=True,
        size=(900, 500),
        
        )

    #  Create Refresh Timer
    # refresh = 0
    # def refresh_timer():
    #     print('wating 1 minute before refresh')
    #     time.sleep(60)
    #     refresh = 1
    #     return(refresh)
    # refresh_timer()



    # Create Event Loop 
    while True:
        event, values = window.read()
        # Refresh Feed when "REFRESH is clicked"
        if event == "Refresh" or refresh == 1:
            print('refreshing feed')
            feed_parse()
            # refresh_timer()
            continue
        # End program if user closes window
        # Or presses OK button
        if event == "OK" or event == sg.WIN_CLOSED:
            break


main()