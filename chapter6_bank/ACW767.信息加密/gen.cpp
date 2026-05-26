#include <iostream>
#include <string>
using namespace std;
int main(int c,char**v){
  int tc=c>1?atoi(v[1]):1;
  string s[]={"Hello, World!","abcXYZ","Test123","AbC","zZaA","Coding","XyZ","hello world","PWD","java"};
  cout<<s[tc-1]<<endl;
  return 0;
}