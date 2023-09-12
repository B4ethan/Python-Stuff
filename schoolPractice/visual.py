#in this file, the json will be presented with kivy graphics

import json

import numpy as np
from kivy.app import App
from kivy.uix.layout import Layout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class ShowMagicCube(Layout):

    def __init__(self):
        Layout.__init__(self)
        self.n = 3
        self.loadJson()
        self.myGrid = GridLayout()
        self.myGrid.cols = self.n
        self.myGrid.size = (500, 500)
        self.add_widget(self.myGrid)

        self.squareKey = 0

        self.show()

        self.myButton = Button()
        self.myButton.x = 100
        self.myButton.y = 450
        self.myButton.text = "press to show the next maigc square"
        self.myButton.bind(on_press= self.react)
        self.add_widget(self.myButton)

       


    def react(self,t):
        if self.squareKey == 7:
            self.squareKey = 0
        else:
            self.squareKey += 1

        self.show()


    def loadJson(self):
        with open("schoolPractice\\magicSquare.json") as json_file:
            self.data = json.load(json_file)
            print (self.data)

    def show(self):
        self.labels = []
        firstSolution =list( self.data.keys())[self.squareKey]
        place =0
        for i in range(self.n):
            line = []
            for j in range(self.n):

                label = Label()
                label.text = firstSolution[place]
                place +=1
                line.append(label)
                self.myGrid.add_widget(label)
            self.labels.append(line)



class MyApp(App):
    def build(self):
        return (ShowMagicCube())


if __name__ == '__main__':
    MyApp().run()