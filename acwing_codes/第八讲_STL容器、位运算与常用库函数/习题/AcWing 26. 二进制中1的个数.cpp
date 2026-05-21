class Solution {
public:
    // lowbit写法
    int NumberOf1(int n) {
        int res = 0;

        while (n) n -= n & -n, res ++;

        return res;
    }
};