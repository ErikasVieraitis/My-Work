import simplegui, random, math, sys
from user305_0gqR7f5rlI_3 import Character
from user305_SyOgT1EUoY_11 import Player
from user305_1shhmyUe0w_6 import Dungeon
from user305_9WDPytKHWw_1 import Vector
from user305_YAxKsjQdGY_4 import Enemies
from user305_LSLhQT3xTg_8 import Wall
from user305_rSKjfOc1b9_4 import Projectile 
from user305_Ym27MVQR35_2 import Menu
from user305_WG8CIVkLu22FA5Y_6 import Drop
from user305_50XyNq9LmG_11 import Heart
from user305_Do4izs4J96QDraX_5 import Weapons
from user305_pGtkxL0RI2_9 import ranged_enemies
        
    
class Interaction:
    def __init__(self, player, dungeon, enemies, walls, projectile_list, menu, drop_list, heart_list):
        self.player = player
        self.dungeon = dungeon
        self.enemies = enemies 
        self.walls = walls
        self.projectile_list = projectile_list
        self.menu = menu
        self.drop_list = drop_list
        self.heart_list = heart_list
        self.shootcount = 1
        self.shoot_active = False
        self.chance = 0
        self.temp_weapon = None
        self.enemy_range = 500
        self.collision_count = 60
                                
    def draw(self, canvas):
        if (self.menu.on_menu == True):
            self.menu.draw(canvas)
            canvas.draw_text("GAME CONTROLS:            'WSAD' to move.  ARROW KEYS to shoot.  'E' to pick up item   '1-4' to select weapon.", (50, 780), 15, "Orange")
            canvas.draw_text("Select an option using arrow keys. Press space to enter it.", (160, 700), 20, "Orange")
            canvas.draw_text("The game gets harder the further you go.", (220, 720), 20, "Orange")
            if (self.player.upcheck == True):
                self.menu.play_selected = True
                self.menu.image = 'https://i.imgur.com/4cnQY7L.png'
                
            if (self.player.downcheck == True):
                self.menu.play_selected = False
                self.menu.image = 'https://i.imgur.com/olmH2jE.png'
            
            if (self.player.spacecheck == True and self.menu.play_selected == True):
                self.menu.on_menu = False
            if (self.player.spacecheck == True and self.menu.play_selected == False):
                exit()
                
        if (self.menu.on_menu == False):
            
            
            
            
  

            self.update()
            self.dungeon.draw(canvas)
            
            image = simplegui.load_image('https://i.imgur.com/Q7C6Jvu.png')
            canvas.draw_image(image, (200/2, 50/2), (200, 50), (200, 770), (200, 50))
            
            
            if (self.player.current_weapon.current_ammo == 0):
                canvas.draw_text("Ammo: " + str(self.player.current_weapon.current_ammo) + " / " + str(self.player.current_weapon.max_ammo), (510,780), 30, "Red")
            else:
                canvas.draw_text("Ammo: " + str(self.player.current_weapon.current_ammo) + " / " + str(self.player.current_weapon.max_ammo), (510,780), 30, "White")
                
            
            canvas.draw_text("Points:  " + str(self.player.points), (550, 40), 30, "White")
            canvas.draw_text("Level:  " + str(self.dungeon.level), (200, 30), 20, "Orange")
            
            
          
            for heart in self.heart_list:
                heart.draw(canvas)

                
            
          
            
            
            for weapons in self.player.weapon_list:
                image = simplegui.load_image(weapons.sprite_image)
                canvas.draw_image(image, (60/2, 70/2), (60, 70), (125 + weapons.sprite_pos_modifier, 767), (60/1.2, 70/1.2))
                

            for projectiles in self.projectile_list:
                projectiles.draw(canvas)
                if (projectiles.active == False):
                    self.projectile_list.remove(projectiles)
            
            
            for drops in self.drop_list:
                drops.draw(canvas)
                if (self.player.echeck == True and math.sqrt(((self.player.position.x - drops.position.x)**2)+((self.player.position.y - drops.position.y)**2)) < 40):
                    
                    if (drops.name == "Heart"):
                        if self.player.hp != 6:
                            self.player.hp += 1
                            for heart in self.heart_list:
                                if heart.is_empty == True:
                                    heart.is_empty = False
                                    break
                    if (drops.name == "Ammo"):
                        self.player.current_weapon.current_ammo = self.player.current_weapon.max_ammo
                    if (drops.name == "SuperAmmo"):
                        for weapons in self.player.weapon_list:
                            weapons.current_ammo = weapons.max_ammo
                            
                    if (drops.name == "AK"):
                        if len(self.player.weapon_list) == 4:
                            self.weapon_swap(Weapons("Ak47", 15, 1, 100, 100, 'https://i.imgur.com/TlsFfxM.png', 0))
                        else:
                            self.player.current_weapon = Weapons("Ak47", 15, 1, 100, 100, 'https://i.imgur.com/TlsFfxM.png', 0)
                            self.player.weapon_list.append(self.player.current_weapon)  
                        self.weapon_list_modifier()
                        
                    if (drops.name == "Desert"):
                        if len(self.player.weapon_list) == 4:
                            self.weapon_swap(Weapons("Desert Eagle", 60, 3, 35, 35, 'https://i.imgur.com/5O1cZ5l.png', 0))
                        else:
                            self.player.current_weapon = Weapons("Desert Eagle", 60, 3, 35, 35, 'https://i.imgur.com/5O1cZ5l.png', 0)
                            self.player.weapon_list.append(self.player.current_weapon)
                        self.weapon_list_modifier()
                        
                    if (drops.name == "Mac"):
                        if len(self.player.weapon_list) == 4:
                            self.weapon_swap(Weapons("Mac11", 10, 0.5, 180, 180, 'https://i.imgur.com/mgorX0n.png', 0))
                        else:
                            self.player.current_weapon = Weapons("Mac11", 10, 0.5, 160, 160, 'https://i.imgur.com/mgorX0n.png', 0)
                            self.player.weapon_list.append(self.player.current_weapon)
                        self.weapon_list_modifier()
                        
                    if (drops.name == "ShotGun"):
                        if len(self.player.weapon_list) == 4:
                            self.weapon_swap(Weapons("Shotgun", 40, 1, 80, 80, 'https://i.imgur.com/1H0UeRr.png', 0))
                        else:
                            self.player.current_weapon = Weapons("Shotgun", 40, 1, 80, 80, 'https://i.imgur.com/1H0UeRr.png', 0)
                            self.player.weapon_list.append(self.player.current_weapon)
                        self.weapon_list_modifier()
                    self.drop_list.remove(drops)
                    
            
            
            if (self.player.current_weapon == self.player.weapon_list[0]):
                canvas.draw_line((100, 797),(150, 797),5,'Red')
            elif (self.player.current_weapon == self.player.weapon_list[1]):
                canvas.draw_line((150, 797),(200, 797),5,'Red')
            elif (self.player.current_weapon == self.player.weapon_list[2]):
                canvas.draw_line((200, 797),(250, 797),5,'Red')
            elif (self.player.current_weapon == self.player.weapon_list[3]):
                canvas.draw_line((250, 797),(300, 797),5,'Red')
            
            if (self.player.onecheck == True):
                self.player.current_weapon = self.player.weapon_list[0]
            if (self.player.twocheck == True and len(self.player.weapon_list) >= 2):
                self.player.current_weapon = self.player.weapon_list[1]
            if (self.player.threecheck == True and len(self.player.weapon_list) >= 3):
                self.player.current_weapon = self.player.weapon_list[2]
            if (self.player.fourcheck == True and len(self.player.weapon_list) >= 4):
                self.player.current_weapon = self.player.weapon_list[3]
              
            
            
            
            self.player.draw(canvas)
            self.player.check_weapons()
        
        
        

            

       
            for enemy in self.enemies:
                # need to make enemy rotate according to player
                enemy.draw(canvas)
                enemy.rotation = math.pi
                enemy.next_frame()
            
            
            
            for enemy in self.enemies:
                for projectile in self.projectile_list:
                    if projectile.enemy_projectile == False:
                        distance_between = enemy.position.copy().subtract(projectile.pos) 
                        if distance_between.length() < (enemy.radius + projectile.radius):
                            enemy.get_hit(self.player.current_weapon.damage)
                            projectile.active = False
                            
                    elif projectile.enemy_projectile == True and enemy.can_shoot == True:
                        distance_between = self.player.position.copy().subtract(projectile.pos) 
                        if distance_between.length() < (self.player.radius + projectile.radius):
                            if self.player.dead == False and projectile.active == True:
                                projectile.active = False
                                self.heart_depletion()
                                self.player.get_hit(1)
                
                
                
                
                
                
            if (self.player.wcheck == True and self.player.position.y > 70):
                self.player.position.add(Vector(0, -self.player.movement_speed))
                self.player.rotation = 0
            

            if (self.player.acheck == True and self.player.position.x > 85):
                self.player.position.add(Vector(-self.player.movement_speed, 0))
                self.player.rotation = -math.pi/2

            if (self.player.scheck == True and self.player.position.y < 705):
                self.player.position.add(Vector(0, self.player.movement_speed))
                self.player.rotation = math.pi

            if (self.player.dcheck == True and self.player.position.x < 720):
                self.player.position.add(Vector(self.player.movement_speed, 0))
                self.player.rotation = math.pi/2
        
        
        
            if (self.player.wcheck == True or self.player.acheck == True or 
                self.player.scheck == True or self.player.dcheck == True):
                self.player.next_frame()
            
        
        
        

            if (self.player.current_weapon.current_ammo > 0):
                
                if (self.player.leftcheck == True):
                    self.player.rotation = -math.pi/2
                    if (self.shoot_active == True):
                        self.projectile_list.append(Projectile(Vector(self.player.position.x -55, self.player.position.y), -5, 0, True,False))
                        if (self.player.current_weapon.name == "Shotgun"):
                            self.projectile_list.append(Projectile(Vector(self.player.position.x - 70, self.player.position.y), -5, 0, True,False))
                            self.player.current_weapon.current_ammo -= 1
                        self.player.current_weapon.current_ammo -= 1
                        self.shoot_reset()
                                        
                if (self.player.rightcheck == True):
                    self.player.rotation = math.pi/2
                    if (self.shoot_active == True):
                        self.projectile_list.append(Projectile(Vector(self.player.position.x +55, self.player.position.y), 5, 0, True,False))
                        if (self.player.current_weapon.name == "Shotgun"):
                            self.projectile_list.append(Projectile(Vector(self.player.position.x + 70, self.player.position.y), 5, 0, True,False))
                            self.player.current_weapon.current_ammo -= 1
                        self.player.current_weapon.current_ammo -= 1
                        self.shoot_reset()

                if (self.player.upcheck == True):
                    self.player.rotation = 0
                    if (self.shoot_active == True):
                        self.projectile_list.append(Projectile(Vector(self.player.position.x, self.player.position.y -55), 0, -5, True,False))
                        if (self.player.current_weapon.name == "Shotgun"):
                            self.projectile_list.append(Projectile(Vector(self.player.position.x, self.player.position.y -70), 0, -5, True,False))
                            self.player.current_weapon.current_ammo -= 1
                        self.player.current_weapon.current_ammo -= 1
                        self.shoot_reset()
            
                if (self.player.downcheck == True):
                    self.player.rotation = math.pi
                    if (self.shoot_active == True):
                        self.projectile_list.append(Projectile(Vector(self.player.position.x, self.player.position.y +55), 0, 5, True,False))
                        if (self.player.current_weapon.name == "Shotgun"):
                            self.projectile_list.append(Projectile(Vector(self.player.position.x, self.player.position.y +70), 0, 5, True,False))
                            self.player.current_weapon.current_ammo -= 1
                        self.player.current_weapon.current_ammo -= 1
                        self.shoot_reset()
                

                
                    
                    
                if (self.shootcount % self.player.current_weapon.fire_rate == 0):
                    self.shoot_active = True   
                else:
                    self.shootcount += 1
       
    def heart_depletion(self):
        for heart in reversed(self.heart_list):
            if heart.is_empty == False:
                heart.is_empty = True
                break

            
    def weapon_list_modifier(self):

        if (self.player.current_weapon == self.player.weapon_list[1]):
            self.player.current_weapon.sprite_pos_modifier += 50
            
        elif (self.player.current_weapon == self.player.weapon_list[2]):
            self.player.current_weapon.sprite_pos_modifier += 100
            
        elif (self.player.current_weapon == self.player.weapon_list[3]):
            self.player.current_weapon.sprite_pos_modifier += 150
    
    
    def weapon_swap(self, currentweapon):
        
        for i in range(4):
            if self.player.weapon_list[i] == self.player.current_weapon:
                self.player.weapon_list[i] = currentweapon
                self.player.current_weapon = self.player.weapon_list[i]
        

        
    def generate_drop(self, enemy):
        self.chance = random.randint(0,18)
        
        if (self.chance == 1 or self.chance == 2 or self.chance == 3):
            self.drop_list.append(Drop("Heart", enemy.position, 'https://i.imgur.com/mVYYLQf.png'))
            

        elif (self.chance == 4 or self.chance == 5):
            self.drop_list.append(Drop("Ammo", enemy.position, 'https://i.imgur.com/p8ucI7W.png'))
            
        elif (self.chance == 6):
            self.drop_list.append(Drop("SuperAmmo", enemy.position, 'https://i.imgur.com/Dll5Rw4.png'))
        
        elif (self.chance == 10 or self.chance == 11):
            randweapon = random.randint(0,3)
            if (randweapon == 0):
                self.drop_list.append(Drop("AK", enemy.position, 'https://i.imgur.com/TlsFfxM.png'))
            elif (randweapon == 1):
                self.drop_list.append(Drop("Mac", enemy.position, 'https://i.imgur.com/mgorX0n.png'))
            elif (randweapon == 2):
                self.drop_list.append(Drop("ShotGun", enemy.position, 'https://i.imgur.com/1H0UeRr.png'))
            elif (randweapon == 3):
                self.drop_list.append(Drop("Desert", enemy.position, 'https://i.imgur.com/5O1cZ5l.png'))
        

            
    def shoot_reset(self):
        self.shoot_active = False
        self.shootcount = 1
        
    def touching(self,e1,e2):
        dist_vec = e1.position.copy().subtract(e2.position)
        return dist_vec.length() < e1.frame_width/4 + e2.frame_width/4
    
    
    def move(self,e1,e2):
        
        dist_vec = e1.position.copy().subtract(e2.position)

        unit = dist_vec.copy().normalize()

            
        e1.vel = unit
        e2.vel = -unit
        
        
 
        
    def collide(self,e1,e2):
        if self.touching(e1,e2):

            self.move(e1,e2)


        
    
    
    def update(self):
        
        self.collision_count -= 1
        if (self.collision_count < 0):
            self.collision_count = 0
        
        for enemy in self.enemies:
            enemy.update()
            p_dist_e = enemy.position.copy().subtract(self.player.position)
            unit = p_dist_e.copy().normalize()
            
            if enemy.can_shoot == True:
                if p_dist_e.length() < self.enemy_range:
                    if enemy.enemy_shoot_count % 120 == 0:
                        self.projectile_list.append(enemy.shoot(self.player.position))
            
            
                enemy.enemy_shoot_count = enemy.enemy_shoot_count + 1
            
            enemy.vel = (-Vector(unit.x/3,unit.y/3))
            self.collide(enemy,self.player)
            if self.touching(enemy,self.player) and self.collision_count == 0:
                self.collision_count = 60
                self.player.get_hit(1)
                self.heart_depletion()
            if enemy.dead == True:
                self.player.points += enemy.points
                self.generate_drop(enemy)
                self.enemies.remove(enemy)
                
                
        for enemy1 in self.enemies:
            for enemy2 in self.enemies:
                if enemy1 != enemy2 and self.touching(enemy1,enemy2):
                    self.collide(enemy1,enemy2)
                    
                
          

        
        
class GameLoop:
    
    def __init__(self):
        self.modifier = 0
        self.ENEMYNUM = random.randint(3,4)
        self.TOP = 65 
        self.BOTTOM = 740
        self.heart_pos = 50
        self.projectile_list = []
        self.enemy_list = []
        self.drop_list = []
        self.heart_list = []
        self.walls = [Wall(Vector(self.TOP,self.TOP),Vector(self.TOP,self.BOTTOM)), Wall(Vector(self.TOP,self.BOTTOM),Vector(self.BOTTOM,self.BOTTOM)),
         Wall(Vector(self.BOTTOM,self.TOP),Vector(self.BOTTOM,self.BOTTOM)),Wall(Vector(self.TOP,self.TOP),Vector(self.BOTTOM,self.TOP))]
        self.menu = Menu('https://i.imgur.com/4cnQY7L.png', True, True)
        self.base_gun = Weapons("Pistol", 30, 1, 200, 200, 'https://i.imgur.com/0O1YmHD.png', 0)
        self.player = Player(6, 3, 'https://i.imgur.com/CddMSKn.png', Vector(400, 700), False, self.base_gun, [self.base_gun], 0)  
        self.dungeon = Dungeon(1, False)
        self.start_active = False
        self.i = Interaction(self.player, self.dungeon, self.enemy_list, self.walls, self.projectile_list, self.menu, self.drop_list, self.heart_list)

        
    def draw(self, canvas):
        if self.start_active == False:
            for i in range(self.ENEMYNUM):
                self.enemy_list.append(self.randEnemy())
            for i in range(self.player.hp):
                self.heart_list.append(Heart(Vector(self.heart_pos, 27), False))
                self.heart_pos += 20

            self.start_active = True
        
        if self.start_active == True:
            if (self.player.dead == True):
                image = simplegui.load_image('https://i.imgur.com/MAQ40Sp.png')
                canvas.draw_image(image, (1000/2, 1000/2), (1000, 1000), (400, 400), (800, 800))
                canvas.draw_text("You made it to Level: " + str(self.dungeon.level), (120, 420), 60, "Orange")
                canvas.draw_text("With " + str(self.player.points) + " points", (250, 480), 60, "Orange")               
                canvas.draw_text("Press E to exit the game", (120, 700), 60, "Orange")
                if (self.player.echeck == True):
                    sys.exit()
                    

                    

            else:
                self.i.draw(canvas)
                if (len(self.enemy_list) == 0):
                    self.dungeon.opened = True
                    if (self.player.position.y < 80 and self.player.position.x > 350 and self.player.position.x < 450):
                        self.next_room()
                
            
            
            
        
                
            
            

        
    def next_room(self):
        self.ENEMYNUM += 1
        if (self.ENEMYNUM > 10):
            self.ENEMYNUM = 10
        for i in range(self.ENEMYNUM):
            self.i.enemies.append(self.randEnemy())
        
        self.dungeon.opened = False
        self.player.position = Vector(400, 720)
        self.i.drop_list = []
        self.i.projectile_list = []
        self.dungeon.level +=1
        
        if (self.dungeon.level % 5 == 0):
            self.modifier += 1

        
        

            
    
    def randPos(self): 
        return Vector(random.randint(70,705),random.randint(85,400))

    def randVel(self): 
        return Vector(random.randint(1,1),random.randint(1,1))
    
    def randShoot_count(self): 
        return random.randint(0,100)
    def randEnemy(self):
        selection = [
                    Enemies(3 + self.modifier, random.randint(6,8 + self.modifier), 'https://i.imgur.com/4m9xLmq.png', self.randPos(), True, self.randVel(), 5), 
                    Enemies(4 + self.modifier, random.randint(3,4 + self.modifier), 'https://i.imgur.com/33dhzaF.png', self.randPos(), True, self.randVel(), 5), 
                    Enemies(3 + self.modifier, random.randint(4,6 + self.modifier), 'https://i.imgur.com/O01BJqL.png', self.randPos(), True, self.randVel(), 5),
                    Enemies(5 + self.modifier, random.randint(4,5 + self.modifier), 'https://i.imgur.com/x8tNX3p.png', self.randPos(), True, self.randVel(), 10),
                    ranged_enemies(3 + self.modifier, random.randint(2,4 + self.modifier), 'https://i.imgur.com/xDi6ngE.png', self.randPos(), True, self.randVel(),self.randShoot_count(), 10)
                    ]
    
        return random.choice(selection)

        










    

start = GameLoop()    
    
frame = simplegui.create_frame("Home", 800, 800)
frame.set_draw_handler(start.draw)
frame.set_keydown_handler(start.player.key_listener)
frame.set_keyup_handler(start.player.key_up)
frame.start()