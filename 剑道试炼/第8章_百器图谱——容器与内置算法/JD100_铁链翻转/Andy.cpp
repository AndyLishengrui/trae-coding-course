#include <iostream>
#include <stack>
using namespace std;

// 用栈实现链表反转：读入时压栈，输出时弹栈（后进先出 = 反转）
int main() {
    stack<int> stk;
    int x;
    while (cin >> x && x != -1) {
        stk.push(x);
    }
    while (!stk.empty()) {
        cout << stk.top();
        stk.pop();
        if (!stk.empty()) cout << " ";
    }
    cout << endl;
    return 0;
}
