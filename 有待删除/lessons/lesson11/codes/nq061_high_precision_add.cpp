#include <iostream>
#include <cstring>
#include <vector>
using namespace std;
const int N = 1e6+7; 

vector<int> add(vector<int> &A, vector<int>&B){
    vector<int> C;
    int t=0;
    for (int i=0; i<A.size()||i<B.size(); i++) {
        if (i<A.size()) t+=A[i];
        if (i<B.size()) t+=B[i];
        //对t取模，取进位
        C.push_back(t %10);//把t模10的余数入数组，商为进位
        t /= 10; //算出进位，供下一次循环使用
    }
    if(t) C.push_back(1);//最高位进位
    return C;
}

int main(){
    //输入为字符串
    string a,b;
    vector<int> A,B;

    cin >> a>>b; // a="786654"
    //倒序存储A，B，a[0]乃是最低位
    for(int i= a.size()-1; i>=0; i--) A.push_back(a[i]-'0');
    for(int i= b.size()-1; i>=0; i--) B.push_back(b[i]-'0');

    auto C = add(A,B);

    for(int i= C.size()-1; i>=0; i--) cout<<C[i];//打印C
    return 0;

}