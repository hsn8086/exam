/*
*/

  #include <iostream>
#include <vector>
using namespace std;

int find(vector<int>& lst, int idx) {
    if (lst[idx] == idx) {
        return idx;
    }
    lst[idx] = find(lst, lst[idx]);
    return lst[idx];
}

bool test(vector<int>& lst, int a, int b) {
    int a_leader = find(lst, a);
    int b_leader = find(lst, b);
    return a_leader == b_leader;
}

void merge(vector<int>& lst, int a, int b) {
    int a_leader = find(lst, a);
    int b_leader = find(lst, b);
    if (a_leader != b_leader) {
        lst[a_leader] = b_leader;
    }
}

int main() {
    std::ios::sync_with_stdio(0);
  std::cin.tie(0);
    int t;
    cin >> t;
    while (t--) {
        int n, q;
        cin >> n >> q;
        vector<int> hu(n + 1);
        vector<int> lst(n + 1);
        vector<int> mapp(n + 1);
        vector<int> rec(n + 1);

        for (int i = 0; i <= n; ++i) {
            hu[i] = i;
            lst[i] = i;
            mapp[i] = i;
            rec[i] = i;
        }

        while (q--) {
            int cmd;
            cin >> cmd;
            if (cmd == 1) {
                int a, b;
                cin >> a >> b;
                merge(lst, b, a);
            } else if (cmd == 2) {
                int a, b;
                cin >> a >> b;
                hu[a] = rec[b];
            } else if (cmd == 3) {
                int a_, b_;
                cin >> a_ >> b_;
                int a = rec[a_];
                int b = rec[b_];
                swap(mapp[a], mapp[b]);
                rec[a_] = b;
                rec[b_] = a;
            } else if (cmd == 4) {
                int a;
                cin >> a;
                cout << mapp[find(lst, hu[a])] << endl;
            }
        }
    }
    return 0;
}