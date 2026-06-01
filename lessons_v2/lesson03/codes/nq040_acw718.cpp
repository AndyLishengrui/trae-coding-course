#include <cstdio>
#include <iostream>
using namespace std;
int main() {
    int n, c = 0, r = 0, f = 0;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int k; char t;
        cin >> k >> t;
        if (t == 'C') c += k;
        else if (t == 'R') r += k;
        else f += k;
    }
    int s = c + r + f;
    printf("Total: %d animals\n", s);
    printf("Total coneys: %d\n", c);
    printf("Total rats: %d\n", r);
    printf("Total frogs: %d\n", f);
    printf("Percentage of coneys: %.2lf %%\n", 100.0 * c / s);
    printf("Percentage of rats: %.2lf %%\n", 100.0 * r / s);
    printf("Percentage of frogs: %.2lf %%\n", 100.0 * f / s);
    return 0;
}
