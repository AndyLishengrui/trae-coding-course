#include <iostream>
#include <string>
#include <climits>
using namespace std;

const int N=9;
const int MAXN=1<<N; // 512
const char BLANK='.';

int row[N],col[N],cell[3][3];
int ones[MAXN],LOG2[MAXN];
string sudoku;

inline int lowbit(int x){return x&-x;}

int count_ones(int n){
    int res=0;
    while(n){
        n-=lowbit(n);
        res++;
    }
    return res;
}

void build_tables(){
    for(int i=0;i<N;++i) LOG2[1<<i]=i;
    for(int i=0;i<MAXN;++i) ones[i]=count_ones(i);
}

void init(){
    for(int i=0;i<N;++i) row[i]=col[i]=MAXN-1;
    for(int i=0;i<3;++i) for(int j=0;j<3;++j) cell[i][j]=MAXN-1;
}

inline void flip(int x,int y,int n){
    row[x]^=1<<n;
    col[y]^=1<<n;
    cell[x/3][y/3]^=1<<n;
}

inline int get_avail(int x,int y){
    return row[x]&col[y]&cell[x/3][y/3];
}

bool dfs(int empty){
    if(empty==0){
        cout<<sudoku<<endl;
        return true;
    }
    int min_opts=INT_MAX,x=-1,y=-1;
    for(int i=0;i<N;++i){
        for(int j=0;j<N;++j){
            if(sudoku[i*N+j]==BLANK){
                int opts=ones[get_avail(i,j)];
                if(opts<min_opts){
                    min_opts=opts;
                    x=i;
                    y=j;
                }
            }
        }
    }
    int avail=get_avail(x,y);
    for(int sk=avail;sk;sk-=lowbit(sk)){
        int bit=lowbit(sk);
        int num=LOG2[bit]; // 0-8，对应数字1-9
        flip(x,y,num);
        sudoku[x*N+y]='1'+num;
        dfs(empty-1);
        sudoku[x*N+y]=BLANK;
        flip(x,y,num);
    }
    return false;
}

int main(){
    build_tables();
    while(cin>>sudoku && sudoku[0]!='e'){
        init();
        int empty=0;
        for(int i=0;i<N;++i){
            for(int j=0;j<N;++j){
                if(sudoku[i*N+j]==BLANK){
                    empty++;
                }else{
                    int num=sudoku[i*N+j]-'1';
                    flip(i,j,num);
                }
            }
        }
        dfs(empty);
    }
    return 0;
}