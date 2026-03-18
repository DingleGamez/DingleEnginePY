from Engine.Object.Component import Component
from Engine.Render.Shader import Shader
from Engine.Render.Texture import Texture

from OpenGL.GL import *
from pyglm import glm

class MeshRenderer(Component):
    def __init__(self, mesh, texPath=None):
        super().__init__()
        self.mesh = mesh
        self.shader = Shader()
        self.texture = Texture()

        self.texture.init(texPath)

        self.shader.compile()