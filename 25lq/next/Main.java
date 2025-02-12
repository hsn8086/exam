import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
  public static void main(String[] args) {
    FastReader fr = new FastReader();
    int tc = fr.nextInt();

    while (tc-- > 0) {
      solve(fr);
    }
  }

  private static void solve(FastReader fr) {
    long n = fr.nextLong();
    long k = fr.nextLong();
    System.out.println(solve(1, n, k).sum);
  }

  static Pair solve(long left, long right, long k){
    long len = right - left + 1;
    if(len < k) return new Pair(0, 0);

    long mid = (left + right) / 2;

    if((len & 1) == 0){
      Pair leftSubPart = solve(left, mid, k);
      long sum = leftSubPart.sum + (leftSubPart.count * mid) + leftSubPart.sum;
      long elementCount = 2 * leftSubPart.count;
      leftSubPart.count = elementCount;
      leftSubPart.sum = sum;
      return leftSubPart;
    }else{
      Pair leftSubPart = solve(left, mid-1, k);

      long sum = leftSubPart.sum + (leftSubPart.count * mid) + leftSubPart.sum + mid;
      long elementCount = 2 * leftSubPart.count + 1;
      leftSubPart.count = elementCount;
      leftSubPart.sum = sum;
      return leftSubPart;
    }
  }

  static class FastReader {
    BufferedReader br;
    StringTokenizer st;

    public FastReader() {
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

    double nextDouble() {
      return Double.parseDouble(next());
    }

    String nextLine() {
      String str = "";
      try {
        if (st.hasMoreTokens()) {
          str = st.nextToken("\n");
        } else {
          str = br.readLine();
        }
      } catch (IOException e) {
        e.printStackTrace();
      }
      return str;
    }
  }
}

class Pair{
  long sum, count;

  Pair(long s, long c){
    sum = s;
    count = c;
  }
}