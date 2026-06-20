#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int x, y;
    cin >> x >> y;

    if (x > y) swap(x, y);

    int sum = 0;
    int i = x + 1;
    while (i < y)
    {
      if (i % 2) sum += i;
      i ++;
    }
    cout << sum << endl;

    return 0;
}