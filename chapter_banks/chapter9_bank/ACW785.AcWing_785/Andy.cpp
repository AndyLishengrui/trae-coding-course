#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

long long *numbers;

void quicksort(long long nums[], int left, int right)
{
    if (left >= right)
        return;
    //选取分割数
    long long target = nums[left]; //选取第一个快排的分割数
    int i = left - 1, j = right + 1;
    while (i < j)
    {
        do
            i++;
        while (nums[i] < target); //i指针定位
        do
            j--;
        while (nums[j] > target); //j指针定位
        if (i < j)
            swap(nums[i], nums[j]); //交换
    }
    //分治
    quicksort(nums, left, j);      //j左边的都是不比Target大的
    quicksort(nums, j + 1, right); // j右边的都比Target大
}
int main()
{
    //!cin\cout提速
    ios::sync_with_stdio(false); //来打消iostream的输入输出缓存
    cin.tie(0);                  //cin.tie(0)来解除cin与cout的绑定,0表示NULL

    int n;
    //创建动态数组
    cin >> n;
    numbers = new long long[n];
    for (int i = 0; i < n; i++)
        cin >> numbers[i];
    quicksort(numbers, 0, n - 1); //注意边界

    for (int i = 0; i < n; i++)
        cout << numbers[i] << " ";

    delete numbers;
    return 0;
}
