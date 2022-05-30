import simplegui
from user305_9WDPytKHWw_1 import Vector


class Heart:
    
    
    def __init__(self, position, is_empty):
        self.position = position
        self.is_empty = is_empty

        
    
    def draw(self,canvas):
        
        if (self.is_empty == True):
            image = simplegui.load_image('https://i.imgur.com/ThSjyKp.png')
        else:
            image = simplegui.load_image('https://i.imgur.com/mVYYLQf.png')
            
            
        

           
        canvas.draw_image(image,(60/2, 70/2), (60,70), self.position.get_p(), (30,30))
    
        
        