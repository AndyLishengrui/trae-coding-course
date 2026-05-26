#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc,char*argv[]){
    int tc=argc>1?atoi(argv[1]):1;
    srand(time(0)+tc*1000);
    switch(tc){
        case 1: cout<<"3\n-5 0 -3 4 -1"<<endl; break;
        case 2: cout<<"3\n-5 0 -3 4 -1"<<endl; break;
        case 3: cout<<"1\n1"<<endl; break;
        case 4: cout<<"1\n1"<<endl; break;
        case 5: printf("%d\n%d\n",rand()%100+1,rand()%100+1); break;
        case 6: printf("%d\n%d\n",rand()%100+1,rand()%100+1); break;
        case 7: printf("%d\n%d\n",rand()%100+1,rand()%100+1); break;
        case 8: printf("%d\n-1 0 -2 %d\n",rand()%10000+1,rand()%10000+1); break;
        case 9: printf("%d\n-1 0 -2 %d\n",rand()%10000+1,rand()%10000+1); break;
        case 10: printf("%d\n-1 0 -2 %d\n",rand()%10000+1,rand()%10000+1); break;
    }
    return 0;
}
