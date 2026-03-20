from OpenGL.raw.GL.VERSION.GL_1_0 import glViewport

from Engine.Scenes.EditorScene import EditorScene

import glfw

class Window:
    _instance = None

    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title
        self.window = None
        self.currentScene = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Window, cls).__new__(cls)
        return cls._instance

    def run(self):
        self.init()
        self.loop()

    def changeScene(self, scene):
        if scene == 0:
            self.currentScene = EditorScene()
            self.currentScene.start()

    def getScene(self):
        return self.currentScene

    def init(self):
        glfw.init()

        self.window = glfw.create_window(self.width, self.height, self.title, None, None)

        if not self.window:
            glfw.terminate()
            return

        glfw.make_context_current(self.window)
        self.changeScene(0)

    def loop(self):
        glViewport(0, 0, self.width, self.height)
        while not glfw.window_should_close(self.window):
            if self.currentScene:
                self.currentScene.update()

            glfw.swap_buffers(self.window)
            glfw.poll_events()
        glfw.destroy_window(self.window)
        glfw.terminate()
