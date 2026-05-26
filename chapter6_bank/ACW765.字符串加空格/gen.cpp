#include <iostream>
#include <string>
using namespace std;
int main(int c,char**v){
  int tc=c>1?atoi(v[1]):1;
  string s[]={"abc","hello","a","123","xyz","test","abcdef","ok","hi","word"};
  cout<<s[tc-1]<<endl;
  return 0;
}