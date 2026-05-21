// NQ012 水仙花数
#include <cstdio>
int main() {
    int m, n; // 定义范围的起始和结束值
    // 循环读取输入，直到文件结束
    while(scanf("%d %d", &m, &n)!=EOF){
        int cnt=0; // 用于计数水仙花数的个数
        // 遍历从m到n的所有数
        for(int i=m;i<=n;i++){
            // 分解数字的百位、十位和个位
            int a=i/100, b=i%100/10, c=i%10;
            // 计算各位数字的立方和
            int sum=a*a*a + b*b*b + c*c*c;
            // 判断是否为水仙花数
            if(sum==i){
                // 如果不是第一个水仙花数，先输出空格
                if(cnt>0)printf(" ");
                // 输出水仙花数
                printf("%d",i);
                // 计数器加1
                cnt++;
            }
        }
        // 如果没有水仙花数，输出"no"
        if(cnt==0)printf("no");
        // 输出换行
        printf("\n");
    }
    return 0;
}