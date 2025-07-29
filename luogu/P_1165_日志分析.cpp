#include <iostream>
#include <vector>

struct Item {
    int id;
    int mass;

    Item(int id, int mass) : id(id), mass(mass) {}
};

int main() {
    std::vector<Item> que = {Item(0, 0)};
    int cnt = 0;

    int n;
    std::cin >> n;

    for (int i = 0; i < n; ++i) {
        int cmd;
        std::cin >> cmd;

        switch (cmd) {
            case 0:
                int mass;
                std::cin >> mass;
                cnt++;
                if (mass > que.back().mass) {
                    que.push_back(Item(cnt, mass));
                }
                break;
            case 1:
                if (que.back().id == cnt) {
                    que.pop_back();
                }
                cnt--;
                break;
            case 2:
                std::cout << que.back().mass << std::endl;
        } 
    }
    return 0;
}