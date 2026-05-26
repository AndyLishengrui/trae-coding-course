#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc,char*argv[]){
    int tc=argc>1?atoi(argv[1]):1;
    srand(time(0)+tc*1000);
    switch(tc){
        case 1:cout<<"0\n-5\n63\n-8\n0\n1\n2\n-100\n50\n200"<<endl;break;
        case 2:cout<<"0\n-5\n63\n-8\n0\n1\n2\n-100\n50\n200"<<endl;break;
        case 3:cout<<"-1\n-2\n-3\n-4\n-5\n-6\n-7\n-8\n-9\n-10"<<endl;break;
        case 4:cout<<"-1\n-2\n-3\n-4\n-5\n-6\n-7\n-8\n-9\n-10"<<endl;break;
        case 5:for(int j=0;j<10;j++)printf("%d\n",rand()%100-50);break;
        case 6:for(int j=0;j<10;j++)printf("%d\n",rand()%100-50);break;
        case 7:for(int j=0;j<10;j++)printf("%d\n",rand()%100-50);break;
        case 8:for(int j=0;j<10;j++)printf("%d\n",rand()%2000000-1000000);break;
        case 9:for(int j=0;j<10;j++)printf("%d\n",rand()%2000000-1000000);break;
        case 10:for(int j=0;j<10;j++)printf("%d\n",rand()%2000000-1000000);break;
    }
    return 0;
}
