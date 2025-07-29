#include <iostream>
#include <string>
using namespace std;

int main() {
    int t;
    cin >> t; 
    while (t--) {
        int n;
        string name;
        cin >> n >> name; 
        int rst = -1; 
        for (int i = 0; i < n; i++) {
            string currentName;
            cin >> currentName; 
            if (currentName == name && rst == -1) {
                rst = i + 1; 
            }
        }
        cout << rst << endl; 
    }
    return 0;
}