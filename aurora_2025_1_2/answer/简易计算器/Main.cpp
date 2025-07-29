#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <cctype>
#include <sstream>

using namespace std;

int main() {
    string str;
    getline(cin, str);

    vector<string> nums;
    int n = str.size();
    int i = 0;
    while (i < n) {
        if (isdigit(str[i])) {
            int start = i;
            while (i < n && isdigit(str[i])) i++;
            nums.push_back(str.substr(start, i - start));
        }
        else i++;
    }
    if (nums.empty()) return 0;

    stack<long long> st;
    stack<int> signal;

    st.push(stoll(nums[0]));
    int index = 1;

    for (char c : str) {
        if (c == '+') {
            while (!signal.empty() && signal.top() == 1) {
                long long a = st.top(); st.pop();
                long long b = st.top(); st.pop();
                st.push(a * b);
                signal.pop();
            }
            signal.push(0);
            st.push(stoll(nums[index++]));
        }
        else if (c == '*') {
            signal.push(1);
            st.push(stoll(nums[index++]));
        }
    }

    while (!signal.empty()) {
        int op = signal.top();
        signal.pop();
        long long a = st.top(); st.pop();
        long long b = st.top(); st.pop();
        if (op == 0) st.push(a + b);
        else st.push(a * b);
    }

    cout << st.top() << endl;

    return 0;
}