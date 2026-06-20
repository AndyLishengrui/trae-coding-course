#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int c,char**v){
  int tc=c>1?atoi(v[1]):1;
  srand(time(0)+tc*1000);
  string s[]={"hello","abc","test","house","code","word","fun","game","book","time"};
  string t[]={"X","Y","Z","OO","XX","AA","BB","CC","DD","EE"};
  cout<<s[tc-1]<<"\n"<<t[tc-1]<<endl;
  return 0;
}