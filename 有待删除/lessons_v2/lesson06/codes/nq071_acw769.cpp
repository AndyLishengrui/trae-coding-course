#include <cstdio>
#include <iostream>

using namespace std;

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
