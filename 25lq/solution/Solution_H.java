
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