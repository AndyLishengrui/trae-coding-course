#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    int x;
    int min_val, pos = 0;
    cin >> min_val;
    for (int i = 1; i < N; i++) {
        cin >> x;
        if (x < min_val) {
            min_val = x;
            pos = i;
        }
    }
    cout << "Menor valor: " << min_val << endl;
    cout << "Posicao: " << pos << endl;
    return 0;
}
