#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int c,char**v){
  int tc=c>1?atoi(v[1]):1;
  srand(time(0)+tc*1000);
  string s[]={"hello2024world","abc123","0xDEAD","test","a1b2c3","999","abcdef","1234567890","x","noDigits"};
  cout<<s[tc-1]<<endl;
  return 0;
}