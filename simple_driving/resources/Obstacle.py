import pybullet as p
import os


class Obstacle:
    def __init__(self, client):
        f_name = os.path.join(os.path.dirname(__file__), 'simpleObstacle.urdf')
        self.Obstacle = client.loadURDF(fileName=f_name,
                   basePosition=[4, 3, 0])
