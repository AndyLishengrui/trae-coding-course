#include <cstdio>
int main() {
  int n;
  while(scanf("%d",&n)==1&&n) {
    for(int i=0;i<n;i++) {
      for(int j=0;j<n;j++) {
        int v=i<j?i:j;
        int w=n-1-i<n-1-j?n-1-i:n-1-j;
        int m=v<w?v:w;
        printf("%3d",m+1);
      }
      printf("\n");
    }
    printf("\n");
  }
  return 0;
}
