#include <iostream>
#include <algorithm>
using namespace std;
const int N = 1007;                        //P进制位最多N位
char a[N], P[36];                          //P进制转换结果,P进制字符映射表，最高36进制
inline char f(int n) { return P[n % 36]; } //把数字转换为字符
int main(){
    //打表法
    for (int i = 0; i < 36; i++)
        P[i] = (i < 10) ? char(i + '0') : char(i - 10 + 'A');
    int n, p;
    //完成p进制的转换
    while (cin >> n >> p)
    {
        if (p>36 || p<=1) continue;//越界忽略
        int minus = 0;
        if (n < 0)
            minus = -1, n = -1 * n;

        int k = 0;
        while (n) {
            a[k] = f(n % p); //转换位相应位数
            k++;
            n /= p;
        }
        if (minus < 0)   cout << "-";
        while (--k >= 0) cout << a[k];
        cout << endl;
    }
    return 0;
}