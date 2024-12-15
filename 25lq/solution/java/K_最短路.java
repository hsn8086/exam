import java.util.*;
import java.io.*;
class Reader {
    private BufferedReader br;
    private StringTokenizer st;

    public Reader() {
        br = new BufferedReader(new InputStreamReader(System.in));
    }

    String next() {
        while (st == null || !st.hasMoreElements()) {
            try {
                st = new StringTokenizer(br.readLine());
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return st.nextToken();
    }

    int nextInt() {
        return Integer.parseInt(next());
    }

    long nextLong() {
        return Long.parseLong(next());
    }

    void close() throws IOException {
        br.close();
    }
}

class Writer {
    private BufferedWriter bw;

    public Writer() {
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
    }

    void print(String s) throws IOException {
        bw.write(s);
    }

    void println(String s) throws IOException {
        bw.write(s);
        bw.newLine();
    }

    void flush() throws IOException {
        bw.flush();
    }

    void close() throws IOException {
        bw.close();
    }
}
public class Main {
    static class Edge {
        int to;
        long weight;
        
        Edge(int to, long weight) {
            this.to = to;
            this.weight = weight;
        }
    }

    public static Map<Integer, Long> dijkstra(Map<Integer, List<Edge>> edges, int start) {
        Map<Integer, Long> dist = new HashMap<>();
        PriorityQueue<AbstractMap.SimpleEntry<Long, Integer>> pq = 
            new PriorityQueue<>(Comparator.comparingLong(AbstractMap.SimpleEntry::getKey));
        Set<Integer> visited = new HashSet<>();

        dist.put(start, 0L);
        pq.offer(new AbstractMap.SimpleEntry<>(0L, start));

        while (!pq.isEmpty()) {
            int u = pq.poll().getValue();
            if (visited.contains(u)) continue;
            visited.add(u);

            if (!edges.containsKey(u)) continue;
            
            for (Edge edge : edges.get(u)) {
                int v = edge.to;
                long w = edge.weight;
                
                if (!dist.containsKey(v) || dist.get(v) > dist.get(u) + w) {
                    dist.put(v, dist.get(u) + w);
                    pq.offer(new AbstractMap.SimpleEntry<>(dist.get(v), v));
                }
            }
        }
        return dist;
    }

    public static void main(String[] args) {
        Reader sc = new Reader();
        int n = sc.nextInt();
        int m = sc.nextInt();

        long[] points = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            points[i] = sc.nextLong();
        }

        List<Edge>[] edges = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            edges[i] = new ArrayList<>();
        }
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            long w = sc.nextLong();

            edges[u].add(new Edge(v, w + points[v]));
            edges[v].add(new Edge(u, w + points[u]));
        }

        long[] dist = new long[n + 1];
        Arrays.fill(dist, Long.MAX_VALUE);
        boolean[] visited = new boolean[n + 1];
        
        dist[1] = 0L;
        PriorityQueue<AbstractMap.SimpleEntry<Long, Integer>> pq = 
            new PriorityQueue<>(Comparator.comparingLong(AbstractMap.SimpleEntry::getKey));
        pq.offer(new AbstractMap.SimpleEntry<>(0L, 1));

        while (!pq.isEmpty()) {
            int u = pq.poll().getValue();
            if (visited[u]) continue;
            visited[u] = true;

            for (Edge edge : edges[u]) {
                int v = edge.to;
                long w = edge.weight;

                if (dist[v] > dist[u] + w) {
                    dist[v] = dist[u] + w;
                    pq.offer(new AbstractMap.SimpleEntry<>(dist[v], v));
                }
            }
        }

        StringBuilder result = new StringBuilder();
        for (int i = 2; i <= n; i++) {
            if (result.length() > 0) result.append(" ");
            result.append(dist[i] + points[1]);
        }
        
        System.out.println(result.toString());

    }
}