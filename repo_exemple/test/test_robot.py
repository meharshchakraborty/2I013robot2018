import unittest
from projet2I013 import Robot


class RobotTest(unittest.TestCase):
    def setUp(self):
        self.robot = Robot()
    def test_create(self):
        self.assertEqual(self.robot.x,0)
        self.assertEqual(self.robot.y,0)
        self.assertEqual(self.robot.z,0)
    def test_create_arg(self):
        robot = Robot(1,2,3)
        self.assertEqual(robot.x,1)
        self.assertEqual(robot.y,2)
        self.assertEqual(robot.z,3)
    def test_move(self):
        x,y,z=self.robot.x,self.robot.y,self.robot.z
        self.robot.move(1,1)
        self.assertEqual(self.robot.x,x+1)
        self.assertEqual(self.robot.y,y+1)
        self.assertEqual(self.robot.z,z)

if __name__=="__main__":
    unittest.main()