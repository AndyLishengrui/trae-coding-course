#include <iostream>
using namespace std;
#define For(a,begin,end) for(int a =begin; a<end;a++)
int main(){
    int x[10];
    For(i,0,10) cin>>x[i];
    For(i,0,10) if (x[i]<=0) x[i]=1;
    For(i,0,10) cout<<"X["<<i<<"] = "<<x[i]<<endl;
    return 0;
}