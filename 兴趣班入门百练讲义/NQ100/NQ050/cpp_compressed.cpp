#include <algorithm>
#include <iostream>
#include <vector>

// 算法竞赛题目：排序考试 (Sorting Exam)
// 任务：对T组数据，每组N个整数进行升序排序并输出。

int main() {
  // 1. 优化输入输出速度
  // 在处理大量数据时，关闭 C++ streams 与 C stdio 的同步，并解除 cin 和 cout 的绑定，
  // 可以显著提高 I/O 效率。
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);

  int T = 0;
  // 读取测试用例的数量 T (1 <= T <= 100)
  if (!(std::cin >> T)) {
    return 0;
  }

  // 循环处理 T 组数据
  while (T--) {
    int N = 0;
    // 读取当前数组的元素个数 N (1 <= N <= 1000000)
    if (!(std::cin >> N)) {
      break;
    }

    // 使用动态数组 std::vector 存储 N 个整数
    std::vector<int> nums;
    // 预留空间，减少 vector 动态扩展时产生的性能开销
    nums.reserve(N);

    // 2. 循环读取 N 个整数
    for (int i = 0; i < N; ++i) {
      int num;
      if (std::cin >> num) {
        nums.push_back(num);
      }
    }

    // 3. 核心逻辑：使用 C++ 标准库中的 std::sort 进行排序
    // 时间复杂度为 O(N log N)，是高效的排序方法。
    std::sort(nums.begin(), nums.end());

    // 4. 输出排序结果
    for (int i = 0; i < N; ++i) {
      std::cout << nums[i];
      // 确保元素之间有空格，但行尾没有多余的空格
      if (i < N - 1) {
        std::cout << " ";
      }
    }
    
    // 每组数据输出后换行。使用 '\n' 比 std::endl 更快。
    std::cout << "\n";
  }

  return 0;
}