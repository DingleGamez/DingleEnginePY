from engine.components.mesh import Mesh
from engine.entities import camera
from engine.render.shader import Shader

from OpenGL.GL import *
from pyglm import glm
import numpy as np

class Renderer:
    def __init__(self, camera, scene):
        self.camera = camera
        self.scene = scene
        self.shader = Shader("engine/shaders/default_shader.glsl")
        self.shader.compile()

    def start(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glFrontFace(GL_CCW)
        glCullFace(GL_BACK)

        self.shader.use()

        projection = self.camera.get_projection_matrix()
        self.shader.upload_mat4("projection", projection)

    def update(self):
        glClearColor(0.25, 0.25, 0.25, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        view = self.camera.get_view_matrix()

        for entity in self.scene.entities:
            mesh = entity.get_component(Mesh)
            model = entity.transform.get_model_matrix()

            self.shader.use()

            glActiveTexture(GL_TEXTURE0)
            mesh.texture.bind()
            self.shader.upload_texture("texSampler", 0)

            self.shader.upload_vec3v("viewPos", self.camera.position)
            self.shader.upload_vec3v("lightPos", glm.vec3(0.0, 1.0, 2.0))
            self.shader.upload_vec3("lightColor", 1.0, 1.0, 1.0)

            self.shader.upload_mat4("model", model)
            self.shader.upload_mat4("view", view)

            glBindVertexArray(mesh.vao)
            glDrawElements(GL_TRIANGLES, len(mesh.indices), GL_UNSIGNED_INT, None)

