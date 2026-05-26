#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc,char*argv[]){
    int tc=argc>1?atoi(argv[1]):1;
    srand(time(0)+tc*1000);
    switch(tc){
        case 1: cout<<"7\n-5\n6\n-3.4\n4.6\n12"<<endl; break;
        case 2: cout<<"7\n-5\n6\n-3.4\n4.6\n12"<<endl; break;
        case 3: cout<<"-1\n-2\n-3\n-4\n-5\n-6"<<endl; break;
        case 4: cout<<"-1\n-2\n-3\n-4\n-5\n-6"<<endl; break;
        case 5: printf("%.1f\n%.1f\n%.1f\n%.1f\n%.1f\n%.1f\n",(rand()%200-100)*1.0,(rand()%200-100)*1.0,(rand()%200-100)*1.0,(rand()%200-100)*1.0,(rand()%200-100)*1.0,(rand()%200-100)*1.0); break;
        case 6: printf("%.1f\n%.1f\n%.1f\n%.1f\n%.1f\n%.1f\n",(rand()%200-100)*1.0,(rand()%200-100)*1.0,(rand()%200-100)*1.0,(rand()%200-100)*1.0,(rand()%200-100)*1.0,(rand()%200-100)*1.0); break;
        case 7: printf("%.1f\n%.1f\n%.1f\n%.1f\n%.1f\n%.1f\n",(rand()%200-100)*1.0,(rand()%200-100)*1.0,(rand()%200-100)*1.0,(rand()%200-100)*1.0,(rand()%200-100)*1.0,(rand()%200-100)*1.0); break;
        case 8: cout<<"0.1\n0.2\n0.3\n0.4\n0.5\n0.6"<<endl; break;
        case 9: cout<<"0.1\n0.2\n0.3\n0.4\n0.5\n0.6"<<endl; break;
        case 10: cout<<"0.1\n0.2\n0.3\n0.4\n0.5\n0.6"<<endl; break;
    }
    return 0;
}
