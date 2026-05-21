#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 307;

int g[N][N];//地图高度
int f[N][N];//从[i,j]开始滑的最长的轨迹

int n,m;//宽高

int dx[4] = {-1, 0, 1, 0}, dy[4] = {0, 1, 0, -1};

int dp(int x, int y)
{
  //记忆化搜索
  if (f[x][y] != -1) return f[x][y];
  //否则，从x,y开始滑
  f[x][y] = 1;//当前位置至少是1格
  //分上下左右四个方向滑雪
  for (int i = 0; i < 4; i++)
  {
    int a = x + dx[i], b = y + dy[i];
    if (a<1 || a >n || b <1 || b > m) continue;//越界
    if (g[a][b] >= g[x][y]) continue;//不能走
    //四个方向深搜，更新f[a][b],取最大值
    f[x][y] = max(f[x][y], dp(a,b) + 1);
  }

  return f[x][y];//返回f[x][y]
}

int main()
{
    cin>>n>>m;
    //读入高度图
    for (int i = 1; i <= n; i ++ )
     for (int j = 1; j <= m; j ++ )
       cin>>g[i][j];

    memset(f,-1,sizeof f);//初始化为-1，表示该点未被访问

    //把每个点作为起点深搜
    int res = 0;
    for (int i = 1; i <= n; i ++ )
     for (int j = 1; j <= m; j ++ )
       res = max(res,dp(i,j));

    cout <<res <<endl;
    return 0;
}