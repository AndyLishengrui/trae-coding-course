#include <iostream>
using namespace std;
const int N = 1000007;
int n, m;
int a[N], b[N];

//差分的插入公式
void insert(int l, int r, int c)
{
    b[l] += c;
    b[r + 1] -= c;
}

int main()
{
    cin >> n >> m;
    //读入数组
    for (int i = 1; i <= n; i++)
        cin >> a[i];
    //构造差分数组b
    for (int i = 1; i <= n; i++)
        insert(i, i, a[i]);
    //输出查询结果
    while (m--)
    {
        int l, r, c;
        cin >> l >> r >> c;
        insert(l, r, c);
    }
    //重新复原a数组(前缀和)
    for (int i = 1; i <= n; i++)
        a[i] = a[i - 1] + b[i];
    //输出a
    for (int i = 1; i <= n; i++)
        cout << a[i] << " ";
    cout << endl;
    return 0;
}
