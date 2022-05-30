import simplegui
from user305_0gqR7f5rlI_3 import Character
from user305_wXVUtMiY422VQF4 import Vector

class Player(Character):

    def __init__(self, hp, movement_speed, imageurl, position, is_enemy, current_weapon, weapon_list, points):
        super().__init__(hp, movement_speed, imageurl, position, is_enemy)
        self.current_weapon = current_weapon
        self.weapon_list = weapon_list
        self.points = points
        self.wcheck = False
        self.acheck = False
        self.scheck = False
        self.dcheck = False
        self.leftcheck = False
        self.downcheck = False
        self.rightcheck = False
        self.upcheck = False
        self.echeck = False
        self.spacecheck = False
        self.onecheck = False
        self.twocheck = False
        self.threecheck = False
        self.fourcheck = False
        self.I_frames = 30
    
        
        
        
    def key_listener(self, key):
        
        if key == simplegui.KEY_MAP['w']:
            self.wcheck = True
        if key == simplegui.KEY_MAP['a']:
            self.acheck = True
        if key == simplegui.KEY_MAP['s']:
            self.scheck = True
        if key == simplegui.KEY_MAP['d']:
            self.dcheck = True
            
            
        if key == simplegui.KEY_MAP['up']:
            self.upcheck = True
        if key == simplegui.KEY_MAP['left']:
            self.leftcheck = True
        if key == simplegui.KEY_MAP['down']:
            self.downcheck = True
        if key == simplegui.KEY_MAP['right']:
            self.rightcheck = True
            
        if key == simplegui.KEY_MAP['1']:
            self.onecheck = True
        if key == simplegui.KEY_MAP['2']:
            self.twocheck = True
        if key == simplegui.KEY_MAP['3']:
            self.threecheck = True
        if key == simplegui.KEY_MAP['4']: 
            self.fourcheck = True
        

        if key == simplegui.KEY_MAP['space']:
            self.spacecheck = True
            
        if key == simplegui.KEY_MAP['e']:
            self.echeck = True
            
    def key_up(self, key):
        if key == simplegui.KEY_MAP['w']:
            self.wcheck = False
        if key == simplegui.KEY_MAP['a']:
            self.acheck = False
        if key == simplegui.KEY_MAP['s']:
            self.scheck = False
        if key == simplegui.KEY_MAP['d']:
            self.dcheck = False
            
            
        if key == simplegui.KEY_MAP['up']:
            self.upcheck = False
        if key == simplegui.KEY_MAP['left']:
            self.leftcheck = False
        if key == simplegui.KEY_MAP['down']:
            self.downcheck = False
        if key == simplegui.KEY_MAP['right']:
            self.rightcheck = False
            
        if key == simplegui.KEY_MAP['1']:
            self.onecheck = False
        if key == simplegui.KEY_MAP['2']:
            self.twocheck = False
        if key == simplegui.KEY_MAP['3']:
            self.threecheck = False
        if key == simplegui.KEY_MAP['4']: 
            self.fourcheck = False
        
        if key == simplegui.KEY_MAP['space']:
            self.spacecheck = False
            
        if key == simplegui.KEY_MAP['e']:
            self.echeck = False
        
    
        
    def check_weapons(self):
        if (self.current_weapon.name == "Pistol"):
            self.imageurl = 'https://i.imgur.com/CddMSKn.png'
        elif (self.current_weapon.name == "Ak47"):
            self.imageurl = 'https://i.imgur.com/vU0ffg9.png'
        elif (self.current_weapon.name == "Shotgun"):
            self.imageurl = 'https://i.imgur.com/cUdqPIA.png'
        elif (self.current_weapon.name == "Mac11"):
            self.imageurl = 'https://i.imgur.com/iaReKmV.png'
        elif (self.current_weapon.name == "Desert Eagle"):
            self.imageurl = 'https://i.imgur.com/IcXgl3l.png'