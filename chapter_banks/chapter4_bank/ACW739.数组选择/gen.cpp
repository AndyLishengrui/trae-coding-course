#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc,char*argv[]){
    int tc=argc>1?atoi(argv[1]):1;
    srand(time(0)+tc*1000);
    switch(tc){
        case 1:for(int j=0;j<100;j++)printf("%.1f ",(rand()%200-100)*1.0);break;
        case 2:for(int j=0;j<100;j++)printf("%.1f ",(rand()%200-100)*1.0);break;
        case 3:for(int j=0;j<100;j++)printf("%.1f ",(rand()%2000-1000)*0.1);break;
        case 4:for(int j=0;j<100;j++)printf("%.1f ",(rand()%2000-1000)*0.1);break;
        case 5:for(int j=0;j<100;j++)printf("%.1f ",(rand()%2000-1000)*0.1);break;
        case 6:for(int j=0;j<100;j++)printf("%.1f ",(rand()%2000-1000)*0.1);break;
        case 7:for(int j=0;j<100;j++)printf("%.1f ",(rand()%2000-1000)*0.1);break;
        case 8:for(int j=0;j<100;j++)printf("%.1f ",(rand()%2000-1000)*0.1);break;
        case 9:for(int j=0;j<100;j++)printf("%.1f ",(rand()%2000-1000)*0.1);break;
        case 10:for(int j=0;j<100;j++)printf("%.1f ",(rand()%2000-1000)*0.1);break;
    }
    return 0;
}
