#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc,char*argv[]){
int tc=argc>1?atoi(argv[1]):1;
srand(time(0)+tc*1000);
switch(tc){
        case 1: cout<<1<<" 0"<<endl;break;
        case 2: cout<<3<<" 0"<<endl;break;
        case 3: cout<<5<<" 0"<<endl;break;
        case 4: cout<<7<<" 0"<<endl;break;
        case 5: cout<<9<<" 0"<<endl;break;
        case 6: cout<<4<<" 0"<<endl;break;
        case 7: cout<<6<<" 0"<<endl;break;
        case 8: cout<<8<<" 0"<<endl;break;
        case 9: cout<<10<<" 0"<<endl;break;
        case 10: cout<<2<<" 0"<<endl;break;
}
return 0;
}
