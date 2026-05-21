//NQ016 十六进制加法
#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    long long a,b;
    cout<<setiosflags(ios::uppercase)<<setbase(16);//输出设置为大写16进制

    while (cin >> hex >> a >> b) // 使用hex操纵器确保十六进制输入
    {
        long long res = a + b;//计算加法
        if(res<0)
            cout << "-" << -(res) << endl;//小于0时手动输出负号。
        else
            cout << res << endl;//正数直接输出
    }
    return 0;
}
