// NQ033 电话号码缩短
// 将电话号码缩短为固定前缀6加上最后5位
#include <string>
#include <iostream>
using namespace std;

int main() {
    int n; cin >> n;  // 读取测试用例数量
    while (n--) {  // 遍历每个测试用例
        string phone;
        cin >> phone;  // 读取电话号码
        // 固定前缀6加上原电话号码的最后5位
        string short_num = "6" + phone.substr(phone.length() - 5);
        cout << short_num << endl;  // 输出缩短后的电话号码
    }
    return 0;
}