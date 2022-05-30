import simplegui, random

class Drop:
    
    def __init__(self, name, position, image):
        self.name = name
        self.position = position 
        self.image = image 
        
        
    
    def draw(self, canvas):
        image = simplegui.load_image(self.image)
        canvas.draw_image(image, (60/2, 70/2), (60, 70), self.position.get_p(), (60,70))
        
        

