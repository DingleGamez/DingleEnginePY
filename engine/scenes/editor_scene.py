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
        textures = [
            "resources/textures/wood.png",
            "resources/textures/brickwall.jpg",
            "resources/textures/block_solid.png",
        ]

        id = 0
        curr_tex = 0
        count = 1

        for x in range(0,1):
            for y in range(0,1):
                cube = Entity(id)
                cube.transform.position = glm.vec3(float(x),float(y),0.5)
                cube.add_component(Mesh(textures[curr_tex]))
                self.entities = np.append(self.entities, cube)

                id += 1
                curr_tex += 1

                if curr_tex >= 3:
                    curr_tex = 0

        face = Entity(id)
        face.transform.position = glm.vec3(0.0,0.0,3.0)
        face.transform.scale = glm.vec3(1.0,1.0,1.0) * 0.5
        face.add_component(Mesh("resources/textures/awesomeface.png"))
        self.entities = np.append(self.entities, face)

        self.renderer.start()

    def update(self):
        for i in range(len(self.entities) - 1):
            entity = self.entities[i]
            transform = entity.transform

            transform.rotation += glm.vec3(0.025,0.025,0.025) * 10.0

        face_transform = self.entities[len(self.entities) - 1].transform
        face_transform.rotation += glm.vec3(0.0, 0.0, 0.025) * 100.0

        self.renderer.update()