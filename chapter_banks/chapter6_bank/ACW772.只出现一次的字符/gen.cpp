#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int c,char**v){
  int tc=c>1?atoi(v[1]):1;
  string s[]={"abaccdeff","abcabc","leetcode","loveleetcode","aabb","abcdefg","a","aabbcc","xyzz","programming"};
  cout<<s[tc-1]<<endl;
  return 0;
}