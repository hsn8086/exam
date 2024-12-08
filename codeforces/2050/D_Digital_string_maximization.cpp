#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  int ntc;
  cin >> ntc;

  while (ntc--) {
    string s;
    cin >> s;
    vector<int> inp;
    for (char c : s) {
      inp.push_back(c - '0');
    }

    bool flag = true;
    while (flag) {
      flag = false;
      for (int i = inp.size() - 1; i > 0; i--) {
        if (inp[i] - 1 > inp[i - 1]) {
          // swap
          int temp = inp[i - 1];
          inp[i - 1] = inp[i] - 1;
          inp[i] = temp;
          flag = true;
        }
      }
    }

    for (int num : inp) {
      cout << num;
    }
    cout << endl;
  }

  return 0;
}
