#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    long long a = 0, b = 1;
    for (int i = 0; i < n; i++) {
        if (i) cout << " ";
        cout << a;
        long long t = a + b; a = b; b = t;
    }
    cout << endl;
    return 0;
}
