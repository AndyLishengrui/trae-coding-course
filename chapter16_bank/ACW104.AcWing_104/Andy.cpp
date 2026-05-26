#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 100007;

int n;
int a[N];

int main()
{
    cin >> n;
    for (int i = 0; i < n; i ++) cin >> a[i];
    sort(a, a+n);
    int res = 0;
    //中位数a[n/2],求距离之和的最小值
    for (int i = 0; i < n; i ++ ) res += abs(a[i]- a[n/2]);
    cout << res <<endl;
    return 0;
}
