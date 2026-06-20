#include <iostream>
using namespace std;
int main(int c,char**v){
int tc=c>1?atoi(v[1]):1;
switch(tc){
case 1:cout<<"1 2 3 -1"<<endl;break;
case 2:cout<<"10 20 30 -1"<<endl;break;
case 3:cout<<"5 -1"<<endl;break;
case 4:cout<<"100 -1"<<endl;break;
case 5:cout<<"7 8 9 -1"<<endl;break;
case 6:cout<<"1 -1"<<endl;break;
case 7:cout<<"50 60 -1"<<endl;break;
case 8:cout<<"2 4 6 8 -1"<<endl;break;
case 9:cout<<"99 88 77 -1"<<endl;break;
case 10:cout<<"3 1 4 1 5 -1"<<endl;break;
}
return 0;
}