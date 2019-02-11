import unittest
from projet2I013 import Carre,Arene,Robot
class CarreTest(unittest.TestCase):
    def test_create(self):
        carre = Carre(1,2,3)
        self.assertEqual(carre.x,1)
        self.assertEqual(carre.y,2)
        self.assertEqual(carre.l,3)


class AreneTest(unittest.TestCase):
    def setUp(self):
        self.robot = Robot()
        self.name = "name"
        self.arene = Arene(self.name)
        self.carre = Carre(1,2,3)
    def test_create(self):
        self.assertEqual(self.arene.name,self.name)
        self.assertIsInstance(self.arene.robot,Robot)
        self.assertEqual(len(self.arene.obstacles),0)
    def test_insert_obstacle(self):
        self.arene.add_obstacle(self.carre)
        self.assertEqual(len(self.arene.obstacles),1)
        self.assertEqual(self.arene.obstacles[0],self.carre)

if __name__=="__main__":
    unittest.main()