#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc,char*argv[]){
int tc=argc>1?atoi(argv[1]):1;
srand(time(0)+tc*1000);
switch(tc){
        case 1: cout<<"S ";for(int j=0;j<144;j++)printf("%.1f ",(rand()%100)*1.0);break;
        case 2: cout<<"S ";for(int j=0;j<144;j++)printf("%.1f ",(rand()%100)*1.0);break;
        case 3: cout<<"S ";for(int j=0;j<144;j++)printf("%.1f ",(rand()%100)*1.0);break;
        case 4: cout<<"M ";for(int j=0;j<144;j++)printf("%.1f ",(rand()%100)*1.0);break;
        case 5: cout<<"S ";for(int j=0;j<144;j++)printf("%.1f ",(rand()%100)*1.0);break;
        case 6: cout<<"M ";for(int j=0;j<144;j++)printf("%.1f ",(rand()%100)*1.0);break;
        case 7: cout<<"S ";for(int j=0;j<144;j++)printf("%.1f ",(rand()%100)*1.0);break;
        case 8: cout<<"M ";for(int j=0;j<144;j++)printf("%.1f ",(rand()%100)*1.0);break;
        case 9: cout<<"S ";for(int j=0;j<144;j++)printf("%.1f ",(rand()%100)*1.0);break;
        case 10: cout<<"M ";for(int j=0;j<144;j++)printf("%.1f ",(rand()%100)*1.0);break;
}
return 0;
}
