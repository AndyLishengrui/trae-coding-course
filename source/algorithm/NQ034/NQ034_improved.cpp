// NQ034 求小数点后的数
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    while (n--) { // 循环n次
        double a;
        int t;
        cin >> a >> t;
        // 循环t次，每次将a乘以10
        while (t--) a *= 10.0;
        // 将a转化为整数后取模10，并输出
        // 加上1e-9避免浮点数精度问题（如9.999999999999被误判为9）
        cout << static_cast<int>(a + 1e-9) % 10 << endl;
    }
    return 0;
}