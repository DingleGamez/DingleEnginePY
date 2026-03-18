from Engine.Render.Scene import Scene
from Engine.Object.GameObject import GameObject
from Components.Transform import Transform
from Components.MeshRenderer import MeshRenderer
from Engine.System.MeshRendererSystem import MeshRendererSystem
from Engine.Render.Camera import Camera
from Engine.Render.Mesh import Mesh

from OpenGL.GL import *
from pyglm import glm
import numpy as np

class EditorScene(Scene):
    def __init__(self):
        super().__init__()
        self.rotation = 0
        self.objects = []
        self.camera = Camera()
        self.renderer = MeshRendererSystem(self.camera, self)

    def start(self):
        glEnable(GL_DEPTH_TEST)

        player = GameObject("Player", Transform())
        player.addComponent(MeshRenderer(Mesh(), "Resources/awesomeface.png"))
        self.objects.append(player)

        player1 = GameObject("Player1", Transform(glm.vec3(-3.0,0.5,1.0), glm.vec3(1.0,1.0,1.0), glm.vec3(0.0,0.0,0.0)))
        player1.addComponent(MeshRenderer(Mesh()))
        self.objects.append(player1)

    def update(self):
        glClearColor(0.25, 0.25, 0.25, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        rotation = self.objects[0].transform.rotation
        rotation1 = self.objects[1].transform.rotation
        rotation.y += 0.1
        rotation1.x += 0.1

        self.renderer.update()