#include <iostream>
using namespace std;
int main() {
    int x;
    while (cin >> x, x) {
        for (int i = 1; i <= x; i++) {
            if (i > 1) cout << " ";
            cout << i;
        }
        cout << endl;
    }
    return 0;
}
