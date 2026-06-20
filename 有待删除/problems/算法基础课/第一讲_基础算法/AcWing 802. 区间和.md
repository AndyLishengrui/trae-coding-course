# AcWing 802. 区间和 — 区间和

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/802/

## 题目描述

假定有一个无限长的数轴，数轴上每个坐标上的数都是0。

现在，我们首先进行 n 次操作，每次操作将某一位置x上的数加c。

接下来，进行 m 次询问，每个询问包含两个整数l和r，你需要求出在区间[l, r]之间的所有数的和。

### 输入格式

第一行包含两个整数n和m。

接下来 n 行，每行包含两个整数x和c。

再接下里 m 行，每行包含两个整数l和r。

### 输出格式

共m行，每行输出一个询问中所求的区间内数字和。

### 样例

**输入:**
```
3 3
1 2
3 6
7 5
1 3
4 6
7 8
```

**输出:**
```
8
0
5
```

### 提示

原题

## AC代码

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef pair<int, int> PII; //自定义类型PII，表示容器类型是<int,int>的pair

const int N = 300007; //需要记录n个坐标值，以及m个区间的坐标，所以是100000*(1+2)
int n, m;
int a[N], s[N];

vector<int> alls;       //存储所有的点坐标，包括询问点坐标
vector<PII> add, query; //输入操作的坐标，查询的区间坐标
//在alls之中，查找值是x的元素值的下标，并且映射到[1...n]
int find(int x)
{
    int left = 0, right = alls.size() - 1; //vector从0开始计数
    while (left < right)
    {
        int mid = left + right >> 1; //取中值
        if (alls[mid] >= x)
            right = mid;
        else
            left = mid + 1;
    }
    return right + 1; //把坐标值映射到1，2，3...而不是从0开始
}

//? 使用离散化的方式来预处理输入数据
//? 把输入的数字映射成{下标，数字}的pair，然后再用差分的方法计算区间和
//? 本题目可以参考797.差分的模板写成
int main()
{
    cin >> n >> m;
    //!离散化：构造映射表

    for (int i = 0; i < n; i++)
    {
        //todo 不直接把数存入a[i],乃是存入add容器内
        int x, c;
        cin >> x >> c;
        add.push_back({x, c}); //?将某一位置x上的数加c
        alls.push_back(x);     //把x位置加入alls
    }
    // 读入query
    for (int i = 0; i < m; i++)
    {
        int l, r; //区间l和r
        cin >> l >> r;
        query.push_back({l, r});
        alls.push_back(l); //坐标与alls的下标做映射
        alls.push_back(r);
    }
    //alls是下标映射表，需要去重
    //使用STL算法库的sort和unique
    sort(alls.begin(), alls.end());
    //unique返回不重复区间的下一个元素位置，用erase去掉尾部
    alls.erase(unique(alls.begin(), alls.end()), alls.end());

    //针对离散化的数据，计算区间和
    for (auto it : add) //用c++11语法遍历add vector
    {                   //初始化a[i],用离散化后的坐标
        int index = find(it.first);
        a[index] += it.second; //将index位置上的数加c
    }
    //预处理前缀和
    for (int i = 1; i <= alls.size(); i++)
        s[i] = s[i - 1] + a[i];
    //处理询问，并且输出
    for (auto item : query)
    {
        int l = find(item.first), r = find(item.second);
        cout << s[r] - s[l - 1] << endl; //前缀和计算公式
    }
    return 0;
}
```
