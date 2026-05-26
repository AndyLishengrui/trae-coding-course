#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
    char t;
    cin >> t;
    double m[12][12];


    for (int i = 0; i < 12; i ++ )
        for (int j = 0; j < 12; j ++ )
            cin >> m[i][j];

    double s = 0, c = 0;
    for (int i = 0; i < 5; i ++ )
        for (int j = i + 1; j <= 10 - i; j ++ )
        {
          c += 1;
          s += m[i][j];
        }
    if (t == 'M') printf("%.1lf\n", s / c);
    else printf("%.1lf\n", s);

    return 0;        
}