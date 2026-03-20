from Engine.Render.Scene import Scene
from Engine.Render.GameObject import GameObject
from Engine.Components.Transform import Transform
from Engine.Components.Mesh import Mesh
from Engine.System.Renderer import Renderer
from Engine.Render.Camera import Camera

from OpenGL.GL import *
from pyglm import glm
import numpy as np
import time

class EditorScene(Scene):
    def __init__(self):
        super().__init__()
        self.rotation = 0
        self.objects = np.array([], dtype=GameObject)
        self.camera = Camera()
        self.renderer = Renderer(self.camera, self)
        self.startTime = time.time()
        self.frameCount = 0

    def start(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glFrontFace(GL_CW)
        glCullFace(GL_FRONT)

        amount = 1
        for x in range(-amount, amount):
            for y in range(-amount, amount):
                for z in range(-amount, amount):
                    model = GameObject(f"model",
                    Transform(glm.vec3(x, y, z), glm.vec3(1.0, 1.0, 1.0), glm.vec3(0.0, 0.0, 0.0)))
                    model.addComponent(Mesh("Engine/Resources/Textures/awesomeface.png"))
                    self.objects = np.append(self.objects, model)

    def DrawFPS(self):
        self.frameCount += 1
        currentTime = time.time()

        if currentTime - self.startTime >= 1.0:
            fps = self.frameCount / (currentTime - self.startTime)
            print(f"FPS: {fps:.2f}")

            self.frameCount = 0
            self.startTime = currentTime

    def update(self):
        self.DrawFPS()
        glClearColor(0.25, 0.25, 0.25, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for i in range(len(self.objects)):
            object = self.objects[i]
            rotation = object.transform.rotation
            rotation += 0.1

            # position = object.transform.position
            # position.z = math.sin((i * 25) - time.time())

        self.renderer.update()