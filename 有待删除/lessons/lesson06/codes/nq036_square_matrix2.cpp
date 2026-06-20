#include <iostream>

using namespace std;

int q[100][100];

int main()
{
    int n;
    while (cin >> n, n)
    {
     for (int i = 0; i < n; i ++ )
     {
       q[i][i] = 1;
       for (int j = i + 1, k = 2; j < n; j ++ , k ++ ) q[i][j] = k;
       for (int j = i + 1, k = 2; j < n; j ++ , k ++ ) q[j][i] = k;
     }

     for (int i = 0; i < n; i ++ )
     {
       for (int j = 0; j < n; j ++ ) cout << q[i][j] << ' ';
       cout << endl;
     }
     cout << endl;
    }

    return 0;
}