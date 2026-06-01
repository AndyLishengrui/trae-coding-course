#include <iostream>
using namespace std;
int main() {
    int n, x, mn, pos = 0;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> x;
        if (i == 0 || x < mn) { mn = x; pos = i; }
    }
    cout << "Menor valor: " << mn << endl;
    cout << "Posicao: " << pos << endl;
    return 0;
}
