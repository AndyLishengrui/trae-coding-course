#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int x, y, sum = 0;
    cin >> x >> y;
    if (x > y) swap(x, y);
    for (int i = x + 1; i < y; i++)
        if (i % 2) sum += i;
    cout << sum << endl;
    return 0;
}
