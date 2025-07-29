#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main() {
    string line;
    while (getline(cin, line)) {
        if (line.empty()) break;
        
        istringstream iss(line);
        int a, b;
        iss >> a >> b;
        cout << a + b << endl;
    }
    return 0;
}