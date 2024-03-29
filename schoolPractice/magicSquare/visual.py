#in this file, the json will be presented with kivy graphics
import json
import numpy as np
from kivy.app import App
from kivy.uix.layout import Layout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.text import LabelBase

class ShowMagicCube(Layout):

    def __init__(self):
        Layout.__init__(self)
        self.n = 3
        self.loadJson()
        self.myGrid = GridLayout()
        self.myGrid.cols = self.n
        self.myGrid.size = (500, 500)
        self.add_widget(self.myGrid)

        self.squareKey = 0 #the index of the magic sqaure

        #loading texts font
        LabelBase.register("numbersFonts", fn_regular="schoolPractice\\magicSquare\\font\\Cweamy-Regular.otf")
        LabelBase.register("buttonFonts", fn_regular="schoolPractice\\magicSquare\\font\\buttonFont.ttf")

        self.show(list(self.data.keys())[self.squareKey])

        #designing the button
        self.myButton = Button()
        self.myButton.x = 250
        self.myButton.y = 470
        self.myButton.width= 400
        self.myButton.background_color = (186/255, 228/255, 229/255, 1)
        self.myButton.text = "press to show the next magic square"
        self.myButton.font_name = "buttonFonts"
        self.myButton.font_size = 40
        self.myButton.bind(on_press= self.react)
        self.add_widget(self.myButton)

    def react(self, t):
        self.squareKey += 1
        if self.squareKey == 8:
            self.squareKey = 0  

        self.myGrid.clear_widgets() #remove the current grid

        current_square = list(self.data.keys())[self.squareKey] #create the new square 

        self.show(current_square) #show it on the window

    def loadJson(self):
        with open("schoolPractice\\magicSquare\\magicSquare.json") as json_file:
            self.data = json.load(json_file)
            print (self.data)

    def show(self, magic_square):
        self.labels = []
        place = 0
        for i in range(self.n):
            self.line = []
            for j in range(self.n):
                label = Label()
                label.text = magic_square[place]
                place += 1

                label.font_name = "numbersFonts"  
                label.font_size = 20   

                self.line.append(label)
                self.myGrid.add_widget(label)
            self.labels.append(self.line)            

class MyApp(App):
    def build(self):
        return (ShowMagicCube())


if __name__ == '__main__':
    MyApp().run()