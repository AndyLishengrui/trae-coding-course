// NQ028 0-1矩阵统计
// 统计矩阵中值为1的元素个数
#include <iostream>
using namespace std;

int main() {
    int t; cin >> t;  
    while (t--) {  
        int a, b, x, cnt = 0;  
        cin >> a >> b;  
        for (int i = 1; i <= a; i++) {  
            for (int j = 1; j <= b; j++) {  
                cin >> x;  
                if (x == 1) cnt++;  
            }
        }
        cout << cnt << endl; 
    }
    return 0;
}