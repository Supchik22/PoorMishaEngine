from enum import Enum, auto
import math



class ProcessMode(Enum):
    DEFAULT = auto()
    WHEN_PAUSED = auto()
    ALWAYS = auto()


import math

# class Vector2:
#     def __init__(self, x: float = 0.0, y: float = 0.0):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Vector2(self.x + other.x, self.y + other.y)

#     def __sub__(self, other):
#         return Vector2(self.x - other.x, self.y - other.y)

#     def __mul__(self, scalar: float):
#         return Vector2(self.x * scalar, self.y * scalar)

#     def __truediv__(self, scalar: float):
#         return Vector2(self.x / scalar, self.y / scalar)

#     def length(self):
#         return math.hypot(self.x, self.y)

#     def length_squared(self):
#         return self.x ** 2 + self.y ** 2

#     def normalized(self):
#         l = self.length()
#         if l == 0:
#             return Vector2()
#         return self / l

#     def dot(self, other):
#         return self.x * other.x + self.y * other.y

#     def angle_to(self, other):
#         dot = self.dot(other)
#         len_product = self.length() * other.length()
#         if len_product == 0:
#             return 0
#         return math.acos(max(min(dot / len_product, 1), -1))

#     def angle(self):
#         return math.atan2(self.y, self.x)

#     def rotated(self, angle_radians):
#         cos_a = math.cos(angle_radians)
#         sin_a = math.sin(angle_radians)
#         return Vector2(
#             self.x * cos_a - self.y * sin_a,
#             self.x * sin_a + self.y * cos_a
#         )

#     def distance_to(self, other):
#         return (self - other).length()

#     def distance_squared_to(self, other):
#         return (self - other).length_squared()

#     def floor(self):
#         return Vector2(math.floor(self.x), math.floor(self.y))

#     def ceil(self):
#         return Vector2(math.ceil(self.x), math.ceil(self.y))

#     def snapped(self, step):
#         return Vector2(
#             round(self.x / step.x) * step.x,
#             round(self.y / step.y) * step.y
#         )

#     def lerp(self, other, t: float):
#         return self + (other - self) * t

#     def clamp(self, min_vec, max_vec):
#         return Vector2(
#             max(min(self.x, max_vec.x), min_vec.x),
#             max(min(self.y, max_vec.y), min_vec.y)
#         )

#     def to_vector2i(self):
#         return Vector2i(int(self.x), int(self.y))

#     def __repr__(self):
#         return f"Vector2({self.x}, {self.y})"

#     def __eq__(self, other):
#         return isinstance(other, Vector2) and self.x == other.x and self.y == other.y


# class Vector2i:
#     def __init__(self, x: int = 0, y: int = 0):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Vector2i(self.x + other.x, self.y + other.y)

#     def __sub__(self, other):
#         return Vector2i(self.x - other.x, self.y - other.y)

#     def __mul__(self, scalar: float):
#         return Vector2i(int(self.x * scalar), int(self.y * scalar))

#     def __truediv__(self, scalar: float):
#         return Vector2i(int(self.x / scalar), int(self.y / scalar))

#     def length(self):
#         return math.hypot(self.x, self.y)

#     def length_squared(self):
#         return self.x ** 2 + self.y ** 2

#     def normalized(self):
#         l = self.length()
#         if l == 0:
#             return Vector2i()
#         return Vector2i(int(self.x / l), int(self.y / l))

#     def floor(self):
#         return Vector2i(math.floor(self.x), math.floor(self.y))

#     def ceil(self):
#         return Vector2i(math.ceil(self.x), math.ceil(self.y))

#     def snapped(self, step):
#         return Vector2i(
#             round(self.x / step.x) * step.x,
#             round(self.y / step.y) * step.y
#         )

#     def clamp(self, min_vec, max_vec):
#         return Vector2i(
#             max(min(self.x, max_vec.x), min_vec.x),
#             max(min(self.y, max_vec.y), min_vec.y)
#         )

#     def to_vector2(self):
#         return Vector2(float(self.x), float(self.y))

#     def __repr__(self):
#         return f"Vector2i({self.x}, {self.y})"

#     def __eq__(self, other):
#         return isinstance(other, Vector2i) and self.x == other.x and self.y == other.y


# Vector2.ZERO = Vector2(0, 0)
# Vector2.ONE = Vector2(1, 1)
# Vector2.UP = Vector2(0, -1)
# Vector2.DOWN = Vector2(0, 1)
# Vector2.LEFT = Vector2(-1, 0)
# Vector2.RIGHT = Vector2(1, 0)

# Vector2i.ZERO = Vector2i(0, 0)
# Vector2i.ONE = Vector2i(1, 1)
# Vector2i.UP = Vector2i(0, -1)
# Vector2i.DOWN = Vector2i(0, 1)
# Vector2i.LEFT = Vector2i(-1, 0)
# Vector2i.RIGHT = Vector2i(1, 0)