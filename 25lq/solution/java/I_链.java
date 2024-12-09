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
    public static boolean isChain(int n, int m, List<int[]> edges) {
        if (n == 1) {
            return m == 0;
        }
        if (m != n - 1) { // 链必须有n-1条边
            return false;
        }

        // 构建邻接列表
        List<List<Integer>> matrix = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            matrix.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            matrix.get(edge[0]).add(edge[1]);
            matrix.get(edge[1]).add(edge[0]);
        }

        // 检查度数并统计度数为1的点
        int degreeOne = 0;
        for (int i = 1; i <= n; i++) {
            int deg = matrix.get(i).size();
            if (deg > 2) {
                return false;
            }
            if (deg == 1) {
                degreeOne++;
            }
        }

        // 链必须有2个端点
        if (degreeOne != 2) {
            return false;
        }

        // 找到起点（度数为1的点）
        int start = 0;
        for (int i = 1; i <= n; i++) {
            if (matrix.get(i).size() == 1) {
                start = i;
                break;
            }
        }

        // DFS检查连通性和路径
        boolean[] visited = new boolean[n + 1];
        int pathLen = 0;
        int currNode = start;
        int prevNode = 0;

        while (currNode != 0) {
            visited[currNode] = true;
            pathLen++;

            int nextNode = 0;
            for (int neighbor : matrix.get(currNode)) {
                if (neighbor != prevNode && !visited[neighbor]) {
                    nextNode = neighbor;
                    break;
                }
            }

            prevNode = currNode;
            currNode = nextNode;
        }

        return pathLen == n;
    }

    public static void main(String[] args) throws IOException {
        Reader reader = new Reader();
        Writer writer = new Writer();
        int ntc = reader.nextInt();
        for (int i = 0; i < ntc; i++) {
            int n = reader.nextInt();
            int m = reader.nextInt();
            List<int[]> edges = new ArrayList<>();
            for (int j = 0; j < m; j++) {
                int u = reader.nextInt();
                int v = reader.nextInt();
                edges.add(new int[]{u, v});
            }
            writer.println(isChain(n, m, edges) ? "Yes" : "No");
        }
        writer.flush();
        reader.close();
        writer.close();
    }
}