#include <iostream>

using namespace std;

int main()
{
    int a, n;
    cin >> a;
    while (cin >> n, n <= 0);

    int s = 0;
    for (int i = 0; i < n; i ++) s += a + i;

    cout << s << endl;

    return 0;
}