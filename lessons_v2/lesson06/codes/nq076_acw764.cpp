#include <iostream>

using namespace std;

int main()
{
    string a, b;
    getline(cin, a);

    for (int i = 0; i < a.size(); i ++ ) b += (char)(a[i] + a[(i + 1) % a.size()]);

    cout << b << endl;

    return 0;
}