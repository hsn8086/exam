#include <iostream>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        map<string, int> ct;
        for (int i = 0; i < n; i++) {
            string s;
            cin >> s;
            ct[s]++;
        }
        int result = ct["Au"] + min(ct["Ag"], ct["Cu"]);
        cout << result << endl;
    }
    return 0;
}