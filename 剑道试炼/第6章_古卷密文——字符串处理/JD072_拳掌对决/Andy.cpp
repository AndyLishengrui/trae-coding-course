#include <cstdio>
#include <cstring>
// 拳掌对决：剪刀石头布胜负判断
int main() {
  char a[20],b[20];
  while(scanf("%s%s",a,b)==2) {
    if(!strcmp(a,b)) printf("Tie\n");
    else if((!strcmp(a,"Hunter")&&!strcmp(b,"Gun"))||(!strcmp(a,"Gun")&&!strcmp(b,"Bear"))||(!strcmp(a,"Bear")&&!strcmp(b,"Hunter"))) printf("Player1\n");
    else printf("Player2\n");
  }
  return 0;
}
