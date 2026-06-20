#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc,char*argv[]){
    int tc=argc>1?atoi(argv[1]):1;
    srand(time(0)+tc*1000);
    switch(tc){
        case 1: cout<<"7 4"<<endl; break;
        case 2: cout<<"7 4"<<endl; break;
        case 3: printf("%d %d ",rand()%10+1,rand()%10+1); break;
        case 4: printf("%d %d ",rand()%10+1,rand()%10+1); break;
        case 5: printf("%d %d ",rand()%10+1,rand()%10+1); break;
        case 6: printf("%d %d ",rand()%20+1,rand()%20+1); break;
        case 7: printf("%d %d ",rand()%20+1,rand()%20+1); break;
        case 8: printf("%d %d ",rand()%20+1,rand()%20+1); break;
        case 9: printf("%d %d ",rand()%20+1,rand()%20+1); break;
        case 10: printf("%d %d ",rand()%20+1,rand()%20+1); break;
    }
    return 0;
}
