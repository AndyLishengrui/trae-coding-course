#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc,char*argv[]){
    int tc=argc>1?atoi(argv[1]):1;
    srand(time(0)+tc*1000);
    switch(tc){
        case 1: cout<<"5\n10\n3\n0"<<endl; break;
        case 2: cout<<"5\n10\n3\n0"<<endl; break;
        case 3: cout<<rand()%10+1<<"\n0"<<endl; break;
        case 4: cout<<rand()%10+1<<"\n0"<<endl; break;
        case 5: cout<<rand()%10+1<<"\n0"<<endl; break;
        case 6: cout<<rand()%50+1<<"\n"<<rand()%50+1<<"\n0"<<endl; break;
        case 7: cout<<rand()%50+1<<"\n"<<rand()%50+1<<"\n0"<<endl; break;
        case 8: cout<<rand()%50+1<<"\n"<<rand()%50+1<<"\n0"<<endl; break;
        case 9: cout<<rand()%50+1<<"\n"<<rand()%50+1<<"\n0"<<endl; break;
        case 10: cout<<rand()%50+1<<"\n"<<rand()%50+1<<"\n0"<<endl; break;
    }
    return 0;
}
