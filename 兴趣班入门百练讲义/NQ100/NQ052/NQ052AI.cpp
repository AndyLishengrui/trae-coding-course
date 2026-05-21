#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

void quicksort(vector<long long>& nums, int left, int right) {
  if (left >= right) return;
  // 随机选择分割数，或者使用“三数取中”法
  int pivotIndex = left + rand() % (right - left + 1); 
  swap(nums[pivotIndex], nums[left]); 
  long long target = nums[left];

  int i = left - 1, j = right + 1;
  while (i < j) {
    do i++; while (nums[i] < target);
    do j--; while (nums[j] > target);
    if (i < j) swap(nums[i], nums[j]);
  }

  quicksort(nums, left, j);
  quicksort(nums, j + 1, right);
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  vector<long long> numbers(n);
  for (auto& num : numbers) cin >> num;
  
  quicksort(numbers, 0, n - 1);

  for (const auto& num : numbers) cout << num << " ";

  return 0;
}