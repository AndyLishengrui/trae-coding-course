#include <iostream>
using namespace std;

// 判断三个数是否能构成三角形
bool canFormTriangle(int a, int b, int c) {
    // 三角形的构成条件是任意两边之和大于第三边
    return (a + b > c) && (a + c > b) && (b + c > a);
}

int main() {
    int n;
    cin >> n;
    
    for (int i = 0; i < n; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        
        if (canFormTriangle(a, b, c)) {
            cout << "OK" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    
    return 0;
}