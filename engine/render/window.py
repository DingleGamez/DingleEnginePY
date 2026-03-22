from engine.scenes.editor_scene import EditorScene

import imgui
from imgui.integrations.glfw import GlfwRenderer
import glfw
from OpenGL.GL import *
import time

class Window:
    instance = None

    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title
        self.window = None
        self.current_scene = None
        self.impl = None
        self.start_time = time.time()
        self.frame_count = 0

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

        imgui.create_context()
        self.impl = GlfwRenderer(self.window)

    def get_fps(self):
        self.frame_count += 1
        current_time = time.time()
        fps = 0

        if current_time - self.start_time >= 1.0:
            fps = self.frame_count / (current_time - self.start_time)

            self.frame_count = 0
            self.start_time = current_time

    def update(self):
        glViewport(0, 0, self.width, self.height)

        fps = 0.0
        wire_toggle = False

        while not glfw.window_should_close(self.window):
            if self.current_scene:
                self.current_scene.update()

            self.frame_count += 1
            current_time = time.time()

            if current_time - self.start_time >= 1.0:
                fps = self.frame_count / (current_time - self.start_time)

                self.frame_count = 0
                self.start_time = current_time

            self.impl.process_inputs()

            imgui.new_frame()

            imgui.begin("Settings")

            imgui.text(f"FPS: {str(fps)}")
            if imgui.button("Wireframe"):
                wire_toggle = not wire_toggle

            imgui.end()

            if wire_toggle:
                glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
                # glPolygonMode(GL_FRONT_AND_BACK, GL_POINT)
            else:
                glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

            imgui.render()
            self.impl.render(imgui.get_draw_data())
            glfw.swap_buffers(self.window)
            glfw.poll_events()

        glfw.destroy_window(self.window)
        glfw.terminate()
