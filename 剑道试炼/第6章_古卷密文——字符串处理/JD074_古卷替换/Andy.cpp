#include <iostream>
#include <sstream>

using namespace std;

// 古卷替换：字符串中单词替换
int main()
{
    string s, a, b;

    getline(cin, s);
    cin >> a >> b;

    stringstream ssin(s);
    string str;
    while (ssin >> str)
        if (str == a) cout << b << ' ';
        else cout << str << ' ';

    return 0;    
}
