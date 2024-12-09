import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine(); // 消耗换行符
        
        for (int i = 1; i <= n; i++) {
            String s = sc.nextLine();
            StringBuilder result = new StringBuilder();
            for (int j = 0; j < i; j++) {
                result.append(s).append("\n");
            }
            System.out.print(result);
        }
        sc.close();
    }
}