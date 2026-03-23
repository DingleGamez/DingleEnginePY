from engine.entities.camera import Camera
from engine.scenes.scene import Scene
from engine.entities.entity import Entity
from engine.components.model import Model
from engine.render.renderer import Renderer
from engine.listeners.key_listener import KeyListener

import numpy as np
import math
from pyglm import glm
import glfw
import time

class EditorScene(Scene):
    def __init__(self):
        self.camera = Camera()
        self.renderer = Renderer(self.camera, self)

        super().__init__()

    def start(self):
        self.renderer.start()

        model = Entity(0)
        model.transform.position = glm.vec3(0.0, 10.0, 0.0)
        model.transform.scale = glm.vec3(1.0, 1.0, 1.0)

        model.add_component(Model("resources/models/backpack/backpack.obj"))
        self.entities = np.append(self.entities, model)

    def update(self, dt):
        kl = KeyListener()

        cam_velocity = 50.0
        cam_turn_speed = 100.0

        if kl.is_key_pressed(glfw.KEY_W):
            self.camera.position += self.camera.cameraFront * cam_velocity * dt
        if kl.is_key_pressed(glfw.KEY_S):
            self.camera.position -= self.camera.cameraFront * cam_velocity * dt
        if kl.is_key_pressed(glfw.KEY_A):
            self.camera.position -= self.camera.cameraRight * cam_velocity * dt
        if kl.is_key_pressed(glfw.KEY_D):
            self.camera.position += self.camera.cameraRight * cam_velocity * dt

        if kl.is_key_pressed(glfw.KEY_UP):
            self.camera.pitch += cam_turn_speed * dt
        if kl.is_key_pressed(glfw.KEY_DOWN):
            self.camera.pitch -= cam_turn_speed * dt
        if kl.is_key_pressed(glfw.KEY_LEFT):
            self.camera.yaw -= cam_turn_speed * dt
        if kl.is_key_pressed(glfw.KEY_RIGHT):
            self.camera.yaw += cam_turn_speed * dt

        # self.entities[0].transform.rotation.x = -90.0

        self.renderer.update()