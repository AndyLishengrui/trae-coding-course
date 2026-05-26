#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc,char*argv[]){
    int tc=argc>1?atoi(argv[1]):1;
    srand(time(0)+tc*1000);
    switch(tc){
        case 1:cout<<rand()%12<<"\nS\n";for(int j=0;j<144;j++)printf("%.1f\n",(rand()%100)*1.0);break;
        case 2:cout<<rand()%12<<"\nM\n";for(int j=0;j<144;j++)printf("%.1f\n",(rand()%100)*1.0);break;
        case 3:cout<<rand()%12<<"\nS\n";for(int j=0;j<144;j++)printf("%.1f\n",(rand()%100)*1.0);break;
        case 4:cout<<rand()%12<<"\nM\n";for(int j=0;j<144;j++)printf("%.1f\n",(rand()%100)*1.0);break;
        case 5:printf("%d\n%c\n",rand()%12,'S');for(int j=0;j<144;j++)printf("%.1f\n",(rand()%200-100)*1.0);break;
        case 6:printf("%d\n%c\n",rand()%12,'M');for(int j=0;j<144;j++)printf("%.1f\n",(rand()%200-100)*1.0);break;
        case 7:printf("%d\n%c\n",rand()%12,'S');for(int j=0;j<144;j++)printf("%.1f\n",(rand()%200-100)*1.0);break;
        case 8:printf("%d\n%c\n",rand()%12,'M');for(int j=0;j<144;j++)printf("%.1f\n",(rand()%200-100)*1.0);break;
        case 9:printf("%d\n%c\n",rand()%12,'S');for(int j=0;j<144;j++)printf("%.1f\n",(rand()%200-100)*1.0);break;
        case 10:printf("%d\n%c\n",rand()%12,'M');for(int j=0;j<144;j++)printf("%.1f\n",(rand()%200-100)*1.0);break;
    }
    return 0;
}
