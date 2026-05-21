// NQ082 试除法分解质因数
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

void divide(int n) {
    for (int i = 2; i <= n / i; i++) // 注意不要用i*i<=n避免溢出
        if (n % i == 0) {
            int nums = 0;
            while (n % i == 0) {
                n /= i;
                nums++;
            }
            printf("%d %d\n", i, nums); // i出现nums次
        }
    // n中只包含一个大于sqrt(n)的质因子
    if (n > 1)
        printf("%d %d\n", n, 1); // n是除掉所有因子后剩下的数
    puts("");                    // 换行
}

int main() {
    int n;
    cin >> n; // 读入n
    while (n--) {
        int a;
        cin >> a;  // 读入a
        divide(a); // 使用auto自动判定属性
    }
    return 0;
}