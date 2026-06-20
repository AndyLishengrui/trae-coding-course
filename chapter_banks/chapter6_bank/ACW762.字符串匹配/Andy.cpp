#include <cstdio>
#include <cstring>
int main() {
  double k;
  char a[110],b[110];
  scanf("%lf%s%s",&k,a,b);
  int match=0;
  int la=strlen(a),lb=strlen(b);
  for(int i=0;i+lb<=la;i++) {
    if(!strncmp(a+i,b,lb)) {match=1;break;}
  }
  printf(match?"yes\n":"no\n");
  return 0;
}
