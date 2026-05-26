#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc,char*argv[]){
int tc=argc>1?atoi(argv[1]):1;
srand(time(0)+tc*1000);
switch(tc){
        case 1: cout<<1<<"\n0"<<endl;break;
        case 2: cout<<3<<"\n0"<<endl;break;
        case 3: cout<<5<<"\n0"<<endl;break;
        case 4: cout<<7<<"\n0"<<endl;break;
        case 5: cout<<9<<"\n0"<<endl;break;
        case 6: cout<<4<<"\n0"<<endl;break;
        case 7: cout<<6<<"\n0"<<endl;break;
        case 8: cout<<8<<"\n0"<<endl;break;
        case 9: cout<<10<<"\n0"<<endl;break;
        case 10: cout<<2<<"\n0"<<endl;break;
}
return 0;
}
