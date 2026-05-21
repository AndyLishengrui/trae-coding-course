// 作者：槑qwq
// 链接：https://www.acwing.com/solution/acwing/content/3320/
// 来源：AcWing
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
#include<bits/stdc++.h>
using namespace std;
int mp[11][11],maxx,now=1;
bool he[11][11],sh[11][11],fa[5][5][11];
struct node
{
    int id,data;
}ha[11];
bool camp(node a,node b)
{
    return a.data>b.data;
}

void print()
{
    int ans=0;
    for(int i=1;i<=9;++i) ans+=mp[1][i]*6;
    for(int i=1;i<=9;++i) ans+=mp[9][i]*6;
    for(int i=2;i<=8;++i) ans+=mp[i][1]*6;
    for(int i=2;i<=8;++i) ans+=mp[i][9]*6;

    for(int i=2;i<=8;++i) ans+=mp[2][i]*7;
    for(int i=2;i<=8;++i) ans+=mp[8][i]*7;
    for(int i=3;i<=7;++i) ans+=mp[i][2]*7;
    for(int i=3;i<=7;++i) ans+=mp[i][8]*7;

    for(int i=3;i<=7;++i) ans+=mp[3][i]*8;
    for(int i=3;i<=7;++i) ans+=mp[7][i]*8;
    for(int i=4;i<=6;++i) ans+=mp[i][3]*8;
    for(int i=4;i<=6;++i) ans+=mp[i][7]*8;

    for(int i=4;i<=6;++i) ans+=mp[4][i]*9;
    for(int i=4;i<=6;++i) ans+=mp[6][i]*9;
    ans+=mp[5][4]*9;
    ans+=mp[5][6]*9;

    ans+=mp[5][5]*10;

    maxx=max(maxx,ans);
}

void dfs(int x,int y)
{
    if(mp[x][y])
    {
        if(now==9 && y==9) print();
        if(y==9) dfs(ha[++now].id,1),now--;
        else dfs(x,y+1);
    }
    else
    {
        for(int i=1;i<=9;++i)
        {
            if(!he[x][i] && !sh[y][i] && !fa[(x+2)/3][(y+2)/3][i])
            {
                he[x][i]=1;
                sh[y][i]=1;
                fa[(x+2)/3][(y+2)/3][i]=1;
                mp[x][y]=i;
                if(now==9 && y==9) print();
                if(y==9) dfs(ha[++now].id,1),now--;
                else dfs(x,y+1);
                he[x][i]=0;
                sh[y][i]=0;
                fa[(x+2)/3][(y+2)/3][i]=0;
                mp[x][y]=0;
            }
        }
    }
}

int main()
{
    for(int i=1;i<=9;++i)
    {
        ha[i].id=i;
        for(int j=1;j<=9;++j)
        {
            scanf("%d",&mp[i][j]);
            if(mp[i][j])
            {
                he[i][mp[i][j]]=1;
                sh[j][mp[i][j]]=1;
                fa[(i+2)/3][(j+2)/3][mp[i][j]]=1;
                ha[i].data++;
            }
        }
    }
    sort(ha+1,ha+10,camp);

    dfs(ha[1].id,1);

    if(maxx>0) printf("%d",maxx);
    else cout<<-1;

    return 0;
}

