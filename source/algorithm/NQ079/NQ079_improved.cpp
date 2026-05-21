#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

const double EPS = 1e-6;
const int N = 4;

bool isZero(double x) {
    return fabs(x) <= EPS;
}

bool count24(vector<double> nums) {
    int n = nums.size();
    if (n == 1) {
        return isZero(nums[0] - 24);
    }
    
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            vector<double> next;
            for (int k = 0; k < n; k++) {
                if (k != i && k != j) {
                    next.push_back(nums[k]);
                }
            }
            
            // 加法
            next.push_back(nums[i] + nums[j]);
            if (count24(next)) return true;
            next.pop_back();
            
            // 乘法
            next.push_back(nums[i] * nums[j]);
            if (count24(next)) return true;
            next.pop_back();
            
            // 减法
            next.push_back(nums[i] - nums[j]);
            if (count24(next)) return true;
            next.pop_back();
            
            // 减法 (交换顺序)
            next.push_back(nums[j] - nums[i]);
            if (count24(next)) return true;
            next.pop_back();
            
            // 除法
            if (!isZero(nums[j])) {
                next.push_back(nums[i] / nums[j]);
                if (count24(next)) return true;
                next.pop_back();
            }
            
            // 除法 (交换顺序)
            if (!isZero(nums[i])) {
                next.push_back(nums[j] / nums[i]);
                if (count24(next)) return true;
                next.pop_back();
            }
        }
    }
    
    return false;
}

int main() {
    while (true) {
        vector<double> nums(N);
        bool isEnd = true;
        for (int i = 0; i < N; i++) {
            cin >> nums[i];
            if (!isZero(nums[i])) isEnd = false;
        }
        if (isEnd) break;
        
        if (count24(nums)) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    return 0;
}
