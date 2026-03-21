from engine.components.component import Component

from pyglm import glm

class Transform(Component):
    def __init__(self, position = None, rotation = None, scale = None):
        super().__init__()

        self.position = position if position else glm.vec3(0,0,0)
        self.rotation = rotation if rotation else glm.vec3(0,0,0)
        self.scale = scale if scale else glm.vec3(1,1,1)

    def get_model_matrix(self):
        mat = glm.mat4(1.0)
        mat = glm.translate(mat, self.position)
        mat = glm.rotate(mat, glm.radians(self.rotation.x), glm.vec3(1,0,0))
        mat = glm.rotate(mat, glm.radians(self.rotation.y), glm.vec3(0,1,0))
        mat = glm.rotate(mat, glm.radians(self.rotation.z), glm.vec3(0,0,1))
        mat = glm.scale(mat, self.scale)

        return mat