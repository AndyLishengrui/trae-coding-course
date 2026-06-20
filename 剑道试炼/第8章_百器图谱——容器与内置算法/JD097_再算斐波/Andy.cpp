#include <iostream>
#include <vector>
using namespace std;

// 用 vector 存储斐波那契数列，迭代计算
int main() {
    int n;
    cin >> n;
    if (n == 0) { cout << 0 << endl; return 0; }

    vector<long long> fib;
    fib.push_back(0);  // fib[0] = 0
    fib.push_back(1);  // fib[1] = 1
    for (int i = 2; i <= n; i++) {
        fib.push_back(fib[i - 1] + fib[i - 2]);
    }
    cout << fib[n] << endl;
    return 0;
}
