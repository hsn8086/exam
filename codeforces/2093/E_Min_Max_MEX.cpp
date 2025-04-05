#include <bits/stdc++.h>
using namespace std;

using i64 = long long;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int t;
  cin >> t;

  while (t--) {
    i64 n, k;
    cin >> n >> k;

    vector<i64> a(n), vals;
    for (i64 &x : a) {
      cin >> x;
      vals.push_back(x);
    }

    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    i64 mex = 0;
    for (i64 v : vals) {
      if (v == mex)
        ++mex;
      else if (v > mex)
        break;
    }

    map<i64, int> cnt;
    for (const i64 &x : a) {
      cnt[x]++;
    }

    i64 left = 0, right = mex, ans = 0;

    while (left <= right) {
      i64 mid = (left + right) / 2;
      bool valid = true;

      if (mid > 0) {
        for (i64 i = 0; i < mid; ++i) {
          auto it = cnt.find(i);
          if (it == cnt.end() || it->second < k) {
            valid = false;
            break;
          }
        }
        if (!valid) {
          right = mid - 1;
          continue;
        }
      }

      if (mid == 0) {
        if (k <= n) {
          ans = max(ans, 0LL);
          left = mid + 1;
        } else {
          right = mid - 1;
        }
      } else {
        i64 req = mid;
        vector<int> freq(req, 0);
        i64 c_seg = 0, col = 0;

        for (const i64 &x : a) {
          if (x >= 0 && x < req) {
            if (++freq[x] == 1) ++col;
            if (col == req) {
              ++c_seg;
              fill(freq.begin(), freq.end(), 0);
              col = 0;
            }
          }
        }

        if (c_seg >= k) {
          ans = max(ans, mid);
          left = mid + 1;
        } else {
          right = mid - 1;
        }
      }
    }

    cout << ans << '\n';
  }

  return 0;
}
