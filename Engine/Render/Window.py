from engine.scenes.editor_scene import EditorScene

import glfw
from OpenGL.GL import *

class Window:
    instance = None

    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title
        self.window = None
        self.current_scene = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(Window, cls).__new__(cls)
        return cls.instance

    def change_scene(self, scene):
        if scene == 0:
            self.current_scene = EditorScene()
            self.current_scene.start()

    def run(self):
        self.start()
        self.update()

    def start(self):
        glfw.init()

        self.window = glfw.create_window(self.width, self.height, self.title, None, None)

        if not self.window:
            glfw.terminate()
            return

        glfw.make_context_current(self.window)
        self.change_scene(0)

    def update(self):
        glViewport(0, 0, self.width, self.height)
        while not glfw.window_should_close(self.window):
            if self.current_scene:
                self.current_scene.update()

            glfw.swap_buffers(self.window)
            glfw.poll_events()
        glfw.destroy_window(self.window)
        glfw.terminate()
