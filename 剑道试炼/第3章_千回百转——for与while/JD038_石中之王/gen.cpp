#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc,char*argv[]){
    int tc=argc>1?atoi(argv[1]):1;
    srand(time(0)+tc*1000);
    switch(tc){
        case 1: cout<<"5 3 2 5 1 4"<<endl; break;
        case 2: cout<<"5 3 2 5 1 4"<<endl; break;
        case 3: cout<<"3 1 1 1"<<endl; break;
        case 4: cout<<"3 1 1 1"<<endl; break;
        case 5: printf("%d ",rand()%10+1); for(int j=0;j<5;j++)printf("%d ",rand()%100);	printf(" "); break;
        case 6: printf("%d ",rand()%10+1); for(int j=0;j<5;j++)printf("%d ",rand()%100);	printf(" "); break;
        case 7: printf("%d ",rand()%10+1); for(int j=0;j<5;j++)printf("%d ",rand()%100);	printf(" "); break;
        case 8: printf("%d ",rand()%100+1); for(int j=0;j<20;j++)printf("%d ",rand()%1000); printf(" "); break;
        case 9: printf("%d ",rand()%100+1); for(int j=0;j<20;j++)printf("%d ",rand()%1000); printf(" "); break;
        case 10: printf("%d ",rand()%100+1); for(int j=0;j<20;j++)printf("%d ",rand()%1000); printf(" "); break;
    }
    return 0;
}
