#include <iostream>
#include <vector>
#include <map>
#include <cmath>
using namespace std;

int main() {
    int ntc;
    cin >> ntc;
    
    while (ntc--) {
        int k;
        cin >> k;
        

        vector<int> a;
        int temp;
        for (int i = 0; i < k; i++) {
            cin >> temp;
            a.push_back(temp);
        }
        

        map<int, int> count;
        for (int x : a) {
            count[x]++;
        }
        
        int area = k - 2;
        bool found = false;
        

        for (int i = 1; i <= sqrt(area); i++) {
            if (area % i == 0) {
                int j = area / i;
                if (count.find(i) != count.end() && count.find(j) != count.end()) {
                    if (i == j) {
                        if (count[i] >= 2) {
                            cout << i << " " << j << endl;
                            found = true;
                            break;
                        }
                    } else {
                        cout << i << " " << j << endl;
                        found = true;
                        break;
                    }
                }
            }
        }
    }
    return 0;
}