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
    public static void main(String[] args) throws IOException {
        Reader reader = new Reader();
        Writer writer = new Writer();
        
        int n = reader.nextInt();
        int m = reader.nextInt();
        int start_x = reader.nextInt() - 1;
        int start_y = reader.nextInt() - 1;
        int end_x = reader.nextInt() - 1;
        int end_y = reader.nextInt() - 1;
        
        String[] matrix = new String[n];
        for (int i = 0; i < n; i++) {
            matrix[i] = reader.next();
        }
        
        int[][] dist = new int[n][m];
        for(int[] row : dist) {
            Arrays.fill(row, Integer.MAX_VALUE);
        }
        dist[start_x][start_y] = 0;
        
        Deque<int[]> queue = new ArrayDeque<>();
        queue.addFirst(new int[]{start_x, start_y});
        
        int[] dx_lst = {-1, 1, 0, 0};
        int[] dy_lst = {0, 0, -1, 1};
        
        while (!queue.isEmpty()) {
            int[] current = queue.pollFirst();
            int x = current[0];
            int y = current[1];
            
            if (x == end_x && y == end_y) {
                break;
            }
            
            // 向相邻位置移动
            for(int i = 0;i<dx_lst.length;i++) {
                int nx = x + dx_lst[i];
                int ny = y + dy_lst[i];
                if(nx >=0 && nx < n && ny >=0 && ny < m && matrix[nx].charAt(ny) == '.' && dist[nx][ny] > dist[x][y]){
                    dist[nx][ny] = dist[x][y];
                    queue.addFirst(new int[]{nx, ny});
                }
            }
            
            // 使用传送魔法
            for(int i = x-2;i<=x+2;i++) {
                for(int j = y-2;j<=y+2;j++) {
                    if(i >=0 && i < n && j >=0 && j < m && matrix[i].charAt(j) == '.' && dist[i][j] > dist[x][y]+1){
                        dist[i][j] = dist[x][y]+1;
                        queue.addLast(new int[]{i,j});
                    }
                }
            }
        }
        
        if(dist[end_x][end_y] == Integer.MAX_VALUE){
            writer.println("-1");
        } else{
            writer.println(String.valueOf(dist[end_x][end_y]));
        }
        
        writer.flush();
        reader.close();
        writer.close();
    }
}