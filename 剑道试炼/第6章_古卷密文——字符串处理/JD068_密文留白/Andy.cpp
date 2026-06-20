#include <iostream>

using namespace std;

// 密文留白：每个字符后加空格
int main()
{
    string a;
    getline(cin, a);

    string b;
    for (auto c : a) b = b + c + ' ';

    b.pop_back();

    cout << b << endl;

    return 0;
}
