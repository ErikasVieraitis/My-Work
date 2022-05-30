import simplegui
from user305_wXVUtMiY422VQF4 import Vector

class Character:
    def __init__(self, hp, movement_speed, imageurl, position, is_enemy):
        self.hp = hp
        self.movement_speed = movement_speed
        self.imageurl = imageurl 
        self.position = position
        self.is_enemy = is_enemy
        self.index = [0,0]
        self.count = 0
        self.rotation = 0
        self.frame_width = 120 
        self.frame_height = 140
        self.radius = 40
        self.dead = False

        
    def get_hit(self,damage_taken):
        if self.hp > 0:
            self.hp = self.hp - damage_taken
            if self.hp <= 0:
                self.dead = True
        else:
            self.dead = True
    def draw(self, canvas):
        image = simplegui.load_image(self.imageurl)
        canvas.draw_image(image, ((self.frame_width/2)*(self.index[0]+1), (self.frame_height/2)*(self.index[1]+1)), (self.frame_width, self.frame_height), self.position.get_p(), (360/3,420/3), self.rotation)
        
        if (self.is_enemy == True):
            canvas.draw_line(((self.position.x)-(self.hp * 10), self.position.y-50),((self.position.x)+(self.hp * 10), self.position.y-50),10,'Red')
    
    def next_frame(self):
        self.count += 1
        
        if (self.count % 4 == 0):
            if (self.index[0] <= 4):
                self.index[0] += 2
        
            if (self.index[0] > 4):
                self.index[0] = 2
            
                if (self.index[1] <= 4):
                    self.index[1] +=2
                
                if (self.index[1] > 4):
                    self.index[1] = 0
            
        
            
        