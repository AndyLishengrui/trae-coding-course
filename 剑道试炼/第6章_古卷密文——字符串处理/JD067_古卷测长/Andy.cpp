#include <cstdio>

// 古卷测长：输出字符串长度
int main()
{
    char str[101];

    fgets(str, 101, stdin);

    int len = 0;
    for (int i = 0; str[i] && str[i] != '\n'; i ++ ) len ++ ;

    printf("%d\n", len);

    return 0;
}
