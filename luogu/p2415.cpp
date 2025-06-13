#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> nums;
    int num;
    while (cin >> num) {
        nums.push_back(num);
    }
    long long sum = accumulate(nums.begin(), nums.end(), 0LL);
    long long result = sum * (1LL << (nums.size() - 1));
    cout << result;
}
