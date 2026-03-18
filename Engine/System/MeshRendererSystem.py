from Engine.Render.Shader import Shader
from Components.Transform import Transform
from Components.MeshRenderer import MeshRenderer

from OpenGL.GL import *
from pyglm import glm

class MeshRendererSystem:
    def __init__(self, camera, scene):
        self.camera = camera
        self.scene = scene

    def update(self):
        objects = self.scene.objects

        for object in objects:
            renderer = object.getComponent(MeshRenderer)
            transform = object.transform

            model = transform.getModelMatrix()
            view = self.camera.getViewMatrix()
            projection = self.camera.getProjectionMatrix()
            shader = renderer.shader

            shader.use()

            glActiveTexture(GL_TEXTURE0)
            renderer.texture.bind()
            shader.uploadTexture("texSampler", 0)

            shader.uploadMat4("model", glm.value_ptr(model))
            shader.uploadMat4("view", glm.value_ptr(view))
            shader.uploadMat4("projection", glm.value_ptr(projection))

            renderer.mesh.draw()