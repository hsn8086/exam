
import java.util.ArrayList;
import java.util.Scanner;

public class Solution_L {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();
        int k = Integer.parseInt(scanner.nextLine());
        
        int maxLen = 0;
        int zeros = 0;
        int left = 0;
        int currentOnes = 0;
        
        for (int right = 0; right < s.length(); right++) {
            if (s.charAt(right) == '0') {
                zeros++;
            } else {
                currentOnes++;
            }
            
            while (zeros > k && left < right) {
                if (s.charAt(left) == '0') {
                    zeros--;
                } else {
                    currentOnes--;
                }
                left++;
            }
            
            maxLen = Math.max(maxLen, right - left + 1);
        }
        
        System.out.println(maxLen);
        scanner.close();
    }
}