/*
w2p03 特殊密码锁
By Andy <使用bitset>
*/
#include <iostream>
#include <cstring>
#include <bitset>
#include <algorithm>
using namespace std;

int main()
{
    string line;//输入的01字符串
    bitset<32> lock; //当前的锁的状态
    int minTimes = 1 << 30;  //初始化按钮次数为无穷大

    // 读入字符串，初始化用bitset表示的锁的初始状态与目标状态变量
	cin >> line;
    bitset<32> sourceLock(line);
    cin >> line;
    bitset<32> targetLock(line);
    
	//枚举第一个按钮是否按下的两种情况即可。对于指定的一种情况，后面的事情都是确定的
    int n=line.size();
	for(int p = 0; p < 2; ++p) { //p=0代表最左边按钮不按，p=1代表按下
        lock = sourceLock;//初始化lock
		int times = 0; //按下的次数
		int nextButton = p; //初始化下一个按钮的状态，是否按下
		
		for(int i = 0; i < n; ++i) {//遍历所有的位置
			if(nextButton==1) { //按钮按下的状态更新
				++ times;
				if( i > 0)
					lock.flip(i-1);//左边取反
				lock.flip(i);//中间取反
				if( i < n-1)
					lock.flip(i+1);//右边取反
			}
            //判断当前lock是否与目标targetLock的第i位相同
			if( lock[i] != targetLock[i])  
				nextButton = 1; //如果不同就要在在下次循环按下按钮
			else 
				nextButton = 0;//不要按下当前按钮
		}
		
		if( lock == targetLock) //是否抵达目标状态
			minTimes = min(minTimes ,times);//取最小值
	}
	if( minTimes == 1 << 30)//没有找到目标状态
		cout << "impossible" << endl;
	else
		cout << minTimes << endl;
	return 0;
}
