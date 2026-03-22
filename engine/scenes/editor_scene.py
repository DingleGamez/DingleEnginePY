import time

from engine.entities.camera import Camera
from engine.scenes.scene import Scene
from engine.entities.entity import Entity
from engine.components.model import Model
from engine.render.renderer import Renderer

import numpy as np
import math
from pyglm import glm
import glfw

class EditorScene(Scene):
    def __init__(self):
        self.camera = Camera()
        self.renderer = Renderer(self.camera, self)

        super().__init__()

    def start(self):
        models = [
            "resources/models/charmander/model.obj",
            "resources/models/pikachu/model.obj",
            "resources/models/cubone/model.obj"
        ]
        sizes = [
            0.75, 0.65, 1,
        ]
        offsets_y = [
            -0.25,0.0,0.0
        ]

        id = 0
        curr = 0
        count = 1

        for x in range(-count,count + 1):
            for y in range(-count,count + 1):
                cube = Entity(id)
                cube.transform.position = glm.vec3(float(x * 0.75),float(y * 0.75) + offsets_y[curr],0.0)
                cube.transform.scale = glm.vec3(1.0,1.0,1.0) * sizes[curr]
                cube.add_component(Model(models[curr]))
                self.entities = np.append(self.entities, cube)

                id += 1
                curr += 1

                if curr >= 3:
                    curr = 0

        self.renderer.start()

    def update(self):
        for i in range(len(self.entities)):
            entity = self.entities[i]
            transform = entity.transform

            transform.rotation += glm.vec3(0.0,0.025,0.0) * 4.0
            transform.position.z = 0.25 * math.sin(i - glfw.get_time())

        self.renderer.update()