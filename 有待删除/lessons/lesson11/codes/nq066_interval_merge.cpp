#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef pair<int, int> PII; //自定义类型PII，表示容器类型是<int,int>的pair

const int N = 100007; //1<=n<=100000
int n;//n个区间

vector<PII> segments; //区间坐标

void merge(vector<PII> &segs)
{
    vector<PII> res;
    //pair排序先按左端点，后右端点
    sort(segs.begin(), segs.end());

    //数字范围是-10^9<num<10^9,因此负无穷大初始化为-2e9
    int left = -2e9, right = -2e9;//当前操作的区间[left,right]
    for (auto seg : segs)//遍历segs
        if (right < seg.first)//区间没有交集，更新当前区间
        {
            //存储合并完毕的区间[left,right]
            if (left != -2e9) res.push_back({left, right});
            //更新当前操作区间
            left = seg.first, right = seg.second;
        }
        else right = max(right, seg.second);//更新右端点，扩展区间

    if (left != -2e9) res.push_back({left, right});//把最后一个区间入栈

    segs = res;//更新segs
}

int main()
{
    cin >> n;
    // 读入n组区间
    for (int i = 0; i < n; i++)
    {
        int l, r; //区间l和r
        cin >> l >> r;
        segments.push_back({l, r});
    }
    //合并区间segment
    merge(segments);
    //输出合并后的区间个数
    cout<<segments.size()<<endl;//输出合并后的区间元素个数

    return 0;
}