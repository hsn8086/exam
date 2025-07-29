#include <bits/stdc++.h>
#include <deque>
#define endl "\n"
#define fastio std::ios::sync_with_stdio(false), std::cin.tie(nullptr)
#define let auto
using i64 = long long;
template <typename T> T input() {

    T val;
    std::cin >> val;
    return val;
}
template <typename T0, typename... Ts>
void print(T0 t0, Ts... ts, std::string sep = " ", std::string end = "\n") {
    std::cout << t0;
    if constexpr (sizeof...(ts) > 0) {
        std::cout << sep;
        print(ts...);
    } else
        std::cout << end;
}

template <typename T> std::vector<T> inpl() {
    int n = input<int>();
    std::vector<T> val(n);
    for (int i = 0; i < n; i++) {
        std::cin >> val[i];
    }
    return val;
}

template <typename... Args> void inpm(Args &...args) { ((std::cin >> args), ...); }

class Range {
    int start_, end_, step_;
    int current_;

  public:
    Range(int end) : start_(0), end_(end), step_(1), current_(0) {}
    Range(int start, int end, int step = 1)
        : start_(start), end_(end), step_(step), current_(start) {}

    // 迭代器支持
    class Iterator {
        int current_, end_, step_;

      public:
        Iterator(int current, int end, int step) : current_(current), end_(end), step_(step) {}

        int operator*() const { return current_; }

        Iterator &operator++() {
            current_ += step_;
            return *this;
        }

        bool operator!=(const Iterator &other) const {
            return step_ > 0 ? current_ < other.current_ : current_ > other.current_;
        }
    };

    Iterator begin() const { return Iterator(start_, end_, step_); }
    Iterator end() const { return Iterator(end_, end_, step_); }
};

int main() {
    std::deque<int> que;
    for (let _ : Range(input<int>())) {
        let cmd = input<int>();
        if (cmd == 1) {
            que.push_back(input<int>());
        } else if (cmd == 2) {
            print(que.front());
            que.pop_front();
        }
    }
    return 0;
}