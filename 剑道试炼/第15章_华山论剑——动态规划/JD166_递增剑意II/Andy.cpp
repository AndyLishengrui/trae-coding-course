#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 100010;
int q[MAXN]; // q[len] = minimum tail value for LIS of length len

int main() {
    int N;
    scanf("%d", &N);
    int len = 0;
    for (int i = 0; i < N; i++) {
        int a;
        scanf("%d", &a);
        // Find first q[k] >= a using binary search
        int lo = 0, hi = len;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (q[mid] >= a) hi = mid;
            else lo = mid + 1;
        }
        q[lo] = a;
        if (lo == len) len++;
    }
    printf("%d\n", len);
    return 0;
}
