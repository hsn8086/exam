import sys
from math import atan2, sqrt
from dataclasses import dataclass

from enum import Enum, auto
import math


EPSILON = 10 ** (-16)


@dataclass
class Vector:
    x: float
    y: float

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (int, float, float)):
            return Vector(self.x * other, self.y * other)
        raise TypeError("Multiplication is only supported with a scalar.")

    def __truediv__(self, other):
        if isinstance(other, (int, float, float)):
            if other == 0:
                raise ZeroDivisionError("Cannot divide vector by zero.")
            return Vector(self.x / other, self.y / other)
        raise TypeError("Division is only supported by a scalar.")

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other: "Vector"):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def cross_product(self, other: "Vector") -> float:
        """计算二维叉积 (self x other)"""
        if not isinstance(other, Vector):
            raise TypeError("Cross product is only supported between two Vectors.")
        return self.x * other.y - self.y * other.x

    def dot_product(self, other: "Vector") -> float:
        """计算二维点积 (self . other)"""
        if not isinstance(other, Vector):
            raise TypeError("Dot product is only supported between two Vectors.")
        return self.x * other.x + self.y * other.y

    def magnitude(self) -> float:
        """计算向量的模长"""
        return sqrt(self.x**2 + self.y**2)

    def normalized(self) -> "Vector":
        """返回单位向量"""
        magnitude = self.magnitude()
        if magnitude == 0:
            raise ZeroDivisionError("Cannot normalize a zero vector.")
        return Vector(self.x / magnitude, self.y / magnitude)

    def angle(self, other: "Vector") -> float:
        """计算两个向量之间的夹角 (弧度)"""
        if not isinstance(other, Vector):
            raise TypeError("Angle calculation is only supported between two Vectors.")

        mag_self = self.magnitude()
        mag_other = other.magnitude()

        if mag_self == 0 or mag_other == 0:
            raise ValueError("Cannot calculate angle with a zero vector.")

        dot_prod = self.dot_product(other)
        cos_theta = dot_prod / (mag_self * mag_other)

        cos_theta = max(float("-1"), min(float("1"), cos_theta))

        return float(math.acos(cos_theta))

    def angle_signed(self, other: "Vector") -> float:
        """
        计算从 self 到 other 的有向夹角 (弧度)
        """
        if not isinstance(other, Vector):
            raise TypeError(
                "Signed angle calculation is only supported between two Vectors."
            )

        mag_self = self.magnitude()
        mag_other = other.magnitude()

        if mag_self == 0 or mag_other == 0:
            raise ValueError("Cannot calculate signed angle with a zero vector.")

        cross_prod = self.cross_product(other)
        dot_prod = self.dot_product(other)

        if abs(dot_prod) < EPSILON and abs(cross_prod) < EPSILON:
            raise ValueError("Cannot calculate angle with a zero vector.")

        if abs(dot_prod) < EPSILON:
            if cross_prod > 0:
                return PI / 2
            elif cross_prod < 0:
                return -PI / 2
            else:
                return float(0)
        else:
            angle_val = float(math.atan(cross_prod / dot_prod))
            if dot_prod < 0:
                if cross_prod >= 0:
                    angle_val += PI
                else:
                    angle_val -= PI
            return angle_val

    def __abs__(self) -> float:
        return self.magnitude()

    def rotate(self, angle: float) -> "Vector":
        """
        将向量绕原点旋转指定角度 (弧度)
        """
        cos_a = float(math.cos(angle))
        sin_a = float(math.sin(angle))
        new_x = self.x * cos_a - self.y * sin_a
        new_y = self.x * sin_a + self.y * cos_a
        return Vector(new_x, new_y)


@dataclass
class Point:
    x: float
    y: float

    def __sub__(self, other: "Point") -> Vector:
        """两点相减得到一个向量。"""
        if not isinstance(other, Point):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __add__(self, other: Vector) -> "Point":
        """点与向量相加得到一个新点。"""
        if not isinstance(other, Vector):
            return NotImplemented
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other: "Point") -> bool:
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"


@dataclass
class Polygon:
    points: list[Point]

    def area(self) -> float:
        """计算多边形的面积"""
        n = len(self.points)
        if n < 3:
            return float(0)

        area = float(0)

        for i in range(n):
            p1 = self.points[i]
            p2 = self.points[(i + 1) % n]

            area += p1.x * p2.y
            area -= p1.y * p2.x

        return abs(area) / float(2)

    def is_convex(self) -> bool:
        """
        检查多边形是否为凸多边形
        """
        n = len(self.points)
        if n < 3:
            return True

        v1 = self.points[1] - self.points[0]
        v2 = self.points[2] - self.points[1]
        first_cross_product = v1.cross_product(v2)

        for i in range(n):
            p1 = self.points[i]
            p2 = self.points[(i + 1) % n]
            p3 = self.points[(i + 2) % n]

            vec1 = p2 - p1
            vec2 = p3 - p2

            current_cross_product = vec1.cross_product(vec2)

            if first_cross_product > 0 and current_cross_product < 0:
                return False
            if first_cross_product < 0 and current_cross_product > 0:
                return False

            if first_cross_product == 0 and current_cross_product != 0:
                first_cross_product = current_cross_product
        return True

    def __contains__(self, point: Point) -> bool:
        """
        检查点是否在多边形内，包括边界和顶点
        """
        if not isinstance(point, Point):
            raise TypeError("Input point must be a Point.")

        n = len(self.points)
        if n < 3:
            return False

        crossings = 0
        for i in range(n):
            p1 = self.points[i]
            p2 = self.points[(i + 1) % n]

            if (p1.y <= point.y < p2.y) or (p2.y <= point.y < p1.y):
                x_at_y = p1.x + (point.y - p1.y) * (p2.x - p1.x) / (p2.y - p1.y)
                if point.x < x_at_y:
                    crossings += 1

        return crossings % 2 == 1


PI = 3.14159265358979323846264338327950288
for _ in range(int(input())):
    n, px, py = map(int, input().split())
    pts_max = []
    max_d = 0
    pts_min = []
    min_d = 1 << 70
    pts = []
    for i in range(n):
        x, y = map(int, input().split())
        pts.append(Point(x, y))
        d = (x - px) ** 2 + (y - py) ** 2
        if d > max_d:
            pts_max = [(x - px, y - py)]
            max_d = d
        elif d == max_d:
            pts_max.append((x - px, y - py))

        if d < min_d:
            pts_min = [(x - px, y - py, i)]
            min_d = d
        elif d == min_d:
            pts_min.append((x - px, y - py, i))
    p = Polygon(pts)
    degrees_far = []
    for x, y in pts_max:
        degrees_far.append(atan2(y, x))
    degrees_far.sort()
    degrees_far += list(map(lambda x: x + 2 * PI, degrees_far))
    ans = 0

    if Point(px, py) not in p and pts_min:
        # check
        flag = False
        pts_min.sort(key=lambda t: t[2])
        x1, y1, i1 = pts_min[0]
        pts_min.append((x1, y1, pts_min[-1][2] + 1))

        tmp = []
        for a, b in zip(pts_min[:-1], pts_min[1:]):
            ax, ay, ai = a
            bx, by, bi = b
            if bi - ai == 1:
                flag = True

            if flag and bi - ai == 1:
                tmp.append(((ax + bx) / 2, (ay + by) / 2, 0))
        if tmp:
            pts_min = tmp

        degrees_near = []
        for x, y, i in pts_min:
            degrees_near.append(atan2(y, x))
        degrees_near.sort()
        degrees_near += list(map(lambda x: x + 2 * PI, degrees_near))
        for deg1, deg2 in zip(degrees_near[:-1], degrees_near[1:]):
            ans = max(deg2 - deg1, ans)

    for deg1, deg2 in zip(degrees_far[:-1], degrees_far[1:]):
        ans = max(deg2 - deg1, ans)

    print("%.32f" % ans)
