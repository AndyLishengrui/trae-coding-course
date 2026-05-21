//NQ010 小鲁记账
#include <cstdio>

int main()
{
    int n, a, b, c;
    float d;
    while(scanf("%d", &n) && n!=0)  //如果n不等于0，持续输入
    {
        a = 0; b = 0; c = 0;
        for(int i = 1; i <= n; i++) //输入n个实数，判断这个数并且计数
        {
            scanf("%f", &d);
            if(d == 0) b++;
            else if(d < 0) a++;
            else c++;
        }
        printf("%d %d %d\n", a, b, c);  //每输完一行，输出结果
    }
    return 0;
}