#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc,char*argv[]){
    int tc=argc>1?atoi(argv[1]):1;
    srand(time(0)+tc*1000);
    switch(tc){
        case 1:cout<<"10\n1 2 3 4 -5 6 7 8 9 10"<<endl;break;
        case 2:cout<<"10\n1 2 3 4 -5 6 7 8 9 10"<<endl;break;
        case 3:cout<<"3\n100 100 100"<<endl;break;
        case 4:cout<<"3\n100 100 100"<<endl;break;
        case 5:printf("%d\n",rand()%20+5);for(int j=0;j<10;j++)printf("%d ",rand()%100);printf("\n");break;
        case 6:printf("%d\n",rand()%20+5);for(int j=0;j<10;j++)printf("%d ",rand()%100);printf("\n");break;
        case 7:printf("%d\n",rand()%20+5);for(int j=0;j<10;j++)printf("%d ",rand()%100);printf("\n");break;
        case 8:printf("%d\n",rand()%500+10);for(int j=0;j<50;j++)printf("%d ",rand()%1000-500);printf("\n");break;
        case 9:printf("%d\n",rand()%500+10);for(int j=0;j<50;j++)printf("%d ",rand()%1000-500);printf("\n");break;
        case 10:printf("%d\n",rand()%500+10);for(int j=0;j<50;j++)printf("%d ",rand()%1000-500);printf("\n");break;
    }
    return 0;
}
