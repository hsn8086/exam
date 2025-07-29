import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        String[] nums = str.split("\\D+");//获取全部数字

        Stack<Long> st = new Stack<>();//创建数字栈,符号栈(数字表示优先级)
        Stack<Integer> signal = new Stack<>();
        st.push(Long.valueOf(nums[0]));
        int index = 1;

        for (int i = 0; i < str.length(); i++) {
            char op = str.charAt(i);
            if (op == '+') {
                while (!signal.isEmpty()&&signal.peek() == 1) {//如果为+，且下方有*，则先把*运算完
                    st.push(st.pop() * st.pop());
                    signal.pop();
                }
                signal.push(0);//如果为+且下方无*：直接填入
                st.push(Long.valueOf(nums[index++]));
            } else if (op == '*') {//如果为*直接填入
                signal.push(1);
                st.push(Long.valueOf(nums[index++]));
            }
        }
        while (!signal.isEmpty()) {
            long op = signal.pop();
            if (op == 0) st.push(st.pop() + st.pop());
            else st.push(st.pop() * st.pop());
        }
        System.out.print(st.peek());
        sc.close();
    }
}