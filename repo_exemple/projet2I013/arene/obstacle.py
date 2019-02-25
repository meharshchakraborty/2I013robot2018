class Carre(object):
    def __init__(self,x,y,l):
        self.x,self.y,self.l=x,y,l
    def __repr__(self):
        return "Carre ({},{},{})".format(self.x,self.y,self.l)