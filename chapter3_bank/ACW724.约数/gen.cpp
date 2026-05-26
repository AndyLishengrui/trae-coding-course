#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc,char*argv[]){
    int tc=argc>1?atoi(argv[1]):1;
    srand(time(0)+tc*1000);
    switch(tc){
        case 1: cout<<"6"<<endl; break;
        case 2: cout<<"6"<<endl; break;
        case 3: cout<<"1"<<endl; break;
        case 4: cout<<"1"<<endl; break;
        case 5: cout<<rand()%1000+1<<endl; break;
        case 6: cout<<rand()%1000+1<<endl; break;
        case 7: cout<<rand()%1000+1<<endl; break;
        case 8: cout<<rand()%100000+1000<<endl; break;
        case 9: cout<<rand()%100000+1000<<endl; break;
        case 10: cout<<rand()%100000+1000<<endl; break;
    }
    return 0;
}
