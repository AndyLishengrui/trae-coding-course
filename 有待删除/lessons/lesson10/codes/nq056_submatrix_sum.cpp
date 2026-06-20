#include <iostream>
using namespace std;
const int N = 1007;
int n, m, q;
int a[N][N], s[N][N]; //子矩阵

int main()
{
    //读入矩阵
    scanf("%d%d%d", &n, &m, &q);
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            scanf("%d", &a[i][j]);

    s[0][0] = 0; //刻意初始化s[0]为0 ，此句可以不写，写也无妨
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + a[i][j]; //打表法
    //q次询问
    while (q--)
    {
        int x1, x2, y1, y2;
        scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
        //求子矩阵和，直接从s中读取数值
        printf("%d\n", s[x2][y2] - s[x2][y1 - 1] - s[x1 - 1][y2] + s[x1 - 1][y1 - 1]); 
    }
    return 0;
}