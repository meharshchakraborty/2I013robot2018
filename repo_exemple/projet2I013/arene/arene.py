from ..robot import Robot

class Arene(object):
    def __init__(self,name):
        self.name = name
        self.robot = Robot()
        self.obstacles  = []
    def __repr__(self): 
        return "Arene 2D"+self.name+"\n"+str(self.robot)+"\n"+"".join(str(x) for x in self.obstacles)
    def add_obstacle(self,obstacle):
        self.obstacles.append(obstacle)
