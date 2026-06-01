#include <iostream>
#include <cstring>
#include <vector>
using namespace std;
const int N = 1e6 + 7;

//C= A*b,t的用法很精彩！
vector<int> mul(vector<int> &A, int b){
    vector<int> C;
    int t=0;
    for(int i=0; i<A.size() || t; i++){
        //如果t还有剩余或者A还有剩余，乘法结果C需要加新的位
        if(i<A.size()) t+=A[i]*b;//把b当作整体做乘法
        C.push_back(t % 10);//存储第i位
        t /=10; //更新t
    }
    while(C.size()>1 && C.back()==0) C.pop_back();//去掉C开头的0
    return C;
}

int main()
{
    //输入为字符串
    string a;
    int b;//输入的b比较小，作为一个整体处理
    vector<int> A,C;

    cin >> a >> b; // a="786654"
    //倒序存储A，B，a[0]乃是最低位
    for (int i = a.size() - 1; i >= 0; i--)
        A.push_back(a[i] - '0');
    C=mul(A,b);
    for (int i = C.size() - 1; i >= 0; i--)
            cout << C[i]; //打印C
    return 0;
}
