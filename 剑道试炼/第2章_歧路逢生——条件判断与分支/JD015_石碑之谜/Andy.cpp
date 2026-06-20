#include <iostream>
using namespace std;
int main() {
    int a, b;
    cin >> a >> b;
    // 判断是否互为倍数
    if (a % b == 0 || b % a == 0)
        cout << "Yes" << endl;
    else
        cout << "No" << endl;
    return 0;
}
