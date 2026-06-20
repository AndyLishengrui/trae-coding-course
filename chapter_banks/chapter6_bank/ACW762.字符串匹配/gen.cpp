#include <iostream>
#include <string>
using namespace std;
int main(int c,char**v){
  int tc=c>1?atoi(v[1]):1;
  string p[][2]={{"abcdefg","cde"},{"hello","ell"},{"test","st"},{"abc","d"},{"xyz","yz"},{"program","gram"},{"coding","cod"},{"match","tch"},{"hello","hel"},{"world","orl"}};
  cout<<p[tc-1][0]<<" "<<p[tc-1][1]<<endl;
  return 0;
}