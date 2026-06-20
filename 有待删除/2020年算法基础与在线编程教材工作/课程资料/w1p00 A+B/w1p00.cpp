// w1p00 A+B
#include <iostream>
using namespace std;

int main()
{
    int a,b;
    cin >> a >>b;    
    cout <<a + b << endl;
    return 0;
}
//C
#include <stdio.h>

int main()
{
    int a, b;
    scanf("%d%d", &a, &b);
    printf("%d\n", a + b);
    return 0;
}
// python3
import sys

for line in sys.stdin:
    print(sum(map(int, line.split())))