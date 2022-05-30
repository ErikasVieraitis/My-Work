import simplegui,random,math
from user305_9WDPytKHWw_1 import Vector


class Wall:
    def __init__(self,pos1,pos2):
        self.pos1 = pos1.get_p()
        self.pos2 = pos2.get_p()
        self.border = 1
        
