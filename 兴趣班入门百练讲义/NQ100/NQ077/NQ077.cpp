#include <iostream>
#include <cmath>
#include <algorithm>
#include <functional>   // std::greater
using namespace std;
const int N = 1007; //1000个数
int a[N];

int main()
{
    int q, n, k;
    // 输入数据首先包含一个正整数q，表示包含q组测试用例.
    scanf("%d",&q);
    while ((q--))
    {
        vector<int> nums;
        //创建动态数组
        scanf("%d%d",&n,&k);
        for (int i = 0; i < n; i++)
            scanf("%d",&a[i]);
        // i <> j 
        for (int i = 0; i < n-1; i++)
            for (int j = i+1; j < n; j++)
               nums.push_back(abs(a[i] - a[j])); //插入
  
        //排序,大的摆前面
        sort(nums.begin(),nums.end(),greater<int>());
        
       // 去重，并调整大小
        nums.erase(unique(nums.begin(), nums.end()), nums.end());
        
        printf("%d\n",nums[k-1]);//输出第k大元素(k<=n)
       
    }
    return 0;
}
