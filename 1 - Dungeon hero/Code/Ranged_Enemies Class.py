import simplegui, random 

from user305_0gqR7f5rlI_3 import Character
from user305_9WDPytKHWw_1 import Vector
from user305_YAxKsjQdGY_3 import Enemies
from user305_rSKjfOc1b9_4 import Projectile


class ranged_enemies(Enemies):
    def __init__(self, hp, movement_speed, imageurl, position, is_enemy, vel,shoot_count, points):
        super().__init__(hp, movement_speed, imageurl, position, is_enemy,vel)
        self.can_shoot = True
        self.points = points
        self.enemy_shoot_count = shoot_count        
    def update(self):
        self.position.add(self.vel*self.movement_speed)
        
               
    def shoot(self,player_position):
        x_vel = self.position.x - player_position.x
        y_vel = self.position.y - player_position.y
        return Projectile(Vector(self.position.x, self.position.y),-x_vel/50,-y_vel/50,True,True)
  
        