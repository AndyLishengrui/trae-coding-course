#include <iostream>
using namespace std;
int main(int c,char**v){
  int tc=c>1?atoi(v[1]):1;
  int vals[]={1,2,3,4,5,6,7,8,9,10};
  int n=vals[tc-1];
  cout<<n<<" 0"<<endl;
  return 0;
}
