#include <algorithm>
#include <iostream>
using namespace std;

void fast_io() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);
}

bool is_divisor(long long a, long long b) { return b != 0 && a % b == 0; }
int getNextPowerOf2(int num) {
  // 处理0和负数的情况
  if (num <= 0)
    return 1;

  // 计算二进制位数
  int count = 0;
  int temp = num;
  while (temp) {
    count++;
    temp >>= 1;
  }

  // 返回下一个2的幂
  return 1 << count;
}
int main() {
  fast_io();
  int n;
  cin >> n;

  while (n--) {
    long long x, m;
    cin >> x >> m;
    long long count = 0;

    if (m >= x) {

      for (long long y = 1; y <= x; y++) {
        long long xor_val = x ^ y;
        if (is_divisor(xor_val, x) || is_divisor(xor_val, y)) {
          count++;
        }
      }

      long long xor_val = x;
      long long step = x;
      while (xor_val <= getNextPowerOf2(m)) {
        xor_val += step;
        long long y = x ^ xor_val;
        if (y <= m && y > 0) {
          count++;
        }
      }
    } else {

      for (long long y = 1; y <= m; y++) {
        long long xor_val = x ^ y;
        if (is_divisor(xor_val, x) || is_divisor(xor_val, y)) {
          count++;
        }
      }
    }

    cout << count << '\n';
  }

  return 0;
}