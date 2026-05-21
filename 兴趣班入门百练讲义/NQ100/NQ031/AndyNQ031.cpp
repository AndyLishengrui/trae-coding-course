#include <iostream>
#include <cstring>
using namespace std;
const string seof="ENDOFINPUT";
int main(){
    string s;
    while(getline(cin,s),s!=seof)
    {
        if (s=="START")
          getline(cin,s);//读入一行
        //解密
      for (auto &c:s)
        if (c>='A' && c<='Z') c = 'A' + (c-'A'+ 21) % 26;
          cout<<s<<endl;
        getline(cin,s);//读入END
    }   
   return 0;
}