from engine.entities.camera import Camera
from engine.scenes.scene import Scene
from engine.entities.entity import Entity
from engine.components.mesh import Mesh
from engine.render.renderer import Renderer

import numpy as np
from pyglm import glm

class EditorScene(Scene):
    def __init__(self):
        self.camera = Camera()
        self.renderer = Renderer(self.camera, self)

        super().__init__()

    def start(self):
        cube = Entity(0)
        cube.add_component(Mesh("resources/textures/wood.png"))
        self.entities = np.append(self.entities, cube)

        cube1 = Entity(1)
        cube1.transform.position = glm.vec3(1.0,0.0,0.0)
        cube1.add_component(Mesh("resources/textures/brickwall.jpg"))
        self.entities = np.append(self.entities, cube1)

        cube2 = Entity(2)
        cube2.transform.position = glm.vec3(-1.0, 0.0, 0.0)
        cube2.add_component(Mesh("resources/textures/block_solid.png"))
        self.entities = np.append(self.entities, cube2)

        self.renderer.start()

    def update(self):
        for entity in self.entities:
            transform = entity.transform

            transform.rotation += glm.vec3(0.025,0.0,0.0) * 1.0

        self.renderer.update()