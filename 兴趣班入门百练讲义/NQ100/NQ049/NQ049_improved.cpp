#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    string s;
    while (getline(cin, s)) {
        // 将所有'5'替换为空格
        for (char &c : s) if (c == '5') c = ' ';
        
        istringstream iss(s);
        vector<int> nums;
        string token;
        
        // 处理每个分割后的token
        while (iss >> token) {
            size_t start = token.find_first_not_of('0');
            if (start == string::npos) {
                nums.push_back(0); // 全为0的情况
            } else {
                nums.push_back(stoi(token.substr(start))); // 去除前导零
            }
        }
        
        sort(nums.begin(), nums.end());
        
        // 输出结果
        for (size_t i = 0; i < nums.size(); ++i) {
            if (i) cout << ' ';
            cout << nums[i];
        }
        cout << endl;
    }
    return 0;
}