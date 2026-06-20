#include <iostream>

using namespace std;

// 辗转相除法求最大公约数
// gcd(a, b) = gcd(b, a%b)，当 b==0 时返回 a
int gcd(int a, int b)
{
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main()
{
    int a, b;
    cin >> a >> b;
    cout << gcd(a, b) << endl;

    return 0;
}
