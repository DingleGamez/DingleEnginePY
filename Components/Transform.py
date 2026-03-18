from Engine.Object.Component import Component

from pyglm import glm

class Transform(Component):
    def __init__(self, position=None, scale=None, rotation=None):
        super().__init__()

        self.position = position if position else glm.vec3(0, 0, 0)
        self.scale = scale if scale else glm.vec3(1, 1, 1)
        self.rotation = rotation if rotation else glm.vec3(0, 0, 0)

    def getModelMatrix(self):
        model = glm.mat4(1.0)

        model = glm.translate(model, self.position)

        model = glm.rotate(model, glm.radians(self.rotation.x), glm.vec3(1,0,0))
        model = glm.rotate(model, glm.radians(self.rotation.y), glm.vec3(0,1,0))
        model = glm.rotate(model, glm.radians(self.rotation.z), glm.vec3(0,0,1))

        model = glm.scale(model, self.scale)

        return model