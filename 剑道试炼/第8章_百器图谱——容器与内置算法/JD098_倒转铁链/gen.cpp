#include <iostream>
using namespace std;
int main(int c,char**v){
  int tc=c>1?atoi(v[1]):1;
  int vals[][12]={
    {1,2,3,-1},
    {3,5,2,7,1,-1},
    {10,20,30,40,50,-1},
    {5,4,3,2,1,-1},
    {100,-1},
    {1,2,3,4,5,6,7,8,-1},
    {1,3,5,7,9,2,4,6,8,10,-1},
    {42,-1},
    {9,8,7,6,5,4,3,2,1,0,-1},
    {15,30,45,60,-1},
  };
  for(int i=0;vals[tc-1][i]!=-1;i++) cout<<vals[tc-1][i]<<" ";
  cout<<"-1"<<endl;
  return 0;
}
