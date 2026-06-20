#include <iostream>
#include <cstring>

using namespace std;

int cnt[26];
char str[100010];

// 独字寻踪：找第一个不重复字符
int main()
{
    cin >> str;

    for (int i = 0; str[i]; i ++ ) cnt[str[i] - 'a'] ++ ;

    for (int i = 0; str[i]; i ++ )
        if (cnt[str[i] - 'a'] == 1)
        {
          cout << str[i] << endl;
          return 0;
        }

        puts("no");

    return 0;    
}
