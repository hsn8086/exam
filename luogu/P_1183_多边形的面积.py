from dataclasses import dataclass
from decimal import Decimal, getcontext
from enum import Enum, auto

getcontext().prec = 100


class PointLinePosition(Enum):
    ABOVE = auto()  # 上方
    ON_LINE = auto()  # 在直线上
    BELOW = auto()  # 下方

    def __str__(self):
        # 如果需要，用于用户友好的打印，将枚举成员映射到中文字符串
        if self == PointLinePosition.ABOVE:
            return "above"
        elif self == PointLinePosition.ON_LINE:
            return "on line"
        elif self == PointLinePosition.BELOW:
            return "below"
        return super().__str__()


@dataclass
class Vector:
    x: Decimal
    y: Decimal

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # 标量乘法
        if isinstance(other, (int, float, Decimal)):
            return Vector(self.x * other, self.y * other)
        raise TypeError("Multiplication is only supported with a scalar.")

    def __truediv__(self, other):  # 标量除法
        if isinstance(other, (int, float, Decimal)):
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

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def cross_product(self, other: "Vector") -> Decimal:
        """计算二维叉积 (self x other)。"""
        if not isinstance(other, Vector):
            raise TypeError("Cross product is only supported between two Vectors.")
        return self.x * other.y - self.y * other.x


@dataclass
class Point:
    x: Decimal
    y: Decimal

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


@dataclass
class Line:
    p: Point  # 直线上的一点
    v: Vector  # 直线的方向向量

    def get_point_side(self, q: Point) -> PointLinePosition:
        """
        使用枚举确定点 Q 位于直线的哪一侧。
        P 是 self.p (直线上的一个点)，v 是 self.v (方向向量)。
        计算 PQ_vector x v。
        - 负数：Q 在直线的“上方”(PointLinePosition.ABOVE)。
        - 零：Q 在直线上 (PointLinePosition.ON_LINE)。
        - 正数：Q 在直线的“下方”(PointLinePosition.BELOW)。
        （注意：“上方”和“下方”取决于 v 的方向和坐标系。
         此处遵循提示的约定。）
        """
        if not isinstance(q, Point):
            raise TypeError("Input q must be a Point.")

        pq_vector = q - self.p  # 从 P (在直线上) 到 Q 的向量

        cross_prod_val = pq_vector.cross_product(self.v)

        # 对于 Decimal 类型，使用一个小的 epsilon 进行浮点数比较
        # 对于 Decimal，除非精度问题极端，否则通常可以直接与 0 比较。

        if cross_prod_val < 0:
            return PointLinePosition.ABOVE
        elif cross_prod_val == 0:
            return PointLinePosition.ON_LINE
        else:  # cross_prod_val > 0 (叉积为正)
            return PointLinePosition.BELOW


@dataclass
class Polygon:
    points: list[Point]  # 多边形的顶点列表

    def area(self) -> Decimal:
        """计算多边形的面积。"""
        n = len(self.points)
        if n < 3:
            return Decimal(0)  # 少于3个点无法形成多边形

        area = Decimal(0)
        # 使用鞋带公式 (Shoelace formula)
        # 面积 = 0.5 * |(x1*y2 + x2*y3 + ... + xn*y1) - (y1*x2 + y2*x3 + ... + yn*x1)|
        for i in range(n):
            p1 = self.points[i]
            p2 = self.points[(i + 1) % n]  # 循环到第一个点

            area += p1.x * p2.y
            area -= p1.y * p2.x

        return abs(area) / Decimal(2)

    def is_convex(self) -> bool:
        """
        检查多边形是否为凸多边形。
        对于凸多边形，连续边的叉积方向应该一致（全部非负或全部非正）。
        假设顶点按顺时针或逆时针顺序给出。
        """
        n = len(self.points)
        if n < 3:
            # 一个点或两个点不能形成多边形，但如果非要说，它们是“凸”的
            return True

        # 计算第一个叉积以确定期望的方向
        v1 = self.points[1] - self.points[0]
        v2 = self.points[2] - self.points[1]
        first_cross_product = v1.cross_product(v2)

        # 遍历所有连续的边，检查叉积方向
        for i in range(n):
            p1 = self.points[i]
            p2 = self.points[(i + 1) % n]
            p3 = self.points[(i + 2) % n]

            vec1 = p2 - p1
            vec2 = p3 - p2

            current_cross_product = vec1.cross_product(vec2)

            # 如果第一个叉积是正的，所有后续叉积必须是非负的
            # 如果第一个叉积是负的，所有后续叉积必须是非正的
            # 如果第一个叉积是零，则后续叉积必须与后续非零叉积方向一致
            if first_cross_product > 0 and current_cross_product < 0:
                return False
            if first_cross_product < 0 and current_cross_product > 0:
                return False
            # 如果第一个叉积是零，并且当前叉积非零，更新期望方向
            if first_cross_product == 0 and current_cross_product != 0:
                first_cross_product = current_cross_product
        return True


p_lst = []
for _ in range(int(input())):
    p_lst.append(Point(*map(Decimal, input().split())))

pg = Polygon(p_lst)
print(pg.area().quantize(Decimal("0.")))
