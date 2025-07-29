from decimal import Decimal, getcontext
import math


getcontext().prec = 18
# Define EPSILON based on the current precision context
# It's set to 10^-(prec-20), ensuring the exponent is at least 1.
_epsilon_exponent = max(1, getcontext().prec - 20)
EPSILON = Decimal("1e-" + str(_epsilon_exponent))
import sys

input = sys.stdin.readline


class Vector:
    def __init__(self, x, y):
        self.x = Decimal(x)
        self.y = Decimal(y)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # 标量乘法
        if isinstance(other, (int, float, Decimal)):
            return Vector(self.x * other, self.y * other)
        raise TypeError("Multiplication is only supported with a scalar.")

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def cross_product(self, other):
        """计算二维叉积 (self x other)。"""
        if not isinstance(other, Vector):
            raise TypeError("Cross product is only supported between two Vectors.")
        return self.x * other.y - self.y * other.x

    def dot_product(self, other):
        """计算二维点积 (self . other)。"""
        if not isinstance(other, Vector):
            raise TypeError("Dot product is only supported between two Vectors.")
        return self.x * other.x + self.y * other.y

    def magnitude(self):
        """计算向量的模长。"""
        return (self.x**2 + self.y**2).sqrt()

    def angle(self, other):
        """计算两个向量之间的夹角（弧度）。"""
        if not isinstance(other, Vector):
            raise TypeError("Angle calculation is only supported between two Vectors.")

        mag_self = self.magnitude()
        mag_other = other.magnitude()

        if mag_self == 0 or mag_other == 0:
            raise ValueError("Cannot calculate angle with a zero vector.")

        dot_prod = self.dot_product(other)
        cos_theta = dot_prod / (mag_self * mag_other)

        cos_theta = max(Decimal("-1"), min(Decimal("1"), cos_theta))

        return Decimal(math.acos(cos_theta))

    def rotate(self, angle):
        """
        将向量绕原点旋转指定角度（弧度）。
        """
        cos_a = Decimal(math.cos(angle))
        sin_a = Decimal(math.sin(angle))
        new_x = self.x * cos_a - self.y * sin_a
        new_y = self.x * sin_a + self.y * cos_a
        return Vector(new_x, new_y)


class Point:
    def __init__(self, x, y):
        self.x = Decimal(x)
        self.y = Decimal(y)

    def __sub__(self, other):
        """两点相减得到一个向量。"""
        if not isinstance(other, Point):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        """点与向量相加得到一个新点。"""
        if not isinstance(other, Vector):
            return NotImplemented
        return Point(self.x + other.x, self.y + other.y)


class Line:
    def __init__(self, p, v):
        self.p = p
        self.v = v

    def intersection(self, other):
        """
        计算两条直线的交点。
        """
        if not isinstance(other, Line):
            raise TypeError("Input other must be a Line.")

        cross_prod_v = self.v.cross_product(other.v)

        if abs(cross_prod_v) < EPSILON:
            if abs((other.p - self.p).cross_product(self.v)) < EPSILON:
                return None
            else:
                return None

        t_numerator = (other.p - self.p).cross_product(other.v)
        t = t_numerator / cross_prod_v
        intersection_point = self.p + self.v * t
        return intersection_point


for _ in range(int(input())):
    x1, y1, x2, y2, x3, y3 = map(Decimal, input().split())
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    p3 = Point(x3, y3)

    v1 = p2 - p1
    v2 = p3 - p2
    v3 = p1 - p3

    ang1 = v1.angle(-v2)
    ang2 = v2.angle(-v3)
    ang3 = v3.angle(-v1)

    nv1_1 = v1.rotate(ang3 / 3)
    nv1_2 = v1.rotate(ang3 * 2 / 3)
    nv2_1 = v2.rotate(ang1 / 3)
    nv2_2 = v2.rotate(ang1 * 2 / 3)
    nv3_1 = v3.rotate(ang2 / 3)
    nv3_2 = v3.rotate(ang2 * 2 / 3)

    l1_1 = Line(p1, nv1_1)
    l1_2 = Line(p1, nv1_2)
    l2_1 = Line(p2, nv2_1)
    l2_2 = Line(p2, nv2_2)
    l3_1 = Line(p3, nv3_1)
    l3_2 = Line(p3, nv3_2)

    rp1 = l1_1.intersection(l2_2)
    rp2 = l2_1.intersection(l3_2)
    rp3 = l3_1.intersection(l1_2)

    print(
        *[
            i.quantize(Decimal("0.000000"))
            for i in [rp2.x, rp2.y, rp3.x, rp3.y, rp1.x, rp1.y]
        ]
    )
