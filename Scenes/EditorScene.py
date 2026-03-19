from Engine.Render.Scene import Scene
from Engine.Object.GameObject import GameObject
from Components.Transform import Transform
from Components.MeshRenderer import MeshRenderer
from Engine.System.Renderer import Renderer
from Engine.Render.Camera import Camera
from Engine.Render.Mesh import Mesh

from OpenGL.GL import *
from pyglm import glm
import numpy as np
import math
import time

class EditorScene(Scene):
    def __init__(self):
        super().__init__()
        self.rotation = 0
        self.objects = []
        self.camera = Camera()
        self.renderer = Renderer(self.camera, self)
        self.start_time = time.time()
        self.frame_count = 0

    def start(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glFrontFace(GL_CW)
        glCullFace(GL_FRONT)

        for i in range(-1, 1):
            for j in range(-1, 1):
                for v in range(-1, 1):
                    cube = GameObject(f"cube{i + 5}",
                    Transform(glm.vec3(i, j, v), glm.vec3(1.0, 1.0, 1.0), glm.vec3((i * j * v) * 15, 0.0, 0.0)))
                    cube.addComponent(MeshRenderer(Mesh(), "Resources/awesomeface.png"))

                    self.objects.append(cube)

    def DrawFPS(self):
        self.frame_count += 1
        current_time = time.time()

        if current_time - self.start_time >= 1.0:
            fps = self.frame_count / (current_time - self.start_time)
            print(f"FPS: {fps:.2f}")

            frame_count = 0
            start_time = current_time

    def update(self):
        # self.DrawFPS()
        glClearColor(0.25, 0.25, 0.25, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for i in range(len(self.objects)):
            object = self.objects[i]
            rotation = object.transform.rotation
            rotation.x += 0.1

            # position = object.transform.position
            # position.z = math.sin((i * 25) - time.time())

        self.renderer.update()