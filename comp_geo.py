from dataclasses import dataclass
from decimal import Decimal, getcontext
from enum import Enum, auto
import math
from typing import Self

getcontext().prec = 28
PI = Decimal(314159265_358979323846264_338327950288_419716939937510) / Decimal(10**50)
# Define EPSILON based on the current precision context
# It's set to 10^-(prec-20), ensuring the exponent is at least 1.
_epsilon_exponent = max(1, getcontext().prec - 20)
EPSILON = Decimal("1e-" + str(_epsilon_exponent))


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

    def __eq__(self, other: Self):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def cross_product(self, other: Self) -> Decimal:
        """计算二维叉积 (self x other)。"""
        if not isinstance(other, Vector):
            raise TypeError("Cross product is only supported between two Vectors.")
        return self.x * other.y - self.y * other.x

    def dot_product(self, other: Self) -> Decimal:
        """计算二维点积 (self . other)。"""
        if not isinstance(other, Vector):
            raise TypeError("Dot product is only supported between two Vectors.")
        return self.x * other.x + self.y * other.y

    def magnitude(self) -> Decimal:
        """计算向量的模长。"""
        return (self.x**2 + self.y**2).sqrt()

    def normalized(self) -> Self:
        """返回单位向量。"""
        magnitude = self.magnitude()
        if magnitude == 0:
            raise ZeroDivisionError("Cannot normalize a zero vector.")
        return Vector(self.x / magnitude, self.y / magnitude)

    def angle(self, other: Self) -> Decimal:
        """计算两个向量之间的夹角（弧度）。"""
        if not isinstance(other, Vector):
            raise TypeError("Angle calculation is only supported between two Vectors.")

        mag_self = self.magnitude()
        mag_other = other.magnitude()

        if mag_self == 0 or mag_other == 0:
            # 零向量没有明确的方向，夹角未定义
            raise ValueError("Cannot calculate angle with a zero vector.")

        # 使用点积公式: a . b = |a| |b| cos(theta)
        # cos(theta) = (a . b) / (|a| |b|)
        dot_prod = self.dot_product(other)
        cos_theta = dot_prod / (mag_self * mag_other)

        # 由于浮点精度问题，cos_theta 可能略微超出 [-1, 1] 范围
        # 限制其范围以避免 ACOS 错误
        cos_theta = max(Decimal("-1"), min(Decimal("1"), cos_theta))

        # 返回弧度
        return Decimal(math.acos(cos_theta))

    def angle_signed(self, other: Self) -> Decimal:
        """
        计算从 self 到 other 的有向夹角（弧度）。
        使用叉积确定方向。
        """
        if not isinstance(other, Vector):
            raise TypeError(
                "Signed angle calculation is only supported between two Vectors."
            )

        mag_self = self.magnitude()
        mag_other = other.magnitude()

        if mag_self == 0 or mag_other == 0:
            raise ValueError("Cannot calculate signed angle with a zero vector.")

        # 使用 atan2(cross_product, dot_product)
        # atan2(y, x) 返回点 (x, y) 到原点的向量与正 x 轴之间的夹角
        # 这里的 y 是叉积 (self x other)，x 是点积 (self . other)
        # 叉积的符号表示方向
        cross_prod = self.cross_product(other)
        dot_prod = self.dot_product(other)

        # Decimal 没有 atan2，需要手动计算
        # angle =
        # Use Decimal's atan2 method if available, or implement it
        # A common way to implement atan2(y, x) for Decimal:
        # If x > 0, atan(y/x)
        # If x < 0, atan(y/x) + pi (if y >= 0), atan(y/x) - pi (if y < 0)
        # If x = 0, pi/2 (if y > 0), -pi/2 (if y < 0), 0 (if y = 0)

        # Handle the case where both dot_prod and cross_prod are zero (zero vector)
        if abs(dot_prod) < EPSILON and abs(cross_prod) < EPSILON:
            raise ValueError("Cannot calculate angle with a zero vector.")

        if abs(dot_prod) < EPSILON:  # x is close to zero
            if cross_prod > 0:
                return PI / 2
            elif cross_prod < 0:
                return -PI / 2
            else:  # Should be caught by the zero vector check
                return Decimal(0)
        else:
            angle_val = Decimal(math.atan(cross_prod / dot_prod))
            if dot_prod < 0:  # x is negative
                if cross_prod >= 0:
                    angle_val += PI
                else:
                    angle_val -= PI
            return angle_val

    def __abs__(self) -> Decimal:
        return self.Magnitude()

    def rotate(self, angle: Decimal) -> Self:
        """
        将向量绕原点旋转指定角度（弧度）。
        使用旋转矩阵:
        [ cos(angle)  -sin(angle) ] [ x ] = [ x*cos(angle) - y*sin(angle) ]
        [ sin(angle)   cos(angle) ] [ y ]   [ x*sin(angle) + y*cos(angle) ]
        """
        cos_a = Decimal(math.cos(angle))
        sin_a = Decimal(math.sin(angle))
        new_x = self.x * cos_a - self.y * sin_a
        new_y = self.x * sin_a + self.y * cos_a
        return Vector(new_x, new_y)


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

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"


@dataclass
class Line:
    p: Point  # 直线上的一点
    v: Vector  # 直线的方向向量

    def is_point_on_line(self, q: Point) -> bool:
        """
        检查点 Q 是否在直线上。
        点 Q 在直线上的条件是向量 PQ (Q - self.p) 与直线的方向向量 self.v 平行。
        两个向量平行意味着它们的叉积为零。
        """
        if not isinstance(q, Point):
            raise TypeError("Input q must be a Point.")

        pq_vector = q - self.p  # 从 P (在直线上) 到 Q 的向量

        # 计算 PQ 和 v 的叉积
        cross_prod_val = pq_vector.cross_product(self.v)

        # 检查叉积是否接近于零（考虑浮点精度）
        return abs(cross_prod_val) < EPSILON

    def distance_to_point(self, q: Point) -> Decimal:
        """
        计算点 Q 到直线的距离。
        直线由点 P (self.p) 和方向向量 v (self.v) 定义。
        距离 d = |PQ x v| / |v|
        """
        if not isinstance(q, Point):
            raise TypeError("Input q must be a Point.")

        pq_vector = q - self.p  # 从 P (在直线上) 到 Q 的向量
        v_magnitude_squared = self.v.x**2 + self.v.y**2

        # 如果方向向量是零向量，这条“直线”实际上是一个点，点到点的距离
        if v_magnitude_squared == 0:
            # 如果 line.v 是零向量，则直线实际上是点 line.p
            # 计算点 Q 到点 line.p 的距离
            return ((q.x - self.p.x) ** 2 + (q.y - self.p.y) ** 2).sqrt()

        # 叉积的绝对值是 PQ 和 v 构成的平行四边形的面积
        # 面积 = 底 * 高 = |v| * d
        # d = 面积 / |v| = |PQ x v| / |v|
        distance = abs(pq_vector.cross_product(self.v)) / v_magnitude_squared.sqrt()
        return distance

    # 计算直线交点
    def intersection(self, other: Self) -> Point | None:
        """
        计算两条直线的交点。
        直线1: self.p + t * self.v
        直线2: other.p + s * other.v
        self.p.x + t * self.v.x = other.p.x + s * other.v.x
        self.p.y + t * self.v.y = other.p.y + s * other.v.y

        t * self.v.x - s * other.v.x = other.p.x - self.p.x
        t * self.v.y - s * other.v.y = other.p.y - self.p.y

        这是一个关于 t 和 s 的线性方程组：
        [ self.v.x  -other.v.x ] [ t ] = [ other.p.x - self.p.x ]
        [ self.v.y  -other.v.y ] [ s ]   [ other.p.y - self.p.y ]

        使用克莱默法则或消元法求解。
        行列式 D = (self.v.x) * (-other.v.y) - (-other.v.x) * (self.v.y)
                = -self.v.x * other.v.y + other.v.x * self.v.y
                = other.v.x * self.v.y - self.v.x * other.v.y
                = -self.v.cross_product(other.v)

        如果 D 接近于零，则直线平行或重合。
        """
        if not isinstance(other, Line):
            raise TypeError("Input other must be a Line.")

        # 计算方向向量的叉积
        cross_prod_v = self.v.cross_product(other.v)

        if abs(cross_prod_v) < EPSILON:
            # 方向向量叉积接近零，直线平行或重合
            # 检查 other.p 是否在 self 直线上
            # 如果 other.p 在 self 直线上，且方向向量平行，则直线重合。
            # 检查 other.p 是否在 self 直线上 (即 (other.p - self.p) x self.v 接近于零)
            if abs((other.p - self.p).cross_product(self.v)) < EPSILON:
                # 直线重合，有无数交点，通常返回 None 或特殊标记
                # 根据具体问题需求，可能需要返回 None 或抛出异常
                return None  # Indicates lines are coincident
            else:
                # 直线平行但不重合，没有交点
                return None

        # 直线不平行，计算交点
        # 使用克莱默法则求解 t 和 s
        # D = other.v.x * self.v.y - self.v.x * other.v.y = -self.v.cross_product(other.v)
        # Dx = (other.p.x - self.p.x) * (-other.v.y) - (-other.v.x) * (other.p.y - self.p.y)
        #    = -(other.p.x - self.p.x) * other.v.y + (other.p.y - self.p.y) * other.v.x
        #    = (other.p - self.p).cross_product(other.v)
        # Dy = self.v.x * (other.p.y - self.p.y) - (other.p.x - self.p.x) * self.v.y
        #    = -(other.p - self.p).cross_product(self.v)

        # t = Dx / D = (other.p - self.p).cross_product(other.v) / (-self.v.cross_product(other.v))
        #   = (other.p - self.p).cross_product(other.v) / (other.v.cross_product(self.v))
        # s = Dy / D = -(other.p - self.p).cross_product(self.v) / (-self.v.cross_product(other.v))
        #   = (other.p - self.p).cross_product(self.v) /
        # (other.v.cross_product(self.v))

        # 计算 t
        t_numerator = (other.p - self.p).cross_product(other.v)
        t = t_numerator / cross_prod_v

        # 计算交点 P_intersection = self.p + t * self.v
        intersection_point = self.p + self.v * t

        return intersection_point

    def is_parallel_to(self, other: Self) -> bool:
        """
        检查两条直线是否平行。
        两条直线平行当且仅当它们的方向向量平行。
        两个向量平行当且仅当它们的叉积为零。
        """
        if not isinstance(other, Line):
            raise TypeError("Input other must be a Line.")

        # 计算方向向量的叉积
        cross_prod_v = self.v.cross_product(other.v)

        # 检查叉积是否接近于零（考虑浮点精度）
        return abs(cross_prod_v) < EPSILON

    def get_perpendicular_line_through_point(self, q: Point) -> Self:
        """
        获取通过点 Q 且垂直于当前直线的直线。
        当前直线由点 P (self.p) 和方向向量 v (self.v) 定义。
        垂直向量 v_perp 可以是 (-v.y, v.x) 或 (v.y, -v.x)。
        新直线通过点 Q，方向向量为 v_perp。
        """
        if not isinstance(q, Point):
            raise TypeError("Input q must be a Point.")

        # 计算垂直方向向量
        v_perp = Vector(-self.v.y, self.v.x)

        # 如果原始方向向量是零向量，则无法定义垂直方向
        if self.v.x == 0 and self.v.y == 0:
            raise ValueError("Cannot get perpendicular line from a zero vector line.")

        # 新直线通过点 Q，方向向量为 v_perp
        return Line(q, v_perp)

    def is_coincident_with(self, other: Self) -> bool:
        """
        检查两条直线是否重合。
        两条直线重合当且仅当它们平行且其中一条直线上的任意一点在另一条直线上。
        """
        if not isinstance(other, Line):
            raise TypeError("Input other must be a Line.")

        # 首先检查是否平行
        if not self.is_parallel_to(other):
            return False

        # 如果平行，检查 other.p 是否在 self 直线上
        # other.p 在 self 直线上的条件是向量 (other.p - self.p) 与 self.v 平行
        # 即 (other.p - self.p) x self.v 接近于零
        return abs((other.p - self.p).cross_product(self.v)) < EPSILON

    def __contains__(self, point: Point) -> bool:
        """
        检查点是否在直线上。
        这是 is_point_on_line 方法的别名，用于支持 `point in line` 语法。
        """
        return self.is_point_on_line(point)

    def __eq__(self, value: Self):
        if not isinstance(value, Line):
            return NotImplemented
        return self.p == value.p and self.v == value.v


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

    def __contains__(self, point: Point) -> bool:
        """
        检查点是否在多边形内，包括边界和顶点。
        使用射线法 (Ray Casting Algorithm)
        """
        if not isinstance(point, Point):
            raise TypeError("Input point must be a Point.")

        n = len(self.points)
        if n < 3:
            return False  # 少于3个点不能构成多边形

        crossings = 0
        for i in range(n):
            p1 = self.points[i]
            p2 = self.points[(i + 1) % n]

            # 检查点是否在边的 y 坐标范围内
            if (p1.y <= point.y < p2.y) or (p2.y <= point.y < p1.y):
                # 计算射线与边的交点的 x 坐标
                # 通过相似三角形计算
                x_at_y = p1.x + (point.y - p1.y) * (p2.x - p1.x) / (p2.y - p1.y)
                if point.x < x_at_y:  # 射线与边相交
                    crossings += 1

        return crossings % 2 == 1


class CirclePos(Enum):
    """
    枚举类，表示圆和点、直线、圆之间的位置关系。
    """

    INTERSECT = auto()  # 相交
    TANGENT = auto()  # 相切
    DISJOINT = auto()  # 不相交/相离
    CONTAINS = auto()  # 包含 (一个圆包含另一个圆)
    CONTAINED_BY = auto()  # 被包含 (一个圆被另一个圆包含)
    EQUAL = auto()  # 重合 (两个圆完全相同)


@dataclass
class Circle:
    center: Point
    radius: Decimal

    def area(self) -> Decimal:
        return PI * self.radius**2

    def circumference(self) -> Decimal:
        return 2 * PI * self.radius

    # 园和直线交点
    def intersection_with_line(self, line: Line) -> list[Point]:
        """
        计算圆和直线的交点。
        # 将直线方程转换为标准形式 Ax + By + C = 0
        # 直线上的点 P(px, py)，方向向量 v(vx, vy)
        # 参数方程: x = px + t*vx, y = py + t*vy
        # 如果 vx != 0, vy != 0: (x - px)/vx = (y - py)/vy => vy*(x - px) = vx*(y - py)
        # vy*x - vy*px = vx*y - vx*py => vy*x - vx*y + vx*py - vy*px = 0
        # A = vy, B = -vx, C = vx*py - vy*px
        # 如果 vx == 0: x = px (垂直线) => x - px = 0 => A = 1, B = 0, C = -px
        # 如果 vy == 0: y = py (水平线) => y - py = 0 => A = 0, B = 1, C = -py

        # 为了避免除法和处理垂直/水平线，我们可以直接使用点到直线的距离公式
        # 点 (x0, y0) 到直线 Ax + By + C = 0 的距离 d = |Ax0 + By0 + C| / sqrt(A^2 + B^2)
        # 对于直线上的点 P(px, py) 和方向向量 v(vx, vy)，直线方程可以写为
        # (y - py)*vx = (x - px)*vy  => vy*x - vx*y + vx*py - vy*px = 0
        # A = vy, B = -vx, C = vx*py - vy*px
        # 圆心 (cx, cy) 到直线的距离 d = |vy*cx - vx*cy + vx*py - vy*px| / sqrt(vy^2 + (-vx)^2)
        # d = |(cx - px)*vy - (cy - py)*vx| / sqrt(vx^2 + vy^2)
        # 注意 (cx - px)*vy - (cy - py)*vx 是向量 (C - P) 和 v 的叉积的负值
        # d = |(P - C).cross_product(v)| / sqrt(v.x^2 + v.y^2)
        """
        if not isinstance(line, Line):
            raise TypeError("Input line must be a Line.")
        # 计算圆心到直线的距离
        # 使用点到直线的距离公式，直线由点 line.p 和向量 line.v 定义
        # 向量 PC = self.center - line.p
        # 距离 d = |PC x line.v| / |line.v|
        pc_vector = self.center - line.p
        # 向量 v 的模长 squared
        v_magnitude_squared = line.v.x**2 + line.v.y**2

        # 如果方向向量是零向量，这条“直线”实际上是一个点，无法计算距离
        if v_magnitude_squared == 0:
            # 如果直线向量为零，则 line.p 就是直线上的唯一“点”。
            # 如果圆心就是这个点，且半径为0，则它们重合（无数交点，但通常不这么处理）
            # 如果圆心不是这个点，或者半径大于0，则没有交点。
            # 题目中的直线通常是无限长的，所以零向量的情况不符合直线定义。
            # 假设 line.v 不是零向量。
            raise ValueError("Line direction vector cannot be zero.")

        # 叉积的绝对值是 PC 和 v 构成的平行四边形的面积
        # 面积 = 底 * 高 = |v| * d
        # d = 面积 / |v| = |PC x v| / |v|
        distance_to_line = (
            abs(pc_vector.cross_product(line.v)) / v_magnitude_squared.sqrt()
        )

        # Compare distance with radius using the global EPSILON

        if distance_to_line > self.radius + EPSILON:
            # 距离大于半径，直线不与圆相交
            return []
        elif abs(distance_to_line - self.radius) <= EPSILON:
            # 距离约等于半径，直线与圆相切，有一个交点
            # 找到圆心到直线的垂足
            # 垂足 Q = C + k * v_perp，其中 v_perp 是垂直于 v 的向量
            # v_perp 可以是 (-vy, vx) 或 (vx, vy)
            # 垂足 Q 也是直线上离圆心最近的点
            # 向量 CP = line.p - self.center
            # 在 v 方向上的投影长度 t = CP . v / |v|^2
            # 垂足 Q = line.p + t * v
            # 或者更直接地，找到圆心 C 到直线 line.p + t*line.v 的垂足
            # 向量 CQ = Q - C = line.p + t*line.v - C
            # CQ 垂直于 v，所以 CQ . v = 0
            # (line.p + t*line.v - C) . line.v = 0
            # (line.p - C) . line.v + t * (line.v . line.v) = 0
            # t = - (line.p - C) . line.v / (line.v . line.v)
            # t = (C - line.p) . line.v / |line.v|^2
            # t = pc_vector . line.v / v_magnitude_squared
            dot_product_pc_v = pc_vector.x * line.v.x + pc_vector.y * line.v.y
            t = dot_product_pc_v / v_magnitude_squared
            tangent_point = line.p + line.v * t
            return [tangent_point]
        else:
            # 距离小于半径，直线与圆相交，有两个交点
            # 找到圆心到直线的垂足 Q (如上计算 t)
            dot_product_pc_v = pc_vector.x * line.v.x + pc_vector.y * line.v.y
            t_closest = dot_product_pc_v / v_magnitude_squared
            closest_point_on_line = line.p + line.v * t_closest

            # 计算从垂足到交点的距离 (使用勾股定理)
            # distance_to_line^2 + distance_from_closest_to_intersection^2 = radius^2
            distance_from_closest_to_intersection_squared = (
                self.radius**2 - distance_to_line**2
            )
            # 确保平方根是实数，尽管 distance_to_line <= radius 应该保证这一点
            if distance_from_closest_to_intersection_squared < 0:
                # 由于浮点精度问题，可能出现微小的负值，将其视为零
                distance_from_closest_to_intersection = Decimal(0)
            else:
                distance_from_closest_to_intersection = (
                    distance_from_closest_to_intersection_squared.sqrt()
                )

            # 计算交点
            # 交点位于垂足 Q 沿着直线方向向量 v 的单位向量方向上，距离为 distance_from_closest_to_intersection
            # v 的单位向量 = v / |v|
            v_magnitude = v_magnitude_squared.sqrt()
            if v_magnitude == 0:  # 再次检查，尽管前面已经处理
                raise ValueError("Line direction vector cannot be zero.")

            unit_v = line.v / v_magnitude

            intersection1 = (
                closest_point_on_line + unit_v * distance_from_closest_to_intersection
            )
            intersection2 = (
                closest_point_on_line - unit_v * distance_from_closest_to_intersection
            )

            # 返回两个交点
            # 可以根据需要对交点进行排序，例如按 x 坐标或 y 坐标
            return [intersection1, intersection2]

    def intersection_with_circle(self, other: Self) -> list[Point]:
        """
        计算两个圆的交点。

        设两个圆的方程分别为：
        (x - cx1)^2 + (y - cy1)^2 = r1^2  （第一个圆，圆心 (cx1, cy1)，半径 r1）
        (x - cx2)^2 + (y - cy2)^2 = r2^2  （第二个圆，圆心 (cx2, cy2)，半径 r2）

        1. 特殊情况处理
           - 圆心重合：如果 cx1 = cx2 且 cy1 = cy2：
             - 如果 r1 = r2，圆重合，有无数交点，返回 None 或特殊标记。
             - 如果 r1 ≠ r2，圆不相交，无解。

        2. 几何方法
           - 计算圆心距 d = sqrt((cx2 - cx1)^2 + (cy2 - cy1)^2)。
           - 讨论交点情况：
             - 如果 d > r1 + r2，圆外离，无交点。
             - 如果 d = r1 + r2，圆外切，一个交点。
             - 如果 d < |r1 - r2|，圆内含，无交点。
             - 如果 d = |r1 - r2| 且 r1 ≠ r2，圆内切，一个交点。
             - 如果 |r1 - r2| < d < r1 + r2，圆相交，两个交点。

        3. 解方程组（相交情况）
           - 设交点为 (x, y)。
           - 联立两个圆的方程，消去二次项：
             (x^2 - 2cx1x + cx1^2 + y^2 - 2cy1y + cy1^2 = r1^2) - (x^2 - 2cx2x + cx2^2 + y^2 - 2cy2y + cy2^2 = r2^2)
             2(cx2 - cx1)x + (cx1^2 - cx2^2) + 2(cy2 - cy1)y + (cy1^2 - cy2^2) = r1^2 - r2^2
           - 令 A = 2(cx2 - cx1)，B = 2(cy2 - cy1)，C = (r1^2 - r2^2) - (cx1^2 - cx2^2) - (cy1^2 - cy2^2)，
             得到直线方程 Ax + By = C。
           - 现在问题转化为求直线与圆的交点，可以使用 Circle.intersection_with_line 方法。

        4. 计算交点
           - 如果存在交点，直线与圆的交点即为所求。
           - 如果交点数目为0或1，根据几何关系确定相交、相切。

        """
        if not isinstance(other, Circle):
            raise TypeError("Input other must be a Circle.")

        # 1. 特殊情况处理
        if self.center == other.center:
            if self.radius == other.radius:
                # 圆重合，有无数交点
                return []  # 或返回 None，根据具体需求
            else:
                # 圆心重合但半径不同，无交点
                return []

        # 2. 计算圆心距
        distance_between_centers = (self.center - other.center).magnitude()

        # 3. 讨论交点情况
        sum_of_radii = self.radius + other.radius
        diff_of_radii = abs(self.radius - other.radius)

        if distance_between_centers > sum_of_radii + EPSILON:
            # 圆外离，无交点
            return []
        elif abs(distance_between_centers - sum_of_radii) <= EPSILON:
            # 圆外切，一个交点
            # 过两个圆心的直线与圆的交点
            direction_vector = (other.center - self.center).normalized()
            intersection_point = self.center + direction_vector * self.radius
            return [intersection_point]
        elif distance_between_centers < diff_of_radii - EPSILON:
            # 圆内含，无交点
            return []
        elif abs(distance_between_centers - diff_of_radii) <= EPSILON:
            # 圆内切，一个交点
            direction_vector = (other.center - self.center).normalized()
            intersection_point = self.center + direction_vector * self.radius
            return [intersection_point]
        else:
            # 圆相交，两个交点

            # 4. 解方程组，计算交点
            cx1, cy1 = self.center.x, self.center.y
            cx2, cy2 = other.center.x, other.center.y
            r1, r2 = self.radius, other.radius

            A = 2 * (cx2 - cx1)
            B = 2 * (cy2 - cy1)
            C = (r1**2 - r2**2) - (cx1**2 - cx2**2) - (cy1**2 - cy2**2)

            # 特殊情况处理: B 接近于 0，直线接近垂直
            if abs(B) < EPSILON:
                if abs(A) < EPSILON:
                    # A 和 B 都接近 0，意味着什么？
                    # 如果 A = B = 0，说明两个圆心相同，应该在前面的情况中处理
                    # 这里为了确保代码健壮性，返回空列表
                    return []

                # 直线方程简化为 x = C / A
                # 将 x 代入第一个圆的方程：
                # (C/A - cx1)^2 + (y - cy1)^2 = r1^2
                # (y - cy1)^2 = r1^2 - (C/A - cx1)^2

                x_val = C / A
                discriminant = r1**2 - (x_val - cx1) ** 2  # 判别式，检查解的情况

                if discriminant < -EPSILON:  # 判别式小于零，无实数解
                    return []  # 无交点
                elif abs(discriminant) <= EPSILON:  # 判别式等于零，一个解
                    y_val = cy1
                    return [Point(x_val, y_val)]
                else:  # 判别式大于零，两个解
                    y1 = cy1 + discriminant.sqrt()
                    y2 = cy1 - discriminant.sqrt()
                    return [Point(x_val, y1), Point(x_val, y2)]
            else:
                # 直线方程可以写成 y = (C - Ax) / B
                # 将 y 代入第一个圆的方程：
                # (x - cx1)^2 + ((C - Ax) / B - cy1)^2 = r1^2

                # 展开并整理，得到关于 x 的二次方程：
                # 令 k = C / B - cy1
                # (x - cx1)^2 + (k - (A/B)x)^2 = r1^2
                # x^2 - 2cx1x + cx1^2 + k^2 - 2k(A/B)x + (A/B)^2x^2 = r1^2
                # (1 + (A/B)^2)x^2 - 2(cx1 + k(A/B))x + (cx1^2 + k^2 - r1^2) = 0

                # 令 a = (1 + (A/B)^2)
                #    b = -2(cx1 + k(A/B))
                #    c = (cx1^2 + k^2 - r1^2)

                # 使用判别式 Δ = b^2 - 4ac
                # - Δ < 0，无解 (无交点)
                # - Δ = 0，一个解 (相切)
                # - Δ > 0，两个解 (相交)

                a = 1 + (A / B) ** 2
                k = C / B - cy1
                b = -2 * (cx1 + k * (A / B))
                c = cx1**2 + k**2 - r1**2

                discriminant = b**2 - 4 * a * c  # 计算判别式

                if discriminant < -EPSILON:  # 判别式小于零，无实数解
                    return []  # 无交点
                elif abs(discriminant) <= EPSILON:  # 判别式等于零，一个解
                    x_val = -b / (2 * a)
                    y_val = (C - A * x_val) / B
                    return [Point(x_val, y_val)]
                else:  # 判别式大于零，两个解
                    x1 = (-b + discriminant.sqrt()) / (2 * a)
                    x2 = (-b - discriminant.sqrt()) / (2 * a)
                    y1 = (C - A * x1) / B
                    y2 = (C - A * x2) / B
                    return [Point(x1, y1), Point(x2, y2)]

    # 点园
    def relationship_with_point(self, point: Point) -> CirclePos:
        """确定圆和点的关系（相交、相切、不相离）。"""
        if not isinstance(point, Point):
            raise TypeError("Input point must be a Point.")

        distance_squared = (point.x - self.center.x) ** 2 + (
            point.y - self.center.y
        ) ** 2
        radius_squared = self.radius**2

        # Use EPSILON for comparison
        if distance_squared > radius_squared + EPSILON:
            return CirclePos.DISJOINT  # 点在圆外
        elif abs(distance_squared - radius_squared) <= EPSILON:
            return CirclePos.TANGENT  # 点在圆周上
        else:
            return CirclePos.INTERSECT  # 点在圆内

    # 园和直线关系

    def relationship_with_line(self, line: Line) -> CirclePos:
        """确定圆和直线的关系（相交、相切、不相离）。"""
        if not isinstance(line, Line):
            raise TypeError("Input line must be a Line.")

        distance_to_line = self.distance_to_point(line)

        if distance_to_line > self.radius + EPSILON:
            return CirclePos.DISJOINT
        elif abs(distance_to_line - self.radius) <= EPSILON:
            return CirclePos.TANGENT
        else:
            return CirclePos.INTERSECT

    def relationship_with_circle(self, other: Self) -> list[CirclePos]:
        """确定两个圆的关系。"""
        if not isinstance(other, Circle):
            raise TypeError("Input other must be a Circle.")

        # 计算圆心之间的距离
        distance_between_centers = (self.center - other.center).magnitude()

        # 比较距离和半径之和/差
        sum_of_radii = self.radius + other.radius
        diff_of_radii = abs(self.radius - other.radius)

        # 使用 EPSILON 进行浮点数比较
        if distance_between_centers > sum_of_radii + EPSILON:
            # 距离大于半径之和，圆不相交（相离）
            return [CirclePos.DISJOINT]
        elif abs(distance_between_centers - sum_of_radii) <= EPSILON:
            # 距离约等于半径之和，圆外切
            return [CirclePos.TANGENT]
        elif distance_between_centers < diff_of_radii - EPSILON:
            # 距离小于半径之差的绝对值，一个圆包含另一个圆
            if self.radius > other.radius:
                return [CirclePos.CONTAINS]
            elif other.radius > self.radius:
                return [CirclePos.CONTAINED_BY]
            else:  # 半径相等，圆心相同
                return [CirclePos.EQUAL]
        elif abs(distance_between_centers - diff_of_radii) <= EPSILON:
            # 距离约等于半径之差的绝对值，圆内切
            return [CirclePos.TANGENT, CirclePos.CONTAINS]  # 内切时，大圆包含小圆
        else:
            # 距离在半径之差和半径之和之间，圆相交
            return [CirclePos.INTERSECT]

    def intersection_area_with_circle(self, other: Self) -> Decimal:
        """
        计算两个圆的相交面积。

        设两个圆的方程分别为：
        (x - cx1)^2 + (y - cy1)^2 = r1^2  （第一个圆，圆心 (cx1, cy1)，半径 r1）
        (x - cx2)^2 + (y - cy2)^2 = r2^2  （第二个圆，圆心 (cx2, cy2)，半径 r2）

        1. 特殊情况处理
           - 圆心重合：如果 cx1 = cx2 且 cy1 = cy2：
             - 如果 r1 = r2，圆重合，相交面积为 πr1^2。
             - 如果 r1 ≠ r2，小圆完全包含在大圆内，相交面积为 π(min(r1, r2))^2。

        2. 计算圆心距 d = sqrt((cx2 - cx1)^2 + (cy2 - cy1)^2)。

        3. 讨论交点情况：
           - 如果 d > r1 + r2，圆外离，相交面积为 0。
           - 如果 d = r1 + r2，圆外切，相交面积为 0。
           - 如果 d < |r1 - r2|，圆内含，相交面积为 π(min(r1, r2))^2。
           - 如果 d = |r1 - r2| 且 r1 ≠ r2，圆内切，相交面积为 π(min(r1, r2))^2。
           - 如果 |r1 - r2| < d < r1 + r2，圆相交，需要计算相交面积。

        4. 计算相交面积（相交情况）
           - 令 r1 和 r2 为两个圆的半径，d 为圆心距。
           - 令 theta1 = acos((r1^2 + d^2 - r2^2) / (2 * r1 * d))  (第一个圆的扇形角的一半)
           - 令 theta2 = acos((r2^2 + d^2 - r1^2) / (2 * r2 * d))  (第二个圆的扇形角的一半)
           - 相交面积 A = r1^2 * theta1 + r2^2 * theta2 - d * r1 * sin(theta1)

        """
        if not isinstance(other, Circle):
            raise TypeError("Input other must be a Circle.")

        # 1. 特殊情况处理
        if self.center == other.center:
            if self.radius == other.radius:
                # 圆重合，相交面积等于其中一个圆的面积
                return self.area()
            else:
                # 圆心重合，小圆包含在大圆内，相交面积等于小圆面积
                return min(self.area(), other.area())

        # 2. 计算圆心距
        distance_between_centers = (self.center - other.center).magnitude()

        # 3. 讨论交点情况
        sum_of_radii = self.radius + other.radius
        diff_of_radii = abs(self.radius - other.radius)

        if distance_between_centers > sum_of_radii + EPSILON:
            # 圆外离，相交面积为 0
            return Decimal(0)
        elif abs(distance_between_centers - sum_of_radii) <= EPSILON:
            # 圆外切，相交面积为 0
            return Decimal(0)
        elif distance_between_centers < diff_of_radii - EPSILON:
            # 圆内含，相交面积等于小圆面积
            return min(self.area(), other.area())
        elif abs(distance_between_centers - diff_of_radii) <= EPSILON:
            # 圆内切，相交面积等于小圆面积
            return min(self.area(), other.area())
        else:
            # 4. 计算相交面积（相交情况）
            r1, r2 = self.radius, other.radius
            d = distance_between_centers

            # 检查 d 是否为零以避免 ZeroDivisionError
            if d == 0:
                if r1 == r2:
                    # 圆完全重合
                    return self.area()
                else:
                    # 一个圆完全包含在另一个圆内
                    return min(self.area(), other.area())

            # 使用余弦定理计算扇形角的一半
            # 确保 acos 的参数在 [-1, 1] 范围内
            arg1 = (r1**2 + d**2 - r2**2) / (2 * r1 * d)
            arg2 = (r2**2 + d**2 - r1**2) / (2 * r2 * d)

            # 检查 acos 参数的有效性
            if abs(arg1) > 1:
                arg1 = Decimal(1) if arg1 > 1 else Decimal(-1)
            if abs(arg2) > 1:
                arg2 = Decimal(1) if arg2 > 1 else Decimal(-1)

            theta1 = Decimal(math.acos(arg1))
            theta2 = Decimal(math.acos(arg2))

            # 相交面积 A = r1^2 * theta1 + r2^2 * theta2 - d * r1 * sin(theta1)
            return r1**2 * theta1 + r2**2 * theta2 - d * r1 * Decimal(math.sin(theta1))

    def __contains__(self, point: Point) -> bool:
        """检查点是否在圆内。"""
        if not isinstance(point, Point):
            raise TypeError("Input point must be a Point.")
        distance_squared = (point.x - self.center.x) ** 2 + (
            point.y - self.center.y
        ) ** 2
        return distance_squared <= self.radius**2
