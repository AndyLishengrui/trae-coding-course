// Cody by Andy (参考guowei)
#include <algorithm>
#include <cstring>
#include <functional>
#include <iostream>

using namespace std;

int oriClocks[9];  //时钟的初始状态
int clocks[9];     //计算过程中的时钟状态

//时钟移动的指令数组
string moves[9] = {"ABDE", "ABC",  "BCEF", "ADG", "BDEFH",
                   "CFI",  "DEGH", "GHI",  "EFHI"};
int moveTimes[9] = {0};  // moveTimes[i]的值表示时钟i被拨动的次数

int minTimes = 1 << 30;  //存储最少的拨动次数
int result[9];           //存储最少的拨动方案

//暴力搜索拨动时钟的所有方法数
void dfs(int n) {
  //递归出口
  if (n >= 9) {
    memcpy(clocks, oriClocks, sizeof(clocks));
    int times = 0;
    //把9种move的移动序列用于时钟之上，然后统计移动次数
    for (int i = 0; i < 9; ++i) {
      if (moveTimes[i]) {
        //读取移动的指令，修改时钟状态
        for (int k = 0; k < moves[i].size(); ++k) {
          //根据移动指令moves[i][k]更新对应时钟的状态
          clocks[moves[i][k] - 'A'] =
              (clocks[moves[i][k] - 'A'] + moveTimes[i]) % 4;
          times += moveTimes[i];  //统计移动次数
        }
      }
    }
    //判断是否9个时钟都到12点的位置，也就是clocks[i]全部为0
    bool flag = true;
    for (int i = 0; i < 9; ++i)
      if (clocks[i] != 0) {
        flag = false;
        break;
      }
    //找到一组解
    if (flag && minTimes > times) {
      minTimes = min(minTimes, times);
      memcpy(result, moveTimes, sizeof(result));
    }
    return;
  }

  //每个时钟拨动的次数有4种，一共9个时钟，需要枚举4^9=262,144种情况
  for (int i = 0; i < 4; ++i) {
    moveTimes[n] = i;  //修改n号时钟的拨动次数
    dfs(n + 1);        //递归到下一级的时钟
  }
  return;
}
int main() {
  //读入时钟状态
  for (int i = 0; i < 9; ++i) cin >> oriClocks[i];
  //递归搜索
  dfs(0);
  //输出结果
  for (int i = 0; i < 9; ++i)
    for (int k = 0; k < result[i]; ++k) cout << i + 1 << " ";
  return 0;
}
