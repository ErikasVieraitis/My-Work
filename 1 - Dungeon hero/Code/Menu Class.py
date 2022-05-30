import simplegui

class Menu:
    
    def __init__(self, image, play_selected, on_menu):
        self.image = image
        self.play_selected = play_selected
        self.on_menu = on_menu
        
    def draw(self, canvas):
        image = simplegui.load_image(self.image)
        canvas.draw_image(image, (1000/2, 1000/2), (1000, 1000), (400,400), (800, 800))
        
