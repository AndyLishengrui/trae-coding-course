#include <iostream>

using namespace std;

// 经文重构：按规则构造新字符串
int main()
{
    string a, b;
    getline(cin, a);

    for (int i = 0; i < a.size(); i ++ ) b += (char)(a[i] + a[(i + 1) % a.size()]);

    cout << b << endl;

    return 0;
}
