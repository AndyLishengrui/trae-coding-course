#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 用 vector + struct 存储三元组，自定义排序
struct Record {
    int x;      // 编号
    double y;   // 重量
    string z;   // 名称
};

bool cmp(const Record &a, const Record &b) {
    if (a.x != b.x) return a.x < b.x;
    return a.y < b.y;
}

int main() {
    int n;
    cin >> n;

    vector<Record> records;
    for (int i = 0; i < n; i++) {
        Record r;
        cin >> r.x >> r.y >> r.z;
        records.push_back(r);
    }

    sort(records.begin(), records.end(), cmp);

    for (int i = 0; i < n; i++) {
        printf("%d %.2lf %s\n", records[i].x, records[i].y, records[i].z.c_str());
    }
    return 0;
}
