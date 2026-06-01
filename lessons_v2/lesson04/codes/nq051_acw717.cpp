#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    long long a = 0, b = 1;
    if (n == 0) { cout << 0 << endl; return 0; }
    for (int i = 1; i < n; i++) {
        long long t = a + b; a = b; b = t;
    }
    cout << b << endl;
    return 0;
}
