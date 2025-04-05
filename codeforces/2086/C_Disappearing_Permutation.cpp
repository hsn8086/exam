#include <iostream>
#include <vector>
using namespace std;

void search(int id_, vector<int>& a, vector<int>& cnt, vector<int>& tag, int start) {
    int stop = start;
    tag[start] = id_;
    start = a[start];
    int cnt_ = 1;
    while (stop != start) {
        tag[start] = id_;
        start = a[start];
        cnt_++;
    }
    cnt[id_] += cnt_;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> a(n + 1);
        for (int i = 1; i <= n; i++) {
            cin >> a[i];
        }
        vector<int> cnt(100010, 0);
        vector<int> tag(100010, 0);
        vector<int> d(n);
        for (int i = 0; i < n; i++) {
            cin >> d[i];
        }

        int id_ = 0;
        for (int i = 1; i <= n; i++) {
            if (!tag[i]) {
                id_++;
                search(id_, a, cnt, tag, i);
            }
        }

        int cnt_ = 0;
        for (int i = 0; i < n; i++) {
            int current_tag = tag[d[i]];
            if (cnt[current_tag]) {
                cnt_ += cnt[current_tag];
                cnt[current_tag] = 0;
            }
            cout << cnt_ << " ";
        }
        cout << endl;
    }
    return 0;
}