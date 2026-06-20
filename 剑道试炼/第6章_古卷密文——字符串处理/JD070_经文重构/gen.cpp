#include <iostream>
#include <string>
using namespace std;
int main(int c,char**v){
  int tc=c>1?atoi(v[1]):1;
  string s[]={"abc","xyz","ABC","123","hello","test","Aa","Bb","Cc","Zz"};
  cout<<s[tc-1]<<endl;
  return 0;
}