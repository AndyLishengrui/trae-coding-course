#include <algorithm>
#include <iostream>
using namespace std;

const int MAX_N = 100005;
int N, C, stalls[MAX_N];

bool canPlace(int distance) {
    int count = 1, last = stalls[0];
    for (int i = 1; i < N; i++) {
        if (stalls[i] - last >= distance) {
            count++;
            last = stalls[i];
            if (count >= C)
                return true;
        }
    }
    return false;
}

int main() {
    scanf("%d%d", &N, &C);
    for (int i = 0; i < N; i++) {
        scanf("%d", &stalls[i]);
    }
    sort(stalls, stalls + N);

    int left = 1, right = stalls[N - 1] - stalls[0];
    while (left < right) {
        int mid = left + (right - left + 1) / 2;
        if (canPlace(mid)) {
            left = mid;
        } else {
            right = mid - 1;
        }
    }
    printf("%d\n", left);

    return 0;
}
