import simplegui

class Dungeon:
    
    def __init__(self, level, opened):
        self.level = level
        self.opened = opened
        
        
    def draw(self, canvas):
        if (self.opened == True):
            image = simplegui.load_image('https://i.imgur.com/kFUcUQZ.png')
        else:
            image = simplegui.load_image('https://i.imgur.com/BKXBqHW.png')

        canvas.draw_image(image, (1050/2, 1050/2), (1050, 1050), (400, 400), (800,800))
