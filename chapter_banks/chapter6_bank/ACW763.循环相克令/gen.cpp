#include <iostream>
using namespace std;
int main(int c,char**v){
  int tc=c>1?atoi(v[1]):1;
  string p[][2]={{"Hunter","Bear"},{"Bear","Hunter"},{"Gun","Bear"},{"Hunter","Gun"},{"Bear","Gun"},{"Gun","Hunter"},{"Hunter","Hunter"},{"Bear","Bear"},{"Gun","Gun"},{"Hunter","Bear"}};
  cout<<p[tc-1][0]<<" "<<p[tc-1][1]<<endl;
  return 0;
}