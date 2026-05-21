#include <iostream>
#include <climits>
using namespace std;

int main() {
    int n;
    while (cin >> n && n > 0) {
        int a[10007];
        int min_val = INT_MAX, min_idx = 0;
        
        // 读取数组并找到最小值及其下标
        for (int i = 0; i < n; i++) {
            cin >> a[i];
            if (a[i] < min_val) {
                min_val = a[i];
                min_idx = i;
            }
        }
        
        // 交换最小值与第一个元素
        if (min_idx != 0) {
            int temp = a[0];
            a[0] = a[min_idx];
            a[min_idx] = temp;
        }
        
        // 输出交换后的数组
        for (int i = 0; i < n; i++) {
            if (i > 0) cout << " ";
            cout << a[i];
        }
        cout << endl;
    }
    return 0;
}