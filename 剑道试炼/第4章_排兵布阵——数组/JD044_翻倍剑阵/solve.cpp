#include <iostream>
using namespace std;

int main() {
    int V;
    cin >> V;
    long long n[10];
    n[0] = V;
    for (int i = 1; i < 10; i++) {
        n[i] = n[i-1] * 2;
    }
    for (int i = 0; i < 10; i++) {
        cout << "N[" << i << "] = " << n[i] << endl;
    }
    return 0;
}
