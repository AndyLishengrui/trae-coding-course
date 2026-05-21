//Andy代码，参考Y总
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int main()
{
    int n; cin>>n;
    while (n -- )
    {
      int a; cin>>a;
      int res = a;
      //分解质因子,用题目公式直接计算
      for (int i = 2; i <= a /i; i++)
      if (a % i == 0)
      {
        res = res /i * (i-1);//取整，调换*与/的次序
        while (a % i == 0) a /=i;
      }

      if (a > 1) res = res /a *(a-1);

      cout<< res<<endl;
    }
    return 0;
}