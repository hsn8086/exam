#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <sstream>

// 解决方案函数
std::vector<int> solve(int m, int n, std::multiset<int>& a, std::vector<std::string>& rules) {
    std::vector<int> results;

    for (const auto& rule : rules) {
        if (rule.empty()) continue;  // 跳过空规则

        std::istringstream iss(rule);
        std::string op;
        int lint, rint;
        iss >> op >> lint >> rint;  // 分离操作符和左右边界

        std::vector<int> insert_list;
        std::vector<int> pop_list;

        // 遍历 multiset 并记录需要删除和插入的元素
        for (auto it = a.lower_bound(lint); it != a.end() && *it <= rint; ) {
            int val = *it;
            if (op == "+") {
                insert_list.push_back(val + 1);
            } else {
                insert_list.push_back(val - 1);
            }
            // 使用 iterator 删除元素后返回下一个元素的位置
            it = a.erase(it);
        }

        // 将新生成的元素插入 multiset 中
        for (int val : insert_list) {
            a.insert(val);
        }

        // 记录当前最大的元素
        results.push_back(*a.rbegin());
    }

    return results;
}

int main() {
    int count_of_tc;
    std::cin >> count_of_tc;  // 输入测试用例数

    for (int i = 0; i < count_of_tc; ++i) {
        int n, m;
        std::cin >> n >> m;  // 输入 n 和 m

        std::multiset<int> a;  // 使用 multiset 存储数组元素
        for (int j = 0; j < n; ++j) {
            int num;
            std::cin >> num;
            a.insert(num);  // 插入数组元素到 multiset
        }

        std::vector<std::string> rules(m);
        std::cin.ignore();  // 忽略换行符
        for (int j = 0; j < m; ++j) {
            std::getline(std::cin, rules[j]);  // 输入规则
        }

        std::vector<int> result = solve(m, n, a, rules);

        // 输出结果
        for (int res : result) {
            std::cout << res << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}
