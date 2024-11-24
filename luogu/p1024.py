# def clac(a,b,c,d):
#     u=(9*a*b*c-27*(a**2)*d-2*(b**3))/54*(a**3)
#     v=math.sqrt(3*(4*a*(c**3)-(b**2)*(c**2)-18*a*b*c*d+27*(a**2)*(d**2)+4*d*(b**3)))/(18*(a**2))
#     if abs(u+v)>=abs(u-v):
#         m=(u+v)**(1/3)
#     else:
#         m=(u-v)**(1/3)

#     if m!=0:
#         n=(b**2-3*a*c)/(9*(a**2)*m)
#     else:
#         n=0
#     w=-(1/2)+(math.sqrt(3)/2)*1j
#     w2=-(1/2)-(math.sqrt(3)/2)*1j
#     return m+n-b/(3*a),w*m+w2*n-b/(3*a),w2*m+w*n-b/(3*a)
# def clac(a,b,c,d):
#     q=(27*(a**2)*d+2*(b**3)-9*a*b*c)/(27*(a**3))
#     p=(3*a*c-b**2)/(3*(a**2))

# import cmath


# def clac(a, b, c, d):
#     p = (3 * a * c - b**2) / (3 * a**2)
#     q = (2 * b**3 - 9 * a * b * c + 27 * a**2 * d) / (27 * a**3)

#     delta = (q / 2) ** 2 + (p / 3) ** 3

#     u_cube = -q / 2 + cmath.sqrt(delta)
#     v_cube = -q / 2 - cmath.sqrt(delta)

#     u = u_cube ** (1 / 3)
#     v = v_cube ** (1 / 3)

#     if u.imag != 0:
#         u = complex(u.real, u.imag)
#     if v.imag != 0:
#         v = complex(v.real, v.imag)

#     root1 = u + v - b / (3 * a)
#     root2 = -(u + v) / 2 - b / (3 * a) + cmath.sqrt(3) * (u - v) / 2 * 1j
#     root3 = -(u + v) / 2 - b / (3 * a) - cmath.sqrt(3) * (u - v) / 2 * 1j
#     rst = [root1.real, root2.real, root3.real]
#     rst.sort()
#     return rst
def f(x, a, b, c, d):
    return a * pow(x, 3) + b * pow(x, 2) + c * x + d


def f_p(x, a, b, c, d):
    return 3 * pow(x, 2) + 2 * b * x + c


def clac(x, a, b, c, d, iterations=100000):
    for i in range(iterations):
        fx = f(x, a, b, c, d)
        fpx = f_p(x, a, b, c, d)

        x = x - fx / fpx
    return x


def solve(a, b, c, d):
    stx = 10000
    right = clac(stx, a, b, c, d)
    left = clac(-stx, a, b, c, d)
    mid = clac((right + left) / 2, a, b, c, d)
    return left, mid, right


rst = solve(*map(float, input().split()))
x1, x2, x3 = rst
print("%.2f %.2f %.2f" % (x1, x2, x3))
