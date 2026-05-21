//NQ010 小鲁记账
#include <cstdio>
int main(){
    int n, a, b, c;
    float d;
    while(scanf("%d", &n) && n!=0){  // 读取n，n=0时结束
        a=0;b=0;c=0;  // a:负数, b:零, c:正数
        for(int i=1;i<=n;i++){
            scanf("%f", &d);
            if(d==0)b++;  // 统计零
            else if(d<0)a++;  // 统计负数
            else c++;  // 统计正数
        }
        printf("%d %d %d\n",a,b,c);  // 输出结果
    }
    return 0;
}