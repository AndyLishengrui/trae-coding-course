#include <iostream>
#include <memory>
#include <vector>
#include <cmath>
using namespace std;

// 搜索区间[0, n)，升序，寻找target的左边界
int lowerBound(const vector<long long>& nums, long long target) {
    int left = 0, right = nums.size();
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] >= target) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
}

// 搜索区间[0, n)，升序，寻找target的右边界
int upperBound(const vector<long long>& nums, long long target) {
    int left = 0, right = nums.size();
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] <= target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left - 1; // 返回右边界的索引，注意减1
}

int main() {
    int n, m;
    long long target;
    
    cin >> n;
    vector<long long> numbers(n); // 使用vector替代动态数组
    for (int i = 0; i < n; i++) {
        cin >> numbers[i];
    }
    
    cin >> m; // 读入m组查询的数
    while (m--) {
        cin >> target;
        
        // 输入数据在范围之外，直接输出结果
        if (target <= numbers.front()) {
            cout << numbers.front() << endl;
            continue;
        }
        if (target >= numbers.back()) {
            cout << numbers.back() << endl;
            continue;
        }
        
        // 二分查找
        int leftIdx = lowerBound(numbers, target); // 寻找target的左边界
        int rightIdx = upperBound(numbers, target); // 寻找target的右边界
        
        long long leftNum = numbers[leftIdx - 1]; // 左边界左边的数
        long long rightNum = numbers[rightIdx]; // 右边界的数
        
        // 输出最接近的元素
        long long foundNumber = (target - leftNum <= rightNum - target) ? rightNum : leftNum;
        cout << foundNumber << endl;
    }
    
    return 0;
}