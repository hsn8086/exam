from dataclasses import dataclass
from decimal import Decimal, getcontext
from enum import Enum, auto

getcontext().prec = 100
PI = Decimal(314159265_358979323846264_338327950288_419716939937510) / Decimal(10**50)


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

        # 比较距离和半径
        # 使用一个小的 epsilon 来处理浮点数精度问题，特别是 Decimal
        epsilon = Decimal("1e-9")  # 可以根据需要调整精度

        if distance_to_line > self.radius + epsilon:
            # 距离大于半径，直线不与圆相交
            return []
        elif abs(distance_to_line - self.radius) <= epsilon:
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

    def __and__(self, other: Line) -> bool: ...

    def __contains__(self, point: Point) -> bool:
        """检查点是否在圆内。"""
        if not isinstance(point, Point):
            raise TypeError("Input point must be a Point.")
        distance_squared = (point.x - self.center.x) ** 2 + (
            point.y - self.center.y
        ) ** 2
        return distance_squared <= self.radius**2


pg = Polygon(
    [
        Point(*map(int, input().split())),
        Point(*map(int, input().split())),
        Point(*map(int, input().split())),
    ]
)

print(pg.area())
