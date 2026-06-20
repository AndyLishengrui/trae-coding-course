#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 合并两条有序链表
// 读入两行，每行以-1结尾，输出合并后的有序序列
int main() {
    vector<int> a;
    int x;
    // 读入第一条链表
    while (cin >> x && x != -1) a.push_back(x);
    // 读入第二条链表
    while (cin >> x && x != -1) a.push_back(x);
    sort(a.begin(), a.end());
    for (size_t i = 0; i < a.size(); i++) {
        cout << a[i];
        if (i + 1 < a.size()) cout << " ";
    }
    cout << endl;
    return 0;
}
