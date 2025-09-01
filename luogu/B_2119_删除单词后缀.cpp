#include <bits/stdc++.h>

signed main() {
    std::string s;
    std::cin >> s;
    int length = s.length();
    if (length >= 2 &&
        ("er" == s.substr(length - 2, 2) || "ly" == s.substr(length - 2, 2))) {
        std::cout << s.substr(0, length - 2) << std::endl;
    } else if (length >= 3 && "ing" == s.substr(length - 3, 3)) {
        std::cout << s.substr(0, length - 3) << std::endl;
    } else {
        std::cout << s << std::endl;
    }
    return 0;
}