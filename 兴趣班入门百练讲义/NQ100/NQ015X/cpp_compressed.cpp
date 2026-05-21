#include <iostream>
using namespace std;
int main(){char t;cin>>t;double q[12][12],s=0,c=0;for(int i=0;i<12;i++)for(int j=0;j<12;j++)cin>>q[i][j];for(int i=1;i<=11;i++)for(int j=12-i;j<=11;j++){s+=q[i][j];c+=1;}if(t=='S')printf("%.1lf\n",s);else printf("%.1lf\n",s/c);return 0;}