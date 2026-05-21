#include<bits/stdc++.h> 
using namespace std;
#define AC 0
#define WA 1
#define ERROR -1

int spj(FILE *input, FILE *user_output);

void close_file(FILE *f) {
    if(f != NULL) fclose(f);
}

int main(int argc, char *args[]) {
FILE *input = NULL, *user_output = NULL;
    int result;
    if(argc != 3){
        printf("Usage: spj x.in x.out\n");
        return ERROR;
    }
    input = fopen(args[1], "r");
    user_output = fopen(args[2], "r");
    if(input == NULL || user_output == NULL){
        printf("Failed to open output file\n");
        close_file(input);
        close_file(user_output);
        return ERROR;
    }

    result = spj(input, user_output);
    printf("result: %d\n", result);
    
    close_file(input);
    close_file(user_output);
    return result;
}
//-----------------------------------------------
int N,M,du[100010]={},itdu[100010]={};
vector<int>e[100010];
queue<int>q;
bool no_solution;

void ReadD(FILE *input)
{
	fscanf(input,"%d%d",&N,&M);
	for(int a=1;a<=M;a++)
	{
		int u,v;
		fscanf(input,"%d%d",&u,&v);
		e[u].push_back(v);
		du[v]++;
		itdu[v]++;
	}
	
    for(int a=1;a<=N;a++) if(du[a]==0) q.push(a);
    
    int cnt=0;
    while(!q.empty())
    {
        int now=q.front();
        q.pop();
        cnt++;
        for(auto nxt:e[now])
        {
            du[nxt]--;
            if(du[nxt]==0) q.push(nxt);
        }
    }
    no_solution=(cnt!=N);
}

bool Check(FILE *user_output)
{
	if(no_solution)
	{
		int t;
		if(fscanf(user_output,"%d",&t)==EOF) return 0;
		if(t==-1) return 1;
		else return 0;
	}
	for(int a=1;a<=N;a++)
	{
		int t;
		if(fscanf(user_output,"%d",&t)==EOF) return 0;
        if(t<1) return 0;
		if(itdu[t]) return 0;
		for(auto nxt:e[t]) itdu[nxt]--;
	}
	return 1;
}
//-----------------------------------------------
int spj(FILE *input, FILE *user_output) {
    ReadD(input);
    if(Check(user_output)) return AC;
    else return WA;
}
