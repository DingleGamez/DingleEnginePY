from engine.components.component import Component
from engine.components.transform import Transform

import numpy as np

class Entity:
    def __init__(self, id):
        self.id = id
        self.transform = Transform()
        self.components = np.array([], dtype=Component)

    def add_component(self, component):
        self.components = np.append(self.components, component)
        component.entity = self
        component.start()

    def get_component(self, component_type):
        for component in self.components:
            if type(component) == component_type:
                return component