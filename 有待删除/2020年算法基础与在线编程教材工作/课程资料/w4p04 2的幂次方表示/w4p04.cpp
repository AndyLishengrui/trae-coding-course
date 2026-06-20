#include <iostream>
#include <bitset>
#include <vector>
#include <string>
using namespace std;

vector<string> res;//存储输出的字符串数组

void dfs(int u)
{
    bitset<16> a(u);//把n转换为bitset处理

    //从低位到高位，枚举输入n的每一位
    //整数为16位,所以取15--0位
    bool isFirstOne=true;
    for (int i = 15; i >=0 ; --i)
    {
          //该位为1，不为0，需要输出
        if(a.test(i))
        {
            //如果不是第一个1，那需要加上"+"
            if(!isFirstOne)
            {
                res.push_back("+");
            } else 
                isFirstOne=false;
            //递归出口
            //如果第i位为0，表示只有最低位是1，直接输出2(0)
            if (i==0)
                res.push_back("2(0)");
            else
            if (i==1)
                res.push_back("2");
            else
            {
            //深度优先搜索          
            //对于读到的每一位，输出二进制的新表达式
                res.push_back("2(");
                dfs(i);//why?
                res.push_back(")");
            }
        };
}
}

int main ()
{
    int x; cin>>x;
    dfs(x);
    for (auto l:res) cout<<l;
    cout<<endl;
    return 0;
}
