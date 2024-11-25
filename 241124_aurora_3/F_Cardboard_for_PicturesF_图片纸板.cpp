#include <iostream>
#include <vector>
using namespace std;
using i64 = long long;
// 计算函数，注意使用 long long 避免溢出
i64 clac(const vector<int>& a, i64 c, i64 w) {
    i64 sum = 0;
    for (int s : a) {
        i64 temp = s + 2 * w;
        sum += temp * temp;
    }
    return sum - c;
}

// 二分查找函数
i64 bis(const vector<int>& a, i64 c, i64 lo, i64 hi) {
    while (lo <= hi) {
        i64 mid = lo + (hi - lo) / 2;
        i64 v = clac(a, c, mid);
        
        if (v == 0) return mid;
        if (v > 0) hi = mid - 1;
        else lo = mid + 1;
    }
    return lo; // 返回最接近的解
}

int main() {
    int ntc;
    cin >> ntc;
    
    while (ntc--) {
        int n;
        i64 c;
        cin >> n >> c;
        
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        
        i64 result = bis(a, c, 0, 1e18);
        cout << result << endl;
    }
    
    return 0;
}