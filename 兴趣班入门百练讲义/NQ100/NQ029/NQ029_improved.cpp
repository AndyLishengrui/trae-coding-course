#include <iostream>
using namespace std;

bool isPalindrome(int x) {
    if (x < 0) return false;
    long long res = 0, oldx = x;
    while (x) {
        res = res * 10 + x % 10;
        x /= 10;
    }
    return res == oldx;
}

int main() {
    int n;
    while (cin >> n) {
        cout << (isPalindrome(n) ? "true" : "false") << endl;
    }
    return 0;
}