#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    char op;
    cin >> op;
    double sum = 0;
    int cnt = 0;
    for (int i = 0; i < 12; i++) {
        for (int j = 0; j < 12; j++) {
            double x;
            cin >> x;
            if (i+j>11) {
                sum += x;
                cnt++;
            }
        }
    }
    if (op == 'S') printf("%.1f\n", sum);
    else printf("%.1f\n", sum / cnt);
    return 0;
}
