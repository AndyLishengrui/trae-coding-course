#include <iostream>
#include <cstdio>
using namespace std;
int main(){
int p,e,i,d,caseNumber = 0;
//输入
while(	cin >> p >> e >>i >>d && p!= -1) {
    ++ caseNumber;
    int k;
//枚举
//   for(k=d+1;k<=d+21252;k++)
//     if ((k-p)%23==0 && (k-e)%28==0 && (k-i)%33==0)
    for(k = d+1; (k-p)%23; ++k);
        for(; (k-e)%28; k+= 23);
            for(; (k-i)%33; k+= 23*28);
    cout<<"Case "<<caseNumber<<": the next triple peak occurs in "<<k-d<<" days."<<endl;
}
    return 0;
}

