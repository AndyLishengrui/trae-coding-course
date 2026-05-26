#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int c;
    char t;
    double m[12][12];

    cin >> c >> t;
    for (int i = 0; i < 12; i ++ )
        for (int j = 0; j < 12; j ++ )
            cin >> m[i][j];

    double s = 0;
    for (int i = 0; i < 12; i ++ ) s += m[i][c];

    if (t == 'S') printf("%.1lf\n", s);
    else printf("%.1lf\n", s / 12);

    return 0;        
}