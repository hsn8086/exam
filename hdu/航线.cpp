#include <bits/stdc++.h>
using namespace std;

#define INF 1e9
#define MAXN 100005

// 定义最多 (n * m * 5) 个节点（每个点5种状态）
const int MAXV = MAXN * 5;
vector<pair<int, int>> adj[MAXV];
int dis[MAXV];
bool vis[MAXV];

inline int getId(int i, int j, int k, int m) {
    return (i * m + j) * 5 + k;
}

void dijkstra(int s, int V) {
    fill(dis, dis + V, INF);
    fill(vis, vis + V, false);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
    dis[s] = 0;
    pq.push({0, s});
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (vis[u]) continue;
        vis[u] = true;
        for (auto [v, w] : adj[u]) {
            if (dis[v] > dis[u] + w) {
                dis[v] = dis[u] + w;
                pq.push({dis[v], v});
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    while (T--) {
        int n, m; cin >> n >> m;
        if (n == 1 && m == 1) {
            int x; cin >> x;
            cout << x * 2 << '\n';
            int dummy; cin >> dummy; // ignore second line
            continue;
        }

        int V = n * m * 5;
        for (int i = 0; i < V; ++i) adj[i].clear();

        int fd = -1;

        // 第一部分：构建上下左右连接图
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                int v; cin >> v;
                if (fd == -1) fd = v;
                int base = i * m + j;

                // 右
                if (j < m - 1) {
                    int u1 = getId(i, j + 1, 3, m);
                    int u2 = getId(i, j, 3, m);
                    adj[u1].emplace_back(u2, v);
                }
                // 下
                if (i < n - 1) {
                    int u1 = getId(i + 1, j, 0, m);
                    int u2 = getId(i, j, 0, m);
                    adj[u1].emplace_back(u2, v);
                }
                // 上
                if (i > 0) {
                    int u1 = getId(i - 1, j, 2, m);
                    int u2 = getId(i, j, 2, m);
                    adj[u1].emplace_back(u2, v);
                }
                // 左
                if (j > 0) {
                    int u1 = getId(i, j - 1, 1, m);
                    int u2 = getId(i, j, 1, m);
                    adj[u1].emplace_back(u2, v);
                }
            }
        }

        // 第二部分：构建五态互通图
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                int v; cin >> v;
                int id[5];
                for (int k = 0; k < 5; ++k)
                    id[k] = getId(i, j, k, m);
                adj[id[0]].emplace_back(id[1], v);
                adj[id[0]].emplace_back(id[4], v);
                adj[id[1]].emplace_back(id[2], v);
                adj[id[1]].emplace_back(id[0], v);
                adj[id[2]].emplace_back(id[3], v);
                adj[id[2]].emplace_back(id[1], v);
                adj[id[3]].emplace_back(id[4], v);
                adj[id[3]].emplace_back(id[2], v);
                adj[id[4]].emplace_back(id[1], v);
                adj[id[4]].emplace_back(id[3], v);
            }
        }

        int start = getId(0, 0, 0, m);
        dijkstra(start, V);

        int ans = INF;
        for (int i = 0; i < 4; ++i) {
            int id = getId(n - 1, m - 1, i, m);
            ans = min(ans, dis[id] + fd);
        }
        cout << ans << '\n';
    }

    return 0;
}
