#include <iostream>
#include <vector>
#include <unordered_map>
#include <cstring>

using namespace std;

const int MAX_N = 200011;  // Adjust based on constraints

vector<bool> visited(MAX_N, false);
vector<bool> in_stack(MAX_N, false);
int cycle_edges = 0;

unordered_map<int, vector<int>> graph;

void dfs(int node, int parent) {
    visited[node] = true;
    in_stack[node] = true;

    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            dfs(neighbor, node);
        } else if (in_stack[neighbor] && neighbor != parent) {
            cycle_edges++;
        }
    }

    in_stack[node] = false;
}

int max_acyclic_subgraph(int n) {
    cycle_edges = 0;
    fill(visited.begin(), visited.end(), false);
    fill(in_stack.begin(), in_stack.end(), false);

    for (auto& [node, _] : graph) {
        if (!visited[node]) {
            dfs(node, -1);
        }
    }

    return cycle_edges;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    cout << max_acyclic_subgraph(n) << endl;

    return 0;
}