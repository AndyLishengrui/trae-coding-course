#include <iostream>
#include <cmath>
using namespace std;
int main() {
    int n, m;
    float res, a;
    while (cin >> n >> m) {
        res = 0;
        a = n;
        for (int i = 1; i <= m; i++) {
            res += a;
            a = sqrt(a);
        }
        printf("%.2f\n", res);
    }
    return 0;
}