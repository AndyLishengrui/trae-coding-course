#include <cstring>
#include <iostream>
using namespace std;

string Left[3];    //天平左边银币
string Right[3];   //天平右边银币
string result[3];  //称量结果

// islight 为真表示假设假币为轻，否则表示假设假币为重
bool isFeitCoin(char iCoin, bool isLight) {
  string c;//只用string存储Coin
  c.push_back(iCoin);//char转换为string的技巧
  
  for (int i = 0; i < 3; i++) {
    
    //临时变量保存左右称量结果
    string l = Left[i], r = Right[i];  
    
    //如果isLight为假，则在另一端判断
    if (!isLight) swap(l, r);
    // 判定c是否为假币
    switch (result[i][0]) {  //天平右边的情况
      case 'e':              //两端平衡
        if (l.find(c) != string::npos || r.find(c) != string::npos)
          return false;
        break;
      case 'u':  // 右端高
        if (r.find(c) == string::npos) return false;
        break;
      case 'd':  // 右端低
        if (l.find(c) == string::npos) return false;
        break;
    }
  }
  return true;
}

int main() {
  int t;
  cin >> t;
  while (t--) {
    for (int i = 0; i < 3; ++i) 
        cin >> Left[i] >> Right[i] >> result[i];
    //枚举所有银币，是否是假币的所有情况
    for (char iCoin = 'A'; iCoin <= 'L'; iCoin++)
      if (isFeitCoin(iCoin, true)) {
        cout << iCoin << " is the counterfeit coin and it is light. " << endl;
        break;
      } else if (isFeitCoin(iCoin, false)) {
        cout << iCoin << " is the counterfeit coin and it is heavy. " << endl;
        break;
      }
  }

  return 0;
}
