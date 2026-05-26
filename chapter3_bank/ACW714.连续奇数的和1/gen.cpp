#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc,char*argv[]){
    int tc=argc>1?atoi(argv[1]):1;
    srand(time(0)+tc*1000);
    switch(tc){
        case 1: cout<<"6 -5"<<endl; break;
        case 2: cout<<"6 -5"<<endl; break;
        case 3: cout<<"-3 3"<<endl; break;
        case 4: cout<<"-3 3"<<endl; break;
        case 5: printf("%d %d\n",rand()%50-25,rand()%50-25); break;
        case 6: printf("%d %d\n",rand()%50-25,rand()%50-25); break;
        case 7: printf("%d %d\n",rand()%50-25,rand()%50-25); break;
        case 8: printf("%d %d\n",rand()%5000-2500,rand()%5000-2500); break;
        case 9: printf("%d %d\n",rand()%5000-2500,rand()%5000-2500); break;
        case 10: printf("%d %d\n",rand()%5000-2500,rand()%5000-2500); break;
    }
    return 0;
}
