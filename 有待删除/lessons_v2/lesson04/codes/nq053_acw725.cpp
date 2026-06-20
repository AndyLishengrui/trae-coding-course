#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    int perfect[] = {6, 28, 496, 8128};
    for (int x : perfect)
        if (x <= n) cout << x << endl;
    return 0;
}
