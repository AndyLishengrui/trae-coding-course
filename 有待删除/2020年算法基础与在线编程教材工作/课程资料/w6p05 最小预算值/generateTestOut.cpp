#include <bits/stdc++.h>
#include <cstdlib>
#include <ctime>
#include <string>
#include <sstream>
#include <memory>  
#include <cstring>  
#include <iostream>
#include <bitset>
#include <algorithm>
#include <functional>
using namespace std;
#define For(a, b, c) for (register int a = b; a <= c;++a)
#define CMax(a,b) (a<(b)?a=(b):0)
#define CMin(a,b) (a>(b)?a=(b):0)
#define Max(a,b) ((a)<(b)?(b):(a))
#define Min(a,b) ((a)>(b)?(b):(a))
#define Clear(a,b) memset(a,b,sizeof(a))
#define Swap(a,b) a^=b^=a^=b


const int NUM = 10;

string getname(int i, string a)
{
    stringstream ss;
    ss << i << a;
    return ss.str();
}

int N,M ;
int cost[100100];
bool Valid(int c)
{
	int m = 1; //������ 
	int curCost = 0; //���»��� 
	for(int i = 0;i < N; ++i) {
		if(cost[i] > c )
			return false; 
		if( curCost + cost[i] > c ) {
			curCost = cost[i];
			++m;
			if( m > M )
				return false;
		}
		else
			curCost += cost[i];
	}
	return true;
}

void expression_value()
{
	cin >> N >> M;
	int L = 1 << 30,R = 0;
	for(int i = 0;i < N; ++i) {
		cin >> cost[i];
		L = min(L,cost[i]);
		R += cost[i];
	}
	int lastValid = 0;
	while( L <= R) {
		int mid = L + (R-L)/2;
		if(Valid(mid)) {
			lastValid = mid;
			R = mid - 1;
		}
		else 
			L = mid +1;
	}
	cout << lastValid ;
}


int main()
{
    
    for (int tt = 1; tt <= NUM; tt++)
    {
        string inFileName,outFileName;
        inFileName = getname(tt, ".in");
        outFileName = getname(tt,".out");
        freopen(inFileName.c_str(),"r",stdin);
        freopen(outFileName.c_str(),"w",stdout);
        
        expression_value(); 


}		
    return 0;
}
