class VieuxRobot(object):
    def __init__(self,x,y):
        self.x,self.y = x,y
    def __repr__(self):
        return "Je suis VieuxRobot"
    def move(self,dx,dy):
        self.x+=dx
        self.y+=dy
