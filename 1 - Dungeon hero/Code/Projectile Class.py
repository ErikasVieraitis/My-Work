import simplegui

class Projectile:
    def __init__(self, pos, xvel, yvel, active,enemy_projectile):
        self.pos = pos
        self.xvel = xvel
        self.yvel = yvel
        self.active = active
        self.radius = 6
        self.enemy_projectile = enemy_projectile
        if self.enemy_projectile == True:
            self.image = simplegui.load_image('https://imgur.com/GcWRzSv.png')
        else:
            self.image = simplegui.load_image('https://i.imgur.com/5Dc9hDC.png')
    def draw(self, canvas):
        if (self.active == True):
            self.pos.x += self.xvel
            self.pos.y += self.yvel
            canvas.draw_image(self.image, (75/2, 75/2), (75,75), self.pos.get_p(), (12, 12))
            self.check_out_of_bound()

            

    def check_out_of_bound(self):
        if (self.pos.x < 80 or self.pos.x > 725 or self.pos.y > 715 or self.pos.y < 70):
            self.active = False
            
            