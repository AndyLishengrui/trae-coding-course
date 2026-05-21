//CodeBy Guo Wei 
#include <iostream>
#include <vector>
#include <cstring>
using namespace std;
#define Clear(a,b) memset(a,b,sizeof(a))

struct Pos
{
	int r,c;
};
Pos path[30] ;
Pos dir[8] = {{ -2,-1},{-2,1},{-1,-2},{-1,2},
			  {1,-2},{1,2} ,{ 2,-1},{2,1} };
int p,q;
int visited[30][30];
//Todo 从 (r,c)出发，此时已经走了step步，看能否成功 
bool dfs(int r, int c,int step)
{
    //?所有棋盘格子都走到
	if( step == p * q )
		return true;
    //?是否超过边界  
	if( r < 0 || r >= p || c < 0 || c >= q )
		return false;	
    //?r,c是否来过	
	if( visited[r][c] )
		return false;
    //todo 枚举8个方向，深搜   
	visited[r][c] = 1;
	path[step].r = r;
	path[step].c = c;
	for( int i = 0;i < 8; ++ i ) {
		if ( dfs(r + dir[i].r, c + dir[i].c, step + 1 ))
			return true;
	}
	visited[r][c] = 0; //回溯，取消这一步的走法，使得走其他步的时候，能绕回到这里 
	return false;
}
int main()
{
	
	int t;
	cin >> t;
	for( int tt = 1; tt <= t; ++ tt ) {
		cout << "#" << tt << ":" << endl;
		cin >> p >> q; // p num, q alph// q行p列 
		memset(visited,0,sizeof(visited));
		int i;
		for(  i = 0; i < q; ++i )
			for( int j = 0; j < p; ++ j ) {
				if (dfs(i,j,0)) {
					i = q + 10;
					for( int k = 0; k < p * q; ++ k)
						cout << char (path[k].r + 'A')
						 << (path[k].c + 1) ;
					break;
				}
			}
		if( i == q ) 
			cout << "none";
		cout << endl;
	}
}
