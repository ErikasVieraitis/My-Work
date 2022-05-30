
You will find 13 files, this is what each of them are:

Main Method - This file contains the 2 main classes "Interaction" and "GameLoop" which contain most of the games main logic and algorithms 
Character Class - Contains all the functions used for each character on the screen like a get_hit method and health, movement etc. 
	          Also handles drawing of each character on the canvas as well as each animation for each character
Player Class - Inherited from the character class and contains functions only the player uses, like keyboard presses and weapon switching 
Dungeon Class - Handles drawing for the dungeon and the dungeons open/closed states 
Vector Class - A pre given class that is the baseline for handling coordinate manipulation in the game
Enemies Class - Inherited from the character class and contains the functions the enemies need to use, like player_hit and alive/dead states
Ranged_Enemies Class - Inherited from the character class and contains the functions for ranged enemies like the shooting mechanics 
Wall Class - Handles wall collisions for projectiles and characters 
Projectile Class - Handles projectile properties and functions like updating projectile movements, collisions for the projectiles and the drawing of them
Menu Class - Handles the drawing of the Menu as well as different selection states like if you had Play or Exit Selected it would draw it differently
Drop Class - Handles the drawing and the functions of each drop item when an enemy is killed
Heart Class - Handles the drawing of the hearts of the player
Weapons Class - Handles each function of each weapon. For example the damage, the fire-rate, the ammo and the weapon type as there are 5 different weapons in the game




Code Skulptor Link to play the game - https://py3.codeskulptor.org/#user305_seIMoQMe15_6.py

(Click on the screen first to activate keyboard)