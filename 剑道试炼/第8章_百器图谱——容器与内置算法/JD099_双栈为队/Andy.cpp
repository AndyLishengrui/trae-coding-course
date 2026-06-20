#include <iostream>
#include <stack>
#include <string>
using namespace std;

// 用两个栈模拟队列
// 栈1负责入队，栈2负责出队
// 出队时若栈2空，把栈1全部倒入栈2
stack<int> s1, s2;

void transfer() {
    while (s1.size()) {
        s2.push(s1.top());
        s1.pop();
    }
}

int main() {
    string cmd;
    while (cin >> cmd) {
        if (cmd == "push") {
            int x; cin >> x;
            s1.push(x);
        } else if (cmd == "pop") {
            if (s2.empty()) transfer();
            cout << s2.top() << endl;
            s2.pop();
        } else if (cmd == "empty") {
            cout << (s1.empty() && s2.empty() ? "yes" : "no") << endl;
        }
    }
    return 0;
}
