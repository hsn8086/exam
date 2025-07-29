import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        while (n-- > 0) {
            //初始工作
            char[] str = sc.nextLine().toCharArray();
            int[] a = new int[12];
            int index = 0;
            for (int i = 0; i < 15; i++) if (str[i] >= '0' && str[i] <= '9') a[index++] = str[i] - 48;

            //计算
            int code = (10 - ((a[0] + a[2] + a[4] + a[6] + a[8] + a[10]) * 3 + a[1] + a[3] + a[5] + a[7] + a[9]) % 10)%10;

            //输出
            System.out.println(code == a[11] ? "Yes" : "No");
        }
    }
}