import sys
import os

try:
    import projet2I013
except ImportError:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    import projet2I013

robot = projet2I013.Robot()
arene = projet2I013.Arene("Mon Arene")
print("Robot: ",robot, "Arene: ",arene)
