#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
    int a[1001];
    int n;

    cin >> n;
    for (int i = 0; i < n; i ++ ) cin >> a[i];

    int p = 0;
    for (int i = 1; i < n; i ++ )
        if (a[i] < a[p])
            p = i;

    printf("Minimum value: %d\n", a[p]);        
    printf("Position: %d\n", p);

    return 0;
}