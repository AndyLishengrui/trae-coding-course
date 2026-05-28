#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc,char*argv[]){
    int tc=argc>1?atoi(argv[1]):1;
    srand(time(0)+tc*1000);
    switch(tc){
        case 1: cout<<"4\n14\n123\n10 -25"<<endl; break;
        case 2: cout<<"4\n14\n123\n10 -25"<<endl; break;
        case 3: cout<<"3\n10\n20 -1"<<endl; break;
        case 4: cout<<"3\n10\n20 -1"<<endl; break;
        case 5: cout<<rand()%20+5; for(int j=0;j<5;j++)printf(" %d",rand()%200-50); printf(" "); break;
        case 6: cout<<rand()%20+5; for(int j=0;j<5;j++)printf(" %d",rand()%200-50); printf(" "); break;
        case 7: cout<<rand()%20+5; for(int j=0;j<5;j++)printf(" %d",rand()%200-50); printf(" "); break;
        case 8: cout<<rand()%100+10; for(int j=0;j<20;j++)printf(" %d",rand()%200-50); printf(" "); break;
        case 9: cout<<rand()%100+10; for(int j=0;j<20;j++)printf(" %d",rand()%200-50); printf(" "); break;
        case 10: cout<<rand()%100+10; for(int j=0;j<20;j++)printf(" %d",rand()%200-50); printf(" "); break;
    }
    return 0;
}
