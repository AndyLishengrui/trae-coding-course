#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
#define MaxCharNumber 12
char str[MaxCharNumber]={0};
char strPermutation[MaxCharNumber]={0};
bool used[MaxCharNumber]={false};
int lengthOfInput;
void permutation(int n)
{ 
    // 如果n的值为lengthofInput，表明从0--LengthofInput都已经排列好
    // 输出此种排列方案
    if (n==lengthOfInput)
    {
        strPermutation[n]=0;//结尾设置为空字符，然后用cout直接输出整个字符串
        cout<<strPermutation<<endl;
        return;
    }
    // 假定n-1已经排列好，现在选取一个字母加入排列的队列中
    // used[i]为true，表示该字符已经被选取
    for (int k =0; k<lengthOfInput;k++)
    {
        if (!used[k])
        {
            used[k]=true;
            //把当前选出的字符放到strPermuation中
            strPermutation[n]=str[k];
            permutation(n+1);
            used[k]=false;
        }
    }

}
int main()
{
    //读入字符串，并且排序
    cin>>str;
    lengthOfInput=strlen(str);
    sort(str,str+lengthOfInput);//调用sort排序
    permutation(0);
    return 0;
}