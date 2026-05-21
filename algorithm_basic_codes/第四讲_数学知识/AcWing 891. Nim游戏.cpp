// 作者：qiaoxinwei
// 链接：https://www.acwing.com/solution/content/14269/
// 来源：AcWing
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
#include <iostream>
#include <cstdio>
using namespace std;

/*
先手必胜状态：先手操作完，可以走到某一个必败状态
先手必败状态：先手操作完，走不到任何一个必败状态
先手必败状态：a1 ^ a2 ^ a3 ^ ... ^an = 0
先手必胜状态：a1 ^ a2 ^ a3 ^ ... ^an ≠ 0
*/

int main(){
    int n;
    scanf("%d", &n);
    int res = 0;
    for(int i = 0; i < n; i++) {
        int x;
        scanf("%d", &x);
        res ^= x;
    }
    if(res == 0) puts("No");
    else puts("Yes");
}