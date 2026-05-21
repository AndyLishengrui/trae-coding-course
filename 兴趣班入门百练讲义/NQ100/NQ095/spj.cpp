#include <iostream>
#include <cstring>
using namespace std;

//todo
char a[10][10]=
   { {"530070000"},
    {"600195000"},
    {"098000060"},
    {"800060003"},
    {"400803001"},
    {"700020006"},
    {"060000280"},
    {"000419005"},
    {"000080079"}};

char b[10][10];

bool Check()
{
	int i,j,k,i1,j1;
    char s[16];
	for(i=1;i<=9;i++)
	{
	   cin>>s;
	  if(strlen(s)!=9)
	     return false;//长度不对

	  for(j=1;j<=9;j++)
	  {
         b[i][j]=s[j-1]-'0';
		 if(b[i][j]<1||b[i][j]>9)
			 return false;//出现非法字符
		 if(a[i][j]!=0 && a[i][j]!=b[i][j])
			 return false;//与初始值不匹配 Missfit with initial data
	  }
	}
	// check in line
	for(i=1;i<=9;i++)
	{
		for(j=1;j<=9;j++) s[j]=0;
		for(j=1;j<=9;j++) 
		{
			if(s[b[i][j]]==1)
			   return false;//行有错误答案
		    else b[i][j]=1;
		}
	}
	// check in column
	for(j=1;j<=9;j++)
	{
		for(i=1;i<=9;i++) s[i]=0;
		for(i=1;i<=9;i++) 
		{
			if(s[b[i][j]]==1)
			    return false;//列有错误法案
		    else b[i][j]=1;
		}
	}
    // check in squares
	for(i=1;i<=9;i+=3)
	{
		for(j=1;j<=9;j+=3) 
		{
			for(k=1;k<=9;k++) s[k]=0;
			for(i1=0;i1<3;i1++)
				for(j1=0;j1<3;j1++)
					if(s[b[i+i1][j+j1]]==1)
                        return false; //方格中有错误答案
		    else b[i+i1][j+j1]=1;
		}
	}
    return true;
}
int main(){
    if (Check()) cout<<"Yes"<<endl;
        else cout<<"No"<<endl;
    return 0;
}
