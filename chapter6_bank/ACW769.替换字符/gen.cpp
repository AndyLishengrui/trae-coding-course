#include <iostream>
using namespace std;
int main(int c,char**v){
  int tc=c>1?atoi(v[1]):1;
  cout<<"hello\no\nworld\nl\nabc\nx\ntest\ne\nhello\na "<<((tc-1)%10<3?"h e":"w o")<<endl;
  return 0;
}