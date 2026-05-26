#include <iostream>
#include <string>
using namespace std;
int main(){
  string samples[]={"Hello World","abc","test","12345","a","abcdefghij","Hello World!","x","你好世界","programming"};
  int tc=1;
  cin>>tc;
  cout<<samples[tc-1]<<endl;
  return 0;
}