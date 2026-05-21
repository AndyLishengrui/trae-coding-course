//NQ095真假记忆碎片
#include <iostream>
#include <cstring>
using namespace std;
#define For(a, begin, end) for (register int a = begin; a < end; ++a)
using namespace std;
//a为9×9数组，用int类型
int a[9][9]=  
  { {5,3,0,0,7,0,0,0,0},
    {6,0,0,1,9,5,0,0,0},
    {0,9,8,0,0,0,0,6,0},
    {8,0,0,0,6,0,0,0,3},
    {4,0,0,8,0,3,0,0,1},
    {7,0,0,0,2,0,0,0,6},
    {0,6,0,0,0,0,2,8,0},
    {0,0,0,4,1,9,0,0,5},
    {0,0,0,0,8,0,0,7,9}};

int b[9][9];//把输入也转换为int类型
string aline;

bool Check() {
  For(i, 0, 9) {
    cin >> aline;
    if (aline.size() != 9) {
      return false;
    }
    For(j, 0, 9) {
      b[i][j] = aline[j] - '0';  //转为整数
      if (b[i][j] < 1 || b[i][j] > 9) {
        return false;
      }
      if (a[i][j] != 0 && a[i][j] != b[i][j]) {
        return false;
      }
    }
  }

  bool isUsed[10];
  For(i, 0, 9) {
    For(j, 0, 10) isUsed[j] = false;
    For(j, 0, 9) {
      if (isUsed[b[i][j]] == true) {
        return false;
      } else
        isUsed[b[i][j]] = true;
    }
  }

  For(j, 0, 9) {
    For(i, 0, 10) isUsed[i] = false;
    For(i, 0, 9) {
      if (isUsed[b[i][j]] == 1) {
        return false;
      } else
        isUsed[b[i][j]] = true;
    }
  }

  for (int i = 0; i < 9; i += 3) {
    for (int j = 0; j < 9; j += 3) {
      For(k, 0, 10) isUsed[k] = false;
      For(i1, 0, 3) For(j1, 0, 3) if (isUsed[b[i + i1][j + j1]] == 1) {
        return false;
      }
      else isUsed[b[i + i1][j + j1]] = true;
    }
  }
  return true;
} 

int main() {
  if (Check())
    cout << "Yes" << endl;
  else
    cout << "No" << endl;
  return 0;
}
