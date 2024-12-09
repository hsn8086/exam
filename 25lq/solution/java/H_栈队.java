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
        Reader reader = new Reader();
        Writer writer = new Writer();
        
        int n = reader.nextInt();
        int m = reader.nextInt();
        int q = reader.nextInt();
        
        Stack<Integer> stack = new Stack<>();
        Queue<Integer> queue = new LinkedList<>();
        Set<Integer> elements = new HashSet<>();
        
        for(int i = 0; i < q; i++) {
            String[] cmd = reader.br.readLine().split(" ");
            int op = Integer.parseInt(cmd[0]);
            switch(op) {
                case 1:
                    int x = Integer.parseInt(cmd[1]);
                    if(stack.size() < n){
                        stack.push(x);
                        elements.add(x);
                    }
                    break;
                case 2:
                    x = Integer.parseInt(cmd[1]);
                    if(queue.size() < m){
                        queue.add(x);
                        elements.add(x);
                    }
                    break;
                case 3:
                    if(!stack.isEmpty()){
                        int temp = stack.pop();
                        elements.remove(temp);
                        if(queue.size() < m){
                            queue.add(temp);
                            elements.add(temp);
                        }
                    }
                    break;
                case 4:
                    if(!queue.isEmpty()){
                        int temp = queue.poll();
                        elements.remove(temp);
                        if(stack.size() < n){
                            stack.push(temp);
                            elements.add(temp);
                        }
                    }
                    break;
                case 5:
                    if(!stack.isEmpty()){
                        writer.println(String.valueOf(stack.peek()));
                    }
                    else{
                        writer.println("SE");
                    }
                    break;
                case 6:
                    if(!queue.isEmpty()){
                        writer.println(String.valueOf(queue.peek()));
                    }
                    else{
                        writer.println("QE");
                    }
                    break;
                case 7:
                    int x7 = Integer.parseInt(cmd[1]);
                    if(elements.contains(x7)){
                        writer.println("YES");
                    }
                    else{
                        writer.println("NO");
                    }
                    break;
                default:
                    // 未知操作
                    break;
            }
        }
        
        writer.flush();
        reader.close();
        writer.close();
    }
}