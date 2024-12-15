import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] inp = new int[3];
        for (int i = 0; i < 3; i++) {
            inp[i] = scanner.nextInt();
        }
        Arrays.sort(inp);  // 保证a<=b<=c
        int a = inp[0], b = inp[1], c = inp[2];

        // a+b>=c
        int cost = (a + b > c) ? 0 : (c - a - b + 1);
        System.out.println(cost);
        
        scanner.close();
    }
}