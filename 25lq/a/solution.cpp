
#include <iostream>
using namespace std;
using i64 = long long;
int main() {
    i64 count = 0;
    i64 num=2000;
    for (i64 i = 0; i <= num; ++i) {
        for (i64 j = 0; j <= num - i; ++j) {
            for (i64 k = 0; k <= num - i - j; ++k) {
                if ((i * 500 + j * 400 + k * 200)*10000 == 114514 * num * 514) {
                    count++;
                }
            }
        }
    }
    cout << count << endl;
    return 0;
}