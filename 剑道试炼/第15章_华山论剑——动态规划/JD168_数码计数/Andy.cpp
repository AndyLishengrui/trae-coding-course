#include <cstdio>
#include <algorithm>
using namespace std;

// Count occurrences of digit d in all numbers from 1 to n
long long countDigit(long long n, int d) {
    if (n <= 0) return 0;
    long long res = 0;
    for (long long p = 1; p <= n; p *= 10) {
        long long high = n / (p * 10);
        int cur = (n / p) % 10;
        long long low = n % p;
        if (d == 0) {
            if (high > 0) {
                res += (high - 1) * p;
                if (cur == 0)
                    res += low + 1;
                else
                    res += p;
            }
        } else {
            res += high * p;
            if (cur == d)
                res += low + 1;
            else if (cur > d)
                res += p;
        }
    }
    return res;
}

int main() {
    long long a, b;
    while (scanf("%lld %lld", &a, &b) == 2) {
        if (a == 0 && b == 0) break;
        long long lo = min(a, b);
        long long hi = max(a, b);
        for (int d = 0; d <= 9; d++) {
            long long ans = countDigit(hi, d) - countDigit(lo - 1, d);
            printf("%lld ", ans);
        }
        printf("\n");
    }
    return 0;
}
