#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

//求约数，返回值存在vector之中
vector<int> get_divisors(int n)
{
    vector<int> res;

    for (int i = 1; i <= n / i; i++)
        if (n % i == 0) //是n的约数
        {
            res.push_back(i); //i如果是约数
            if (i != n / i)
                res.push_back(n / i); // n/i也是约数
        }
    //排序
    sort(res.begin(), res.end()); //使用算法sort排序
    return res;
}

int main()
{
    int n; cin >> n; //读入n
    while (n--)
    {
        int a;cin >> a;             //读入a
        auto res = get_divisors(a); //使用auto自动判定属性
        for (auto i : res) cout << i << ' ';
        cout << endl;
    }
    return 0;
}