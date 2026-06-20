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

const double PI=acos(-1.0); 
const double eps = 1e-6;
int r[10010];
int N,F;
bool Valid(double V)
{
	if( V < eps )
		return true;
	int total = 0;
	for(int i = 0;i < N; ++i) {
		double n =  r[i]*r[i] / V;
		total += n;
		if( total >= F)
			return true;
	}
	return false;
}

void expression_value()
{
	cin >> N >> F;
	++F;
	double maxV = 0;
	for(int i = 0;i < N; ++i) {
		cin >> r[i];
		maxV = max(maxV,(double)r[i]*r[i]);
	}
	double L = 0,R = maxV;
	while( R - L > eps ) {
		double midV = L + (R-L )/2;
		if( Valid(midV) ) 
			L = midV;
		else 
			R = midV;
	}
	cout << fixed << setprecision(3) << PI * L ;
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
