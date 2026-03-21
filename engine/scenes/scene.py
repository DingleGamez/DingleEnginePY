from engine.entities.entity import Entity

import numpy as np

class Scene:
    def __init__(self):
        self.entities = np.array([], dtype=Entity)

    def start(self):
        pass

    def update(self):
        pass