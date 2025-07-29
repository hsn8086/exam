import java.io.*;

public class Main {
    public static StreamTokenizer st = new StreamTokenizer(new InputStreamReader(System.in));
    public static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = nextInt();
        while (T-- > 0) {
            int a = nextInt(),
                    b = nextInt(),
                    c = nextInt(),
                    MAX = Math.max(a, Math.max(b, c)),
                    MIN = Math.min(a, Math.min(b, c)),
                    GCD = gcd(MIN, MAX);//计算最大公约数
            out.printf("%d/%d\n", MIN / GCD, MAX / GCD);
        }
        out.flush();
    }

    //求最大公约数
    public static int gcd(int x, int y) {//辗转相除法
        int z = y;
        while (x % y != 0) {
            z = x % y;
            x = y;
            y = z;
        }
        return z; //返回最小公因数
    }

    public static int nextInt() throws IOException {
        st.nextToken();
        return (int) st.nval;
    }
}
