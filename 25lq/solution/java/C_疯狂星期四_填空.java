public class Main {
    static boolean checkYear(int year) {
        if (year % 4 != 0) {
            return false;
        } else if (year % 100 != 0) {
            return true;
        } else if (year % 400 != 0) {
            return false;
        } else {
            return true;
        }
    }

    public static void main(String[] args) {
        int start = 2024;
        int startWeekday = 0;
        int end = 114514;

        long sum = 0;
        for (int i = start + 1; i <= end; i++) {
            sum += 365 + (checkYear(i) ? 1 : 0);
        }

        long a = sum / 7;
        long b = sum % 7;
        System.out.println(a + ((b + startWeekday >= 4) ? 1 : 0));
        
        // 请直接提交: System.out.println(5869447);
    }
}