
#include <bitset>
#include <cstring>
#include <iostream>
#include <memory>
using namespace std;

bitset<6> source[5],  //最初灯矩阵，一个比特表示一盏灯
    lights[5],        //不停变化的灯矩阵
    res[5],           //结果按钮矩阵
    line;             //某一行的开关状态

void Output(int t)  //输出结果
{
  cout << "PUZZLE #" << t << endl;
  for (int i = 0; i < 5; ++i) {
    for (int j = 0; j < 6; ++j) {
      cout << res[i][j] << " ";
    }
    cout << endl;
  }
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    //读入最初灯状态
    for (int i = 0; i < 5; i++) {
      for (int j = 0; j < 6; j++) {
        int x;
        cin >> x;
        source[i].set(j, x);  //调用Set
      }
    }
    //遍历首行开关的64种状态
    for (int n = 0; n < 64; ++n) {
      //初始化lights的状态
      for (int i = 0; i < 5; i++) lights[i] = source[i];
      line = n;  //开关状态初始化为n
      
      for (int i = 0; i < 5; ++i) {
      
        res[i] = line;  //存储当前行的开关状态
      
        for (int j = 0; j < 6; ++j) {
          if (line.test(j)) {                  //判断第j位是否是1
            if (j > 0) lights[i].flip(j - 1);  //改左灯
            lights[i].flip(j);                 //改开关位置的灯
            if (j < 5) lights[i].flip(j + 1);  //改右灯
          }
        }
      
        if (i < 4) lights[i + 1] ^= line;  //改下一行的灯
        line = lights[i];  //第i+1行开关方案和第i行灯情况同
      }

      //调用none判断是bitset是否每个位都是0
      if (lights[4].none()) {
        Output(t);
        break;
      }
    }  // for( int n = 0; n < 64; n ++ )
  }
  return 0;
}
