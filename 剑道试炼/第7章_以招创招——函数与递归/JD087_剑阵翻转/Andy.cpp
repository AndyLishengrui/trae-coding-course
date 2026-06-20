#include <iostream>
using namespace std;

const int N = 1010;

// 全局数组自动零初始化
int a[N];

void reverse(int a[], int size)
{
    for (int i = 0, j = size - 1; i < j; i++, j--)
        swap(a[i], a[j]);
}

int main()
{
    int n, size;
    cin >> n >> size;
    for (int i = 0; i < n; i++) cin >> a[i];
    reverse(a, size);

    for (int i = 0; i < n; i++) cout << a[i] << ' ';
    cout << endl;

    return 0;
}
