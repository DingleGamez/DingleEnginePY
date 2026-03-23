from engine.scenes.editor_scene import EditorScene
from engine.listeners.mouse_listener import MouseListener
from engine.listeners.key_listener import KeyListener

import glfw
from OpenGL.GL import *
import time

class Window:
    instance = None

    def __init__(self, width, height, title):
        if hasattr(self, "_initialized"):
            return

        self._initialized = False
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
            cls.instance = super().__new__(cls)
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

        glfw.window_hint(glfw.SAMPLES, 2)
        self.window = glfw.create_window(self.width, self.height, self.title, None, None)

        if not self.window:
            glfw.terminate()
            return

        # glfw.set_input_mode(self.window, glfw.CURSOR, glfw.CURSOR_DISABLED)
        glfw.set_key_callback(self.window, KeyListener().key_callback)
        glfw.set_mouse_button_callback(self.window, MouseListener().mouse_button_callback)
        glfw.set_cursor_pos_callback(self.window, MouseListener().mouse_pos_callback)
        glfw.set_scroll_callback(self.window, MouseListener().mouse_scroll_callback)

        glfw.make_context_current(self.window)
        self.change_scene(0)

    def get_fps(self):
        self.frame_count += 1
        current_time = time.time()
        fps = 0

        if current_time - self.start_time >= 1.0:
            fps = self.frame_count / (current_time - self.start_time)

            self.frame_count = 0
            self.start_time = current_time

    def update(self):
        begin_time = time.time()
        end_time = 0.0
        dt = -1.0

        glViewport(0, 0, self.width, self.height)

        while not glfw.window_should_close(self.window):
            glfw.poll_events()

            if KeyListener().is_key_pressed(glfw.KEY_ESCAPE):
                glfw.set_window_should_close(self.window, True)

            if self.current_scene:
                self.current_scene.update(dt)

            glfw.swap_buffers(self.window)

            end_time = time.time()

            dt = end_time - begin_time
            begin_time = end_time

        glfw.destroy_window(self.window)
        glfw.terminate()
