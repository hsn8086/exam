#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

long long pow_mod(long long base, long long exp, long long mod) {
  long long result = 1;
  base = base % mod;
  while (exp > 0) {
    if (exp % 2 == 1) {
      result = (result * base) % mod;
    }
    base = (base * base) % mod;
    exp = exp / 2;
  }
  return result;
}

long long mod_inverse(long long a, long long p) { return pow_mod(a, p - 2, p); }

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, p, k;
  cin >> n >> p >> k;

  long long ans = 0;
  for (int i = 1; i <= n; ++i) {
    long long v;
    cin >> v;
    long long term1 = pow_mod(k, i, p);
    long long term2 = mod_inverse(v, p);
    ans = (ans + (term1 * term2) % p) % p;
  }

  cout << ans << endl;

  return 0;
}