# 解题思路
注意到,保龄球边长$x$满足方程$x(x+1)/2=w+b$,可转换为$f(x)=x(x+1)-2(w+b)$,则$f'(x)=2x+1$,由牛顿迭代得出结果向下取整.
# 代码实现
``` python
import math

def newton_method(f, fd, x0, eps=1e-10, max_iter=100):
	x = x0
	for _ in range(max_iter):
		fx = f(x)
		if abs(fx) < eps:
		return x
		x = x - fx / fd(x)
		return x

ntc = int(input())
for _ in range(ntc):
	w, b = map(int, input().split())
	rst = newton_method(
	lambda x: x**2 + x - 2 * (w + b),
	lambda x: 2 * x + 1,
	100,
	)
	print(math.floor(rst))
```