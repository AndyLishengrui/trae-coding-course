#include <iostream>
#include <cstring>

using namespace std;

const int N = 110;

void copy(int a[], int b[], int size)
{
    memcpy(b, a, size * 4);
}

int main()
{
    int a[N], b[N];
    int n, m, size;
    cin >> n >> m >> size;
    for (int i = 0; i < n; i ++ ) cin >> a[i];
    for (int i = 0; i < m; i ++ ) cin >> b[i];

    copy(a, b, size);

    for (int i = 0; i < m; i ++ ) cout << b[i] << ' ';
    cout << endl;

    return 0;
}
