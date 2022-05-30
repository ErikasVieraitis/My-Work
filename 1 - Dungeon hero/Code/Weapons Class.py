import simplegui

class Weapons:
    
    def __init__(self, name, fire_rate, damage, current_ammo, max_ammo, sprite_image, sprite_pos_modifier):
        self.name = name
        self.fire_rate = fire_rate
        self.damage = damage
        self.current_ammo = current_ammo
        self.max_ammo = max_ammo
        self.sprite_image = sprite_image
        self.sprite_pos_modifier = sprite_pos_modifier