#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc,char*argv[]){
    int tc=argc>1?atoi(argv[1]):1;
    srand(time(0)+tc*1000);
    switch(tc){
        case 1: cout<<"10\n10 C\n6 R\n15 F\n5 C\n14 R\n9 C\n6 R\n8 F\n5 C 14 R"<<endl; break;
        case 2: cout<<"10\n10 C\n6 R\n15 F\n5 C\n14 R\n9 C\n6 R\n8 F\n5 C 14 R"<<endl; break;
        case 3: cout<<rand()%20+1; for(int j=0;j<3;j++){char t="CRF"[rand()%3]; printf(" %d %c",rand()%20+1,t);} printf(" "); break;
        case 4: cout<<rand()%20+1; for(int j=0;j<3;j++){char t="CRF"[rand()%3]; printf(" %d %c",rand()%20+1,t);} printf(" "); break;
        case 5: cout<<rand()%20+1; for(int j=0;j<3;j++){char t="CRF"[rand()%3]; printf(" %d %c",rand()%20+1,t);} printf(" "); break;
        case 6: cout<<rand()%50+10; for(int j=0;j<10;j++){char t="CRF"[rand()%3]; printf(" %d %c",rand()%20+1,t);} printf(" "); break;
        case 7: cout<<rand()%50+10; for(int j=0;j<10;j++){char t="CRF"[rand()%3]; printf(" %d %c",rand()%20+1,t);} printf(" "); break;
        case 8: cout<<rand()%50+10; for(int j=0;j<10;j++){char t="CRF"[rand()%3]; printf(" %d %c",rand()%20+1,t);} printf(" "); break;
        case 9: cout<<rand()%50+10; for(int j=0;j<10;j++){char t="CRF"[rand()%3]; printf(" %d %c",rand()%20+1,t);} printf(" "); break;
        case 10: cout<<rand()%50+10; for(int j=0;j<10;j++){char t="CRF"[rand()%3]; printf(" %d %c",rand()%20+1,t);} printf(" "); break;
    }
    return 0;
}
