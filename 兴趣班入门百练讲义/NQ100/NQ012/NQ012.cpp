// NQ012 水仙花数
#include <cstdio>

int main() {
  int m, n;
  int count = 0;
  while (scanf("%d %d", &m, &n) != EOF) {
    count = 0;  // 水仙花数计数清零
    for (int i = m; i <= n; i++) {
      // 计算立方和：从个位、十位到百位分别计算求和
      int a, b, c;
      a = i / 100;
      b = i % 100 / 10;
      c = i % 100 % 10;
      int sum = a * a * a + b * b * b + c * c * c;
      // 输出结果
      if (sum == i) {
        if (count > 0) printf(" ");
        printf("%d", i);
        count++;
      }
    }
    // 输出结果（没有水仙花数）和换行
    if (count == 0) printf("no");
    printf("\n");
  }
  return 0;
}