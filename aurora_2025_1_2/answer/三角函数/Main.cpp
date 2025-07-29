#include <iostream>
#include <cmath>
using namespace std;

//求最大公约数
int gcd(int x, int y) //辗转相除法
{
	int z = y;
	while (x % y != 0)
	{
		z = x % y;
		x = y;
		y = z;
	}
	return z; //返回最小公因数
}


int main() 
{
	int T;
	cin >> T;
	while (T--) {
		int a, b, c;
		cin >> a >> b >> c;
		int MAX = max(a, max(b, c)),
			MIN = min(a, min(b, c)),
			GCD = gcd(MIN, MAX);//计算最大公约数
		printf("%d/%d\n", MIN / GCD, MAX / GCD);
	}
	return 0;
}