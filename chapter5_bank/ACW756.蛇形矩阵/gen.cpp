#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc,char*argv[]){
int tc=argc>1?atoi(argv[1]):1;
srand(time(0)+tc*1000);
switch(tc){
        case 1: cout<<"3 3"<<endl;break;
        case 2: cout<<"1 1"<<endl;break;
        case 3: cout<<"4 5"<<endl;break;
        case 4: cout<<"5 5"<<endl;break;
        case 5: cout<<"2 3"<<endl;break;
        case 6: cout<<"3 4"<<endl;break;
        case 7: cout<<"6 6"<<endl;break;
        case 8: cout<<"7 8"<<endl;break;
        case 9: cout<<"10 10"<<endl;break;
        case 10: cout<<"2 2"<<endl;break;
}
return 0;
}
