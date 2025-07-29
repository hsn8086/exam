#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

typedef long double ld;

const ld EPSILON = 1e-12;

class Vector {
public:
    ld x, y;

    Vector(ld x, ld y) : x(x), y(y) {}

    Vector operator-(const Vector& other) const {
        return Vector(x - other.x, y - other.y);
    }

    Vector operator*(ld scalar) const {
        return Vector(x * scalar, y * scalar);
    }

    Vector operator-() const {
        return Vector(-x, -y);
    }

    ld cross_product(const Vector& other) const {
        return x * other.y - y * other.x;
    }

    ld dot_product(const Vector& other) const {
        return x * other.x + y * other.y;
    }

    ld magnitude() const {
        return sqrt(x*x + y*y);
    }

    ld angle(const Vector& other) const {
        ld mag_self = magnitude();
        ld mag_other = other.magnitude();

        if (mag_self == 0 || mag_other == 0) {
            throw runtime_error("Cannot calculate angle with a zero vector.");
        }

        ld dot_prod = dot_product(other);
        ld cos_theta = dot_prod / (mag_self * mag_other);

        cos_theta = max(ld(-1.0), min(ld(1.0), cos_theta));

        return acos(cos_theta);
    }

    Vector rotate(ld angle) const {
        ld cos_a = cos(angle);
        ld sin_a = sin(angle);
        ld new_x = x * cos_a - y * sin_a;
        ld new_y = x * sin_a + y * cos_a;
        return Vector(new_x, new_y);
    }
};

class Point {
public:
    ld x, y;

    Point(ld x, ld y) : x(x), y(y) {}

    Vector operator-(const Point& other) const {
        return Vector(x - other.x, y - other.y);
    }

    Point operator+(const Vector& vec) const {
        return Point(x + vec.x, y + vec.y);
    }
};

class Line {
public:
    Point p;
    Vector v;

    Line(const Point& p, const Vector& v) : p(p), v(v) {}

    Point* intersection(const Line& other) {
        ld cross_prod_v = v.cross_product(other.v);

        if (abs(cross_prod_v) < EPSILON) {
            if (abs((other.p - p).cross_product(v)) < EPSILON) {
                return nullptr;
            } else {
                return nullptr;
            }
        }

        ld t_numerator = (other.p - p).cross_product(other.v);
        ld t = t_numerator / cross_prod_v;
        Point intersection_point = p + v * t;
        return new Point(intersection_point);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout << fixed << setprecision(6);

    int t;
    cin >> t;

    while (t--) {
        ld x1, y1, x2, y2, x3, y3;
        cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

        Point p1(x1, y1);
        Point p2(x2, y2);
        Point p3(x3, y3);

        Vector v1 = p2 - p1;
        Vector v2 = p3 - p2;
        Vector v3 = p1 - p3;

        ld ang1 = v1.angle(-v2);
        ld ang2 = v2.angle(-v3);
        ld ang3 = v3.angle(-v1);

        Vector nv1_1 = v1.rotate(ang3 / 3);
        Vector nv1_2 = v1.rotate(ang3 * 2 / 3);
        Vector nv2_1 = v2.rotate(ang1 / 3);
        Vector nv2_2 = v2.rotate(ang1 * 2 / 3);
        Vector nv3_1 = v3.rotate(ang2 / 3);
        Vector nv3_2 = v3.rotate(ang2 * 2 / 3);

        Line l1_1(p1, nv1_1);
        Line l1_2(p1, nv1_2);
        Line l2_1(p2, nv2_1);
        Line l2_2(p2, nv2_2);
        Line l3_1(p3, nv3_1);
        Line l3_2(p3, nv3_2);

        Point* rp1 = l1_1.intersection(l2_2);
        Point* rp2 = l2_1.intersection(l3_2);
        Point* rp3 = l3_1.intersection(l1_2);

        cout << rp2->x << " " << rp2->y << " "
             << rp3->x << " " << rp3->y << " "
             << rp1->x << " " << rp1->y << "\n";

        delete rp1;
        delete rp2;
        delete rp3;
    }

    return 0;
}