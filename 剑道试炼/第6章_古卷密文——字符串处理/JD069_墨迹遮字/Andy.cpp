#include <cstdio>
#include <iostream>

using namespace std;

// 墨迹遮字：字符串中指定字符替换为#
int main()
{
    char str[31];
    scanf("%s", str);

    char c;
    scanf("\n%c", &c);

    for (int i = 0; str[i]; i ++ )
        if (str[i] == c)
            str[i] = '#';

    puts(str);

    return 0;
}
