#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
    int N;
    scanf("%d",&N);
    for(int a = 2; a <= N; ++a)//a范围[2,N]
        for (int b = 2; b<=a-1; ++b) //b范围[2,a-1]
            for (int c=b; c<=a-1; ++c)//c范围[b,a-1]
                for(int d = c; d<=a-1; ++d)//d范围[c,a-1]
            if( a*a*a == b*b*b + c*c*c +d*d*d)
                printf("Cube = %d, Triple = (%d,%d,%d)\n", a, b, c,d);
    return 0;
}
