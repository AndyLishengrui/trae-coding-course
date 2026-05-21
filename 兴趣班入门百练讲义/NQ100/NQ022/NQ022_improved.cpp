// NQ022 竞选投票
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    int n;
    cin >> n;
    vector<int> v(n);
    for(int i=0; i<n; i++) {
        int x;
        cin >> x;
        v[i] = x/2 + 1;  // 每个班级需要超过半数的票数
    }
    sort(v.begin(), v.end());
    int need = n/2 + 1, total = 0;
    for(int i=0; i<need; i++) {
        total += v[i];  // 取所需班级数的最小票数
    }
    cout << total << '\n';
    return 0;
}