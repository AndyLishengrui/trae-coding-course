#include <iostream>
using namespace std;
int main() {
    int n, x, mx, pos = 1;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> x;
        if (i == 1 || x > mx) { mx = x; pos = i; }
    }
    cout << mx << endl << pos << endl;
    return 0;
}
