#include <stdio.h>

int fibonacci(int n) {
    if(n == 1 || n == 2) {
        return 1;
    }
    return fibonacci(n-1) + fibonacci(n-2);
}

int main() {
    int n = 5;
    printf("斐波那契数列的第%d项是：%d\n", n, fibonacci(n));
    return 0;
}
