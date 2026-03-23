from pyglm import glm
import math

class Camera:
    def __init__(self):
        self.view = glm.mat4(1.0)
        self.projection = glm.mat4(1.0)
        self.position = glm.vec3(0.0, 5.0, 20.0)
        self.yaw, self.pitch, = -90.0, 0.0
        self.cameraFront = glm.vec3(0.0, 0.0, -1.0)
        self.cameraRight = glm.vec3(1.0)
        self.adjust_projection()

    def adjust_projection(self):
        self.projection = glm.perspective(glm.radians(45.0), 1200 / 800, 0.1, 10000.0)

    def get_view_matrix(self):
        front = glm.vec3(0.0)
        front.x = math.cos(glm.radians(self.yaw)) * math.cos(glm.radians(self.pitch))
        front.y = math.sin(glm.radians(self.pitch))
        front.z = math.sin(glm.radians(self.yaw)) * math.cos(glm.radians(self.pitch))

        self.cameraFront = glm.normalize(front)
        self.cameraRight = glm.normalize(glm.cross(front, glm.vec3(0.0, 1.0, 0.0)))

        self.view = glm.lookAt(self.position, self.position + self.cameraFront,
                               glm.vec3(0.0, 1.0, 0.0))

        return self.view

    def get_projection_matrix(self):
        return self.projection