#include <iostream>
#include <algorithm>
using namespace std;

void quickSort(long long nums[], int left, int right) {
    if (left >= right) return;
    long long pivot = nums[left];
    int i = left - 1, j = right + 1;
    while (i < j) {
        do i++; while (nums[i] < pivot);
        do j--; while (nums[j] > pivot);
        if (i < j) swap(nums[i], nums[j]);
    }
    quickSort(nums, left, j);
    quickSort(nums, j + 1, right);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    long long* nums = new long long[n];
    for (int i = 0; i < n; i++) cin >> nums[i];
    quickSort(nums, 0, n - 1);
    for (int i = 0; i < n; i++) cout << nums[i] << " ";
    cout << endl;
    delete[] nums;
    return 0;
}