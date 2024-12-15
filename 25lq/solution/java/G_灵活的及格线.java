import java.util.*;
import java.io.*;

class Reader {
    BufferedReader br;
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
        Reader rd = new Reader();
        Writer wr = new Writer();
        int n = rd.nextInt();
        int q = rd.nextInt();
        
        int[] scores = new int[n];
        for (int i = 0; i < n; i++) {
            scores[i] = rd.nextInt();
        }
        
        Arrays.sort(scores);
        
        for (int i = 0; i < q; i++) {
            int query = rd.nextInt();
            wr.println(String.valueOf(n - bisectLeft(scores, query)));
        }
        
        wr.flush();
        rd.close();
        wr.close();
    }
    
    private static int bisectLeft(int[] arr, int target) {
        int left = 0;
        int right = arr.length;
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
}