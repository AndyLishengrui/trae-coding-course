#include <cstdio>
#include <algorithm>
using namespace std;

const int kMaxArraySize = 100005;
long long nums[kMaxArraySize];

int main() {
    int n;
    scanf("%d", &n);
    
    for (int i = 0; i < n; ++i) {
        scanf("%lld", &nums[i]);
    }
    
    long long target;
    scanf("%lld", &target);
    
    sort(nums, nums + n);
    
    for (int i = 0; i < n; ++i) {
        long long complement = target - nums[i];
        auto it = lower_bound(nums + i + 1, nums + n, complement);
        
        if (it != nums + n && *it == complement) {
            printf("%lld %lld\n", nums[i], complement);
            return 0;
        }
    }
    
    printf("No\n");
    return 0;
}