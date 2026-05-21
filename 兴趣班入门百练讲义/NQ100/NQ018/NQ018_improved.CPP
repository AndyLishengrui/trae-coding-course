// NQ018 计算折线长度
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
int main() {
    int x1,y1,x2,y2,n;
    scanf("%d",&n);
    while(n--){
        scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
        if(x1+y1>x2+y2){swap(x1,x2);swap(y1,y2);}
        const int S2=x2+y2;
        double len=0.0;
        const double sqrt2=sqrt(2.0);
        while(x1!=x2||y1!=y2){
            const int S1=x1+y1;
            if(y1==0){
                len+=sqrt(1.0*S1*S1+1.0*(S1+1)*(S1+1));
                x1=0;y1=S1+1;
            }else{
                int steps=S1<S2?y1:x2-x1;
                len+=steps*sqrt2;
                x1+=steps;y1-=steps;
            }
        }
        printf("%.3lf\n",len);
    }
    return 0;
}