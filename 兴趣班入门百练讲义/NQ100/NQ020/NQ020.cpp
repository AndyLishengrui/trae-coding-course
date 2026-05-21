//NQ020 时钟夹角
#include <cstdio>
#include <cmath>

int main()
{
    int t;
    int h0, m0, s0, x0;
    double h, m, s, n, x; // 用double定义时，分，秒
    // 读取测试数据组数
    scanf("%d", &t);
    while (t--)
    {   
        scanf("%d%d%d", &h0, &m0, &s0);
        // 将初始时间赋值给变量
        h = h0, m = m0, s = s0;
        double c = s / 60.0; // 求出秒针对分针的影响
        m += c; // 秒针影响分针
        double d = m / 60.0; // 分针对时针的影响
        if (h >= 12) h = h - 12; // 每12h时针转一圈
        h += d, m = m * 6 ,h = h * 30; //转换角度 60分钟360'
        // 计算时针和分针之间的夹角
        if (h > m) n = h - m;
        else   n = m - h;
        // 根据夹角大小计算时针和分针之间的最小夹角
        if (n > 180) x = 360 - n;
        else     x = n;
        // 将夹角转换为整数
        x0 = (int)(x);         
        printf("%d\n", x0);// 输出结果
    }

    return 0;
}