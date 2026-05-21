// NQ024 珠穆朗玛峰测距
#include <cmath>
#include <cstdio>
int main() {
    int c;
    double x,y,m,n;
    scanf("%d",&c);
    while(c--){
        scanf("%lf %lf %lf %lf",&x,&y,&m,&n);
        double d=sqrt((x-m)*(x-m)+(y-n)*(y-n));  // 计算欧几里得距离
        printf("%.1lf\n",d);  // 输出保留一位小数
    }
    return 0;
}