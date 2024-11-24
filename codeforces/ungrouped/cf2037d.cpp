#include<bits/stdc++.h>
int main(){
    if (powers.empty()) {
    break;
}
auto [pos, value] = powers.front();
powers.pop_front();

if (pos < left) {
    now_powers.push_back({pos, value});
} else {
    powers.push_front({pos, value});
    break;
}
std::sort(now_powers.begin(), now_powers.end(), [](const std::pair<int, int>& a, const std::pair<int, int>& b) {
    return a.second < b.second;
});
while (power < right - left + 2) {
    if (now_powers.empty()) {
        return -1;
    }
    auto [pos, value] = now_powers.back();
    now_powers.pop_back();

    power += value;
    count += 1;
}
return count;

int ntc;
std::cin >> ntc;
return 0;
}