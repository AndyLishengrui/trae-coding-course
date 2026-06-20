#include <iostream>

using namespace std;
//数据规模较大
const int N = 1000010;
int q[N];//全局数组

int quick_sort(int q[], int l, int r, int k)
{
    //递归终止：左指针与右指针重叠或者越过
    if (l >= r) return q[l];
    //左右指针为两边界之前的位置，分区点x取区间中点
    int i = l - 1, j = r + 1, x = q[l + r >> 1];

    while (i < j)
    {
        do i ++ ; while (q[i] < x);//移动左指针
        do j -- ; while (q[j] > x);//移动右指针
        if (i < j) swap(q[i], q[j]);//交换
    }
    //判断哪个分支需要递归 
    int sl= j - l + 1; //左区间长度为SL= j-l+1
    if (sl >= k) return quick_sort(q, l, j, k);
    else return quick_sort(q, j + 1, r, k - sl);
}

int main()
{
    int n, k;
    scanf("%d%d", &n, &k);
    //使用scanf比较快
    for (int i = 0; i < n; i ++ ) scanf("%d", &q[i]);
    //输出第k个数
    cout << quick_sort(q, 0, n - 1, k) << endl;

    return 0;
}