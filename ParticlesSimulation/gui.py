#Slider, button and its GUI is taken from: https://github.com/osama-usuf/Interactive-Ant-Colony-Optimization-Simulation

from button import Button
from slider import Slider


class GUI: 
    def __init__(self):
        self.buttons = []
        self.sliders = []
        self.bg = [1080, 0, 200, 720]  # x,y,w,h
        # Pressable Buttons
        # # #Toggle Buttons
        self.buttons.append(Button('Add Car', self.bg))
        self.buttons.append(Button('Remove Car', self.bg))
        self.buttons[0].pressed = False  # press remove by default

        # Sliders
        self.sliders.append(Slider('Amount of particles', 1, 20, 1, self.bg))
        self.sliders.append(Slider('C02 Intensity', 1,5,1,self.bg))
        self.sliders.append(Slider('Car Speed', 1,5,1,self.bg))
        self.sliders.append(Slider('Lifespan', 1, 10, 1, self.bg))
        self.tit = '    Particle Simulation\n'
        self.crs = '    Computational Intelligence\n'
        self.auth_1 = '    Muhammad - mm06369\n'
        self.auth_2 = '    Ali Asghar Yousuf - ay06993'
        self.crdt = self.crs+self.tit+self.auth_1+self.auth_2

    def draw(self):
        text
        noStroke()
        rectMode(CORNER)
        fill(204, 102, 0)
        rect(*self.bg)
        self.drawElements()
        textSize(11)
        fill(255)
        text(self.crdt, self.bg[0], self.bg[1] +
             (Slider.sliderCount+1)*Button.buttonSpacing, 160, 120)

    def drawElements(self):
        for i in self.buttons:
            i.draw()
        for i in self.sliders:
            i.draw()

    def mouseHover(self):
        for i in self.buttons:
            if (i.mouseHover()):
                return i.id
        return None
    
    def mousepressed(self):
        for i in self.buttons:
            if (i.mousepressed()):
                return i.id
        return None

    def toggleButton(self, id):
        self.buttons[id].pressed = not self.buttons[id].pressed
