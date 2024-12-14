# Dijkstra
## Code
``` cpp

struct edge {
  int v, w;
};

struct node {
  int dis, u;

  bool operator>(const node& a) const { return dis > a.dis; }
};

vector<edge> e[MAXN];
int dis[MAXN], vis[MAXN];
priority_queue<node, vector<node>, greater<node>> q;

void dijkstra(int n, int s) {
  memset(dis, 0x3f, (n + 1) * sizeof(int));
  memset(vis, 0, (n + 1) * sizeof(int));
  dis[s] = 0;
  q.push({0, s});
  while (!q.empty()) {
    int u = q.top().u;
    q.pop();
    if (vis[u]) continue;
    vis[u] = 1;
    for (auto ed : e[u]) {
      int v = ed.v, w = ed.w;
      if (dis[v] > dis[u] + w) {
        dis[v] = dis[u] + w;
        q.push({dis[v], v});
      }
    }
  }
}

```

``` python
def dijkstra(graph, start):
    """
    Parameters:
    graph: adjacency list representation of the graph
    start: starting vertex

    Returns:
    distances: dictionary containing shortest distances from start to all vertices
    """
    distances = defaultdict(lambda: float("inf"))
    distances[start] = 0
    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        _, current = heapq.heappop(priority_queue)
        if current in visited:
            continue
        visited.add(current)
        for neighbor, weight in graph[current]:
            if distances[neighbor] > distances[current] + weight:
                distances[neighbor] = distances[current] + weight
                heapq.heappush(priority_queue, (distances[neighbor], neighbor))
    
    return distances
```