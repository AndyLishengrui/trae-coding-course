#include <iostream>
using namespace std;

// 计算x的二进制中最后一个1所构成的整数
inline int lowbit(int x) {
    return x & -x;
}

int countOnes(int x) {
    int res = 0;
    // 每次减去x的最后一个1，直到x为0
    while (x) {
        x -= lowbit(x);
        res++;
    }
    return res;
}

int main() {
    int n, x;
    cin >> n;
    
    for (int i = 0; i < n; i++) {
        cin >> x;
        cout << countOnes(x) << " ";
    }
    cout << endl;
    
    return 0;
}