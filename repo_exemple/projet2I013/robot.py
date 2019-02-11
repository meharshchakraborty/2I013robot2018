class Robot(object):
    def __init__(self,x=0,y=0,z=0):
        self.x,self.y,self.z = x,y,z
    def __repr__(self):
        return "Je suis Robot"
    def move(self,dx,dy):
        self.x+=dx
        self.y+=dy
