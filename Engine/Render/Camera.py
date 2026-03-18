from pyglm import glm

class Camera:
    def __init__(self):
        self.view = glm.mat4(1.0)
        self.projection = glm.mat4(1.0)
        self.position = glm.vec3(0, 0, 0)
        self.adjustProjection()

    def adjustProjection(self):
        self.projection = glm.perspective(glm.radians(45.0), 1200 / 800, 0.1, 1000.0)

    def getViewMatrix(self):
        self.view = glm.lookAt(glm.vec3(self.position.x, self.position.y, 10.0), self.position, glm.vec3(0.0, 1.0, 0.0))

        return self.view

    def getProjectionMatrix(self):
        return self.projection