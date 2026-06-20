#include <iostream>
using namespace std;
int main() {
    int m, n;
    while (cin >> m >> n, m > 0 && n > 0) {
        if (m > n) swap(m, n);
        int sum = 0;
        for (int i = m; i <= n; i++) {
            cout << i << " ";
            sum += i;
        }
        cout << "Sum=" << sum << endl;
    }
    return 0;
}
