#include <cstdio>

int main()
{
    char str[101];

    fgets(str, 101, stdin);

    int cnt = 0;
    for (int i = 0; str[i]; i ++ )
        if (str[i] >= '0' && str[i] <= '9')
           cnt ++ ;

    printf("%d\n", cnt);

    return 0;
}