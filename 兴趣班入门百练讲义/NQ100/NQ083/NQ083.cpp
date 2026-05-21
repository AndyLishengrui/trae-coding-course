//NQ083 最长公共子序列的长度。
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
#define N 1007
//最长公共子列的状态矩阵
//maxSlength[i][j]表示 序列s1的前i项与序列s2的前j项的最长公共子列长度
int maxSlength[N][N];
string s1, s2;
int main()
{
    while (cin >> s1 >> s2) //直到输入为空
    {
        //初始化maxSlength
        int len1 = s1.length(), len2 = s2.length();
        //把长度为0的边界设置为0；
        for (int i = 0; i <= len1; i++) //maxSlength[i][0]==0
            maxSlength[i][0] = 0;
        for (int i = 0; i <= len2; i++) //maxSlength[0][i]==0
            maxSlength[0][i] = 0;
        //递推计算
        for (int i = 1; i <= len1; i++)
            for (int j = 1; j <= len2; j++)
                if (s1[i - 1] == s2[j - 1]) //字符串从0开始计数，比较第i，j个字符的比较用s1[i-1],s2[j-1]
                    maxSlength[i][j] = maxSlength[i - 1][j - 1] + 1;
                else
                    maxSlength[i][j] = max(maxSlength[i - 1][j], maxSlength[i][j - 1]);
        //输出最长公共字串
        cout << maxSlength[len1][len2] << endl; //[1，n] n代表字符串长度，最长是n
    }
}
