from typing import Optional
import pyray as rl
from poormishaengine.nodes import *

from enum import Enum, auto

from poormishaengine.enginetypes import *
from poormishaengine.resources import *
from pyray import Vector2

class PoorEngine:


    def __init__(self, width: int, height: int, title: str):
        self.width = width
        self.height = height
        self.title = title
        self.paused = False
        self.rendering_engine = RenderingEngine(width, height)
        
        self.bg_color = rl.RAYWHITE
        self.input_actions = InputActions()
        self.processes = {}
        
        # Set window properties
        rl.set_config_flags(rl.ConfigFlags.FLAG_WINDOW_RESIZABLE)
        rl.init_window(self.width, self.height, self.title)
        
        # Define screen width and height

        
        # Set target FPS
        rl.set_target_fps(60)
    
    def run(self):
        while not rl.window_should_close():
            rl.begin_drawing()

            self.screen_width = rl.get_screen_width()
            self.screen_height = rl.get_screen_height()
            rl.clear_background(self.bg_color)
            for proc in self.processes.values():
                if proc["mode"] == ProcessMode.DEFAULT:
                    if not self.paused:
                        proc["func"]()
                elif proc["mode"] == ProcessMode.WHEN_PAUSED:
                    if self.paused:
                        proc["func"]()
                elif proc["mode"] == ProcessMode.ALWAYS:
                    proc["func"]()
                
            rl.end_drawing()

        rl.close_window()
    def process(self, name=None, mode=ProcessMode.DEFAULT):
        def decorator(func):
            cmd_name = name or func.__name__
            self.processes[cmd_name] = {"func": func, "mode": mode}
            return func
        return decorator

    def drawing(self, name=None):
        def decorator(func):
            cmd_name = name or func.__name__
            self.processes[cmd_name] = {"func": func, "mode": ProcessMode.ALWAYS}
            return func
        return decorator

class RenderingEngine:
    def __init__(self, width: int, height: int):
        self.default_font: rl.Font = rl.load_font("resources/fonts/CascadiaMono-Medium.ttf")
        self.width = width
        self.height = height

    def draw(self):
        pass  # Implement your drawing logic here
    def draw_text(self, text: str, pos: rl.Vector2, font_size: float, color: rl.Color, font: rl.Font = None):
        if font == None:
            font = self.default_font
        rl.draw_text_ex(font, text, pos, font_size,0 , color)

    def draw_line(self, start: rl.Vector2, end: rl.Vector2, color: rl.Color):
        rl.draw_line(int(start.x), int(start.y), int(end.x), int(end.y), color)

    def draw_rect(self, rect: rl.Rectangle, color: rl.Color):
        rl.draw_rectangle_rec(rect, color)

    def draw_circle(self, center: Vector2, radius: float, color: rl.Color):
        rl.draw_circle(int(center.x), int(center.y), int(radius), color)
    def draw_texture(self, texture: rl.Texture2D, position: Vector2, color: rl.Color = rl.WHITE):
        rl.draw_texture(texture, int(position.x), int(position.y), color)

    def draw_texture_rec(self, texture: rl.Texture2D, source_rec: rl.Rectangle, position: Vector2, color: rl.Color = rl.WHITE):
        rl.draw_texture_rec(texture, source_rec, position, color)

class InputActions:
    def __init__(self):
        self.actions = {}

    def bind_action(self, action_name: str, keys: list[int]):
    
        self.actions[action_name] = keys

    def is_action_pressed(self, action_name: str) -> bool:
     
        if action_name in self.actions:
            return any(rl.is_key_down(key) for key in self.actions[action_name])
        return False

    def is_action_just_pressed(self, action_name: str) -> bool:
       
        if action_name in self.actions:
            return any(rl.is_key_pressed(key) for key in self.actions[action_name])
        return False

    def is_action_just_released(self, action_name: str) -> bool:
       
        if action_name in self.actions:
            return any(rl.is_key_released(key) for key in self.actions[action_name])
        return False

