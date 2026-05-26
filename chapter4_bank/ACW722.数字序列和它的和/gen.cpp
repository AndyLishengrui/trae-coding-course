#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc,char*argv[]){
    int tc=argc>1?atoi(argv[1]):1;
    srand(time(0)+tc*1000);
    switch(tc){
        case 1:cout<<"5 10\n2 3\n0 0"<<endl;break;
        case 2:cout<<"5 10\n2 3\n0 0"<<endl;break;
        case 3:cout<<"1 5\n-1 -1"<<endl;break;
        case 4:cout<<"1 5\n-1 -1"<<endl;break;
        case 5:printf("%d %d\n%d %d\n-1 -1\n",rand()%50+1,rand()%50+1,rand()%50+1,rand()%50+1);break;
        case 6:printf("%d %d\n%d %d\n-1 -1\n",rand()%50+1,rand()%50+1,rand()%50+1,rand()%50+1);break;
        case 7:printf("%d %d\n%d %d\n-1 -1\n",rand()%50+1,rand()%50+1,rand()%50+1,rand()%50+1);break;
        case 8:printf("%d %d\n%d %d\n-1 -1\n",rand()%50+1,rand()%50+1,rand()%50+1,rand()%50+1);break;
        case 9:printf("%d %d\n%d %d\n-1 -1\n",rand()%50+1,rand()%50+1,rand()%50+1,rand()%50+1);break;
        case 10:printf("%d %d\n%d %d\n-1 -1\n",rand()%50+1,rand()%50+1,rand()%50+1,rand()%50+1);break;
    }
    return 0;
}
