#include <iostream>
#include <string>
#include <climits>
using namespace std;

const int N=9;
const int MAX_ARRAY=1<<N; // 512
const char BLANK='0';

int row[N],col[N],cell[3][3];
int ones[MAX_ARRAY],lowbit2pos[MAX_ARRAY];
string sudoku;

inline int lowbit(int x){return x&-x;}
inline void clearBit(int&x,int n){x&=~(1<<n);}
inline void setBit(int&x,int n){x|=(1<<n);}
inline int getAvailable(int x,int y){return row[x]&col[y]&cell[x/3][y/3];}

void init(){
    for(int i=0;i<N;++i) row[i]=col[i]=MAX_ARRAY-1;
    for(int i=0;i<3;++i) for(int j=0;j<3;++j) cell[i][j]=MAX_ARRAY-1;
}

void precompute(){
    for(int i=0;i<N;++i) lowbit2pos[1<<i]=i;
    for(int i=0;i<MAX_ARRAY;++i){
        int cnt=0;
        for(int j=i;j;j-=lowbit(j)) cnt++;
        ones[i]=cnt;
    }
}

string readSudoku(){
    string res,line;
    for(int i=0;i<N;++i){
        cin>>line;
        res+=line;
    }
    return res;
}

void printSudoku(const string&s){
    for(int i=0;i<N;++i) cout<<s.substr(i*N,N)<<endl;
}

bool dfs(int empty){
    if(empty==0) return true;
    int minOpts=INT_MAX,x=-1,y=-1;
    for(int i=0;i<N;++i){
        for(int j=0;j<N;++j){
            if(sudoku[i*N+j]==BLANK){
                int opts=ones[getAvailable(i,j)];
                if(opts<minOpts){
                    minOpts=opts;
                    x=i;
                    y=j;
                }
            }
        }
    }
    int avail=getAvailable(x,y);
    for(int sk=avail;sk;sk-=lowbit(sk)){
        int bit=lowbit(sk);
        int num=lowbit2pos[bit]; // 0-8，对应数字1-9
        clearBit(row[x],num);
        clearBit(col[y],num);
        clearBit(cell[x/3][y/3],num);
        sudoku[x*N+y]='1'+num;
        if(dfs(empty-1)) return true;
        sudoku[x*N+y]=BLANK;
        setBit(row[x],num);
        setBit(col[y],num);
        setBit(cell[x/3][y/3],num);
    }
    return false;
}

int main(){
    precompute();
    sudoku=readSudoku();
    init();
    int empty=0;
    for(int i=0;i<N;++i){
        for(int j=0;j<N;++j){
            if(sudoku[i*N+j]==BLANK){
                empty++;
            }else{
                int num=sudoku[i*N+j]-'1';
                clearBit(row[i],num);
                clearBit(col[j],num);
                clearBit(cell[i/3][j/3],num);
            }
        }
    }
    dfs(empty);
    printSudoku(sudoku);
    return 0;
}