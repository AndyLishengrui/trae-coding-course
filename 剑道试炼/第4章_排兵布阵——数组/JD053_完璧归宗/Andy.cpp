#include <iostream>
using namespace std;
int main() {
    int perfect[] = {6, 28, 496, 8128, 33550336};
    int n;
    cin >> n;
    for (int x : perfect)
        if (x <= n) cout << x << endl;
    return 0;
}
