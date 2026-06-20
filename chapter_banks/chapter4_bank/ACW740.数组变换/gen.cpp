#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc,char*argv[]){
    int tc=argc>1?atoi(argv[1]):1;
    srand(time(0)+tc*1000);
    switch(tc){
        case 1:for(int j=0;j<20;j++)cout<<j<<endl;break;
        case 2:for(int j=0;j<20;j++)cout<<j<<endl;break;
        case 3:for(int j=0;j<20;j++)cout<<rand()%10<<endl;break;
        case 4:for(int j=0;j<20;j++)cout<<rand()%10<<endl;break;
        case 5:for(int j=0;j<20;j++)cout<<rand()%1000-500<<endl;break;
        case 6:for(int j=0;j<20;j++)cout<<rand()%1000-500<<endl;break;
        case 7:for(int j=0;j<20;j++)cout<<rand()%1000-500<<endl;break;
        case 8:for(int j=0;j<20;j++)cout<<rand()%1000-500<<endl;break;
        case 9:for(int j=0;j<20;j++)cout<<rand()%1000-500<<endl;break;
        case 10:for(int j=0;j<20;j++)cout<<rand()%1000-500<<endl;break;
    }
    return 0;
}
