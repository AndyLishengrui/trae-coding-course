
#include <bits/stdc++.h>
#include <cstdlib>
#include <ctime>
#include <string>
#include <sstream>
#include <ctime>
#include <memory>  
#include <cstring>  
#include <iostream>  
using namespace std;
int GetBit(char c,int i) {
    //取c的第i位,右移动，然后用&1的操作保留最右位
    return	( c >> i ) & 1;
}
void SetBit(char & c,int i, int v) {
//设置c的第i位为v  v为0或者1
    if (v) 
        c|= (1 << i); // 或运算把c的第i位设置为1
    else
        c &= ~( 1 << i); // 与运算把c的第i位设置为0
}
void Flip(char & c, int i) {
    //将c的第i位为取反
    c ^= ( 1 << i); //用异或运算把第i位取反
}

void Outputpressed(int t,char pressed[]) //输出结果
{
    cout << "PUZZLE #" << t << endl;
    for( int i = 0;i < 5; ++i ) {
        for( int j = 0; j < 6; ++j ) {
            cout << GetBit(pressed[i],j)<< " ";
    }
    cout << endl;
    }
}

const int NUM = 10;

string getname(int i, string a)
{
    stringstream ss;
    ss << i << a;
    return ss.str();
}


int main()
{
    
    //只读入一组测试数据test.in，生成test.out的代码模板：
 //   freopen("test.in","r",stdin);//设置 cin scanf 这些输入流都从 test.in中读取
 //   freopen("test.out","w",stdout);//设置 cout printf 这些输出流都输出到 test.out里面去
    // 待测程序，即标程,放在这里
    
    //------------------------------我是分割线---------------------------------------
    
    //循环读入1.in-- 10.in    
    //循环读入10个in文件，生成10个out的代码模板：
    for (int tt = 1; tt <= NUM; tt++)
    {
        string inFileName,outFileName;//文件名
        inFileName = getname(tt, ".in");
        outFileName = getname(tt,".out");
        freopen(inFileName.c_str(),"r",stdin);
        freopen(outFileName.c_str(),"w",stdout);
    
    // 待测程序，即标程,放在这里
    // GW075
    char oriLights[5]; //最初灯矩阵，一个比特表示一盏灯
    char lights[5];  //不停变化的灯矩阵
    char pressed[5];  //结果按钮矩阵
    char switchs;  //某一行的开关状态
    int T;
    cin >> T;
    for( int t = 1; t <= T; ++ t) {
        memset(oriLights,0,sizeof(oriLights)); //清零oriLights
            for( int i = 0;i < 5; i ++ ) { //读入最初灯状态
                for(int j = 0; j < 6; j ++ ) {
                int s;
                cin >> s;  
                SetBit(oriLights[i],j,s); //调用SetBit
                }
        }

        for( int n = 0; n < 64; ++n ) { //遍历首行开关的64种状态 
        memcpy(lights,oriLights,sizeof(oriLights));  
        switchs = n; //第i行的开关状态
        for( int i = 0;i < 5; ++i ) {
            pressed[i] = switchs; //第i行的开关方案 
            for( int j = 0; j < 6; ++j ) {
                if( GetBit(switchs,j)) {
                    if( j > 0)
                        Flip(lights[i],j-1);//改左灯 
                        Flip(lights[i],j);//改开关位置的灯 
                    if( j < 5 ) Flip(lights[i],j+1);//改右灯
                }
            }
            if( i < 4 )
                lights[i+1] ^= switchs;//改下一行的灯
            switchs = lights[i]; //第i+1行开关方案和第i行灯情况同
        }
        if( lights[4] == 0 ) {
                Outputpressed(t,pressed);
                break;
        }
        } // for( int n = 0; n < 64; n ++ )
        }
    // _sleep(2*1000);//延时2秒 
       
    }

    return 0;
}
