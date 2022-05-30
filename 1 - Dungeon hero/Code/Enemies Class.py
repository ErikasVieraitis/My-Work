import simplegui, random 

from user305_0gqR7f5rlI_3 import Character
from user305_9WDPytKHWw_1 import Vector



class Enemies(Character):
    
    def __init__(self, hp, movement_speed, imageurl, position, is_enemy, vel, points):
        super().__init__(hp, movement_speed, imageurl, position, is_enemy)
        self.vel = vel
        self.points = points
        self.can_shoot = False        
    def update(self):
        
        self.position.add(self.vel*self.movement_speed)
        