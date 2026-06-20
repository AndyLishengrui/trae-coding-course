#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc,char*argv[]){
    int tc=argc>1?atoi(argv[1]):1;
    srand(time(0)+tc*1000);
    switch(tc){
        case 1: cout<<"8"<<endl; break;
        case 2: cout<<"8"<<endl; break;
        case 3: cout<<"0"<<endl; break;
        case 4: cout<<"0"<<endl; break;
        case 5: cout<<rand()%100<<endl; break;
        case 6: cout<<rand()%100<<endl; break;
        case 7: cout<<rand()%100<<endl; break;
        case 8: cout<<rand()%10000+100<<endl; break;
        case 9: cout<<rand()%10000+100<<endl; break;
        case 10: cout<<rand()%10000+100<<endl; break;
    }
    return 0;
}
