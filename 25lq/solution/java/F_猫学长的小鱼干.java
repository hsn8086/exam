
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        
        Arrays.sort(a);
        
        StringBuilder sb = new StringBuilder();
        for (int i = n - m; i < n; i++) {
            if (i > n - m) sb.append(" ");
            sb.append(a[i]);
        }
        
        System.out.println(sb.toString());
        sc.close();
    }
}