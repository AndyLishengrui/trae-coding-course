#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 1010;

int n;
int q[N];

int main()
{
    cin >> n;
    for (int i = 0; i < n; i ++ ) cin >> q[i];

    sort(q, q + n);

    int k = 1;
    for (int i = 1; i < n; i ++ )
        if (q[i] != q[k - 1])
            q[k ++ ] = q[i];
    cout << k << endl;
    return 0;
}