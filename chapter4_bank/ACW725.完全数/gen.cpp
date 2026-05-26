#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc,char*argv[]){
    int tc=argc>1?atoi(argv[1]):1;
    srand(time(0)+tc*1000);
    switch(tc){
        case 1:cout<<"30"<<endl;break;
        case 2:cout<<"6"<<endl;break;
        case 3:cout<<"500"<<endl;break;
        case 4:cout<<"9000"<<endl;break;
        case 5:cout<<"1"<<endl;break;
        case 6:cout<<"100"<<endl;break;
        case 7:cout<<"1000"<<endl;break;
        case 8:cout<<"10000"<<endl;break;
        case 9:cout<<"100000000"<<endl;break;
        case 10:cout<<"10"<<endl;break;
    }
    return 0;
}
