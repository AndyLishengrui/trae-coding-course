//NQ047数组去重问题
#include <iostream>
using namespace std;
//统计前size中，去重后的数值个数
int SumofUnique(int a[], int size) {
  int cnt = 0;  //个数
  for (int i = 0; i < size; i++) {
    bool is_exist = false;
    for (int j = 0; j < i; j++)
      if (a[j] == a[i]) {
        is_exist = true;
        break;
      }
    if (!is_exist) cnt++;  //统计
  }
  return cnt;  //独一无二值的个数
}

int main() {
  int a[1000];
  int n, size;
  cin >> n >> size;
  for (int i = 0; i < n; i++) cin >> a[i];
  //前size个数去重后，数值长度变为n-size+SumofUique
  cout << n - size + SumofUnique(a, size) << endl;
  return 0;
}