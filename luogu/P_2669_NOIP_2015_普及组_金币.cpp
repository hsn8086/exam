#include <bits/stdc++.h>
#include <iostream>

int main() {
    int n;
    std::cin >> n;
    int round = 1, cnt = 1, ans = 0;
    while (n--) {
        ans += round;
        if (cnt == round) {
            round++;
            cnt = 0;
        }
    }
    std::cout << round;
}