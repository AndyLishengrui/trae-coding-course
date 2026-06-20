#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n[20];
    for (int i = 0; i < 20; i++) {
        cin >> n[i];
    }
    for (int i = 0; i < 10; i++) {
        swap(n[i], n[19 - i]);
    }
    for (int i = 0; i < 20; i++) {
        cout << "N[" << i << "] = " << n[i] << endl;
    }
    return 0;
}
