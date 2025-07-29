#include <bits/stdc++.h>
using namespace std;

void dfs(const vector<vector<int>>& e, int s, vector<bool>& visited) {
    if (visited[s]) return;
    visited[s] = true;
    cout << s << " ";

    for (int i : e[s]) {
        dfs(e, i, visited);
    }
}

void bfs(const vector<vector<int>>& e, int s) {
    queue<int> q;
    q.push(s);
    vector<bool> visited(e.size(), false);
    visited[s] = true;

    while (!q.empty()) {
        int point = q.front();
        q.pop();
        cout << point << " ";

        for (int i : e[point]) {
            if (visited[i]) continue;
            visited[i] = true;
            q.push(i);
        }
    }
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> e(n + 1);

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        e[u].push_back(v);
    }

    // Sort adjacency lists
    for (auto& lst : e) {
        sort(lst.begin(), lst.end());
    }

    // DFS
    vector<bool> dfs_visited(e.size(), false);
    dfs(e, 1, dfs_visited);
    cout << endl;

    // BFS
    bfs(e, 1);
    cout << endl;

    return 0;
}