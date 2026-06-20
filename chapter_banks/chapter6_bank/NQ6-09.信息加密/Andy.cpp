#include <iostream>
#include <cstring>
using namespace std;

int main(){

    string s;
    getline(cin,s);//读入一行

    for (auto &c:s)//使用auto注意&c直接引用字符串直接修改
      if (c>='a' && c<='z') 
          c = 'a'+ (c-'a'+1) % 26;//取模运算
         else if (c>='A' && c<='Z') 
          c = 'A' + (c-'A'+1) % 26;

    cout<<s<<endl;//输出结果
}
