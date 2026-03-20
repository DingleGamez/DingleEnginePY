from Engine.Render.Shader import Shader
from Engine.Components.Mesh import Mesh

from OpenGL.GL import *
from pyglm import glm

class Renderer:
    def __init__(self, camera, scene):
        self.camera = camera
        self.scene = scene
        self.shader = Shader()
        self.shader.compile(None, None)

        self.start()

    def start(self):
        self.shader.use()

        projection = self.camera.getProjectionMatrix()
        self.shader.uploadMat4("projection", glm.value_ptr(projection))

    def update(self):
        objects = self.scene.objects
        for object in objects:
            mesh = object.getComponent(Mesh)
            transform = object.transform
            model = transform.getModelMatrix()
            view = self.camera.getViewMatrix()
            projection = self.camera.getProjectionMatrix()

            self.shader.use()

            glActiveTexture(GL_TEXTURE0)
            mesh.texture.bind()
            self.shader.uploadTexture("texSampler", 0)

            self.shader.uploadMat4("model", glm.value_ptr(model))
            self.shader.uploadMat4("view", glm.value_ptr(view))

            glBindVertexArray(mesh.VAO)

            glDrawElements(
                GL_TRIANGLES,
                len(mesh.indices),
                GL_UNSIGNED_INT,
                None
            )

            glBindVertexArray(0)