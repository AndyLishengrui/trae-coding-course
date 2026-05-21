#include <iostream>
using namespace std;
const int N=100007;
int num[N],visited[N];

int main(){
    int n;
    cin>>n;
    for (int i=0; i<n; i++ ) cin>>num[i];//读入n个数
    //双指针扫描
    int res=0;//初始化为最小值
    for (int i=0, j=0; i<n; i++){
        visited[num[i]]++;
        while(j<=i && visited[num[i]]>1){
            visited[num[j]]--;
            j++; //去掉重复数
        }
        res= max(res,i-j+1);//j--i 之间的数字个数
    }
    cout<<res<<endl;
    return 0;
}