#include <iomanip>
#include <iostream>
using namespace std;

int main() {
    int t; cin >> t;
    cout << fixed << setprecision(3);
    while (t--) {
        float u, v, w, l; cin >> u >> v >> w >> l;
        float res = w * l / (u + v);  // 计算时间：w*l/(u+v)
        cout << res << endl;
    }
    return 0;
}