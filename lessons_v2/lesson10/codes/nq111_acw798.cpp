#include <iostream>
using namespace std;
const int N = 1007;
int n, m, q;
int a[N][N], b[N][N]; //子矩阵
//二维差分核心操作
void insert(int x1, int y1, int x2, int y2, int c)
{
    b[x1][y1] += c;
    b[x1][y2 + 1] -= c;
    b[x2 + 1][y1] -= c;
    b[x2 + 1][y2 + 1] += c;
}
int main()
{
    //读入矩阵
    scanf("%d%d%d", &n, &m, &q);
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            scanf("%d", &a[i][j]);

    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            insert(i, j, i, j, a[i][j]); //构造二维差分矩阵

    //q次询问
    while (q--)
    {
        int x1, x2, y1, y2, c;
        scanf("%d%d%d%d%d", &x1, &y1, &x2, &y2, &c);
        //差分核心操作
        insert(x1, y1, x2, y2, c);
    }
    //重建a[][],即求二维前缀和
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            a[i][j] = a[i - 1][j] + a[i][j - 1] - a[i - 1][j - 1] + b[i][j];
    //输出a[][]
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
            cout << a[i][j] << " ";
        cout << endl;
    }
    return 0;
}