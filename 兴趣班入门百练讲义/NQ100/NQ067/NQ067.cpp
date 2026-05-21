#include <iostream>
#include <cstring>
using namespace std;
int n;
//wall[i],当i为奇数时没有完全平铺的方案
int wall[31];//wall[i]表示3行i列的墙一共有多少完全平铺数，wall[1]==0,
int main()
{
    //清零
    memset(wall, 0, sizeof wall);
    //边界值
    wall[0] = 1;  wall[2] = 3;
    //注意递归步长和范围
    for (int i = 4; i <= 30; i += 2) {
        wall[i] = 4 * wall[i - 2] - wall[i - 4];
    }
   //查表得答案
    while(cin >> n, n != -1) {
        cout << wall[n] << endl;
    }
    return 0;
}