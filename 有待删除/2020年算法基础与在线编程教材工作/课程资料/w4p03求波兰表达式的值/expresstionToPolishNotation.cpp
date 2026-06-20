// 中缀表达式转换为前缀表达式
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <stack>
#include <algorithm>
using namespace std;

void GetInfix(vector<string>& infix)
{
    infix.clear();
    string line;
    getline(cin, line);

    istringstream sin(line);
    string tmp;
    while (sin >> tmp)
    {
        infix.push_back(tmp);
    }
}

// 初始化操作符
void InitOperators(map<string, int>& opers)
{
    opers.clear();
    opers["("] = 100;
    opers[")"] = 900;
    opers["+"] = 100;
    opers["-"] = 100;
    opers["*"] = 200;
    opers["/"] = 200;
}

bool IsOperator(const string& op, const map<string, int>& opers)
{
    auto cit = opers.find(op);
    if (cit != opers.end())
    {
        return true;
    }
    else
    {
        return false;
    }
}

void InfixToPrefix(const vector<string>& infix, vector<string>& prefix, map<string, int>& opers)
{
    prefix.clear();
    stack<string> stk; // 操作符栈
    for (int i = infix.size() - 1; i >= 0; --i) // 从右到左扫描
    {
        if (!IsOperator(infix[i], opers)) // 如果是操作数
        {
            prefix.push_back(infix[i]);
        }
        else // 如果是操作符
        {
            if (infix[i] == ")") // 如果是右括号，则直接入栈
            {
                stk.push(infix[i]);
            }
            else if (infix[i] == "(") // 如果是左括号
            {
                // 依次弹出栈中的操作符，直至遇到右括号
                while (!stk.empty())
                {
                    if (stk.top() == ")")
                    {
                        stk.pop();
                        break;
                    }
                    else
                    {
                        prefix.push_back(stk.top());
                        stk.pop();
                    }
                }
            }
            else // 如果是其他操作符
            {
                while (!stk.empty() && stk.top() != ")" && opers[stk.top()] > opers[infix[i]]) // 栈顶操作符优先级大于当前操作符优先级
                {
                    prefix.push_back(stk.top());
                    stk.pop();
                }
                // 将当前操作符入栈
                stk.push(infix[i]);
            }
        }
    }

    // 检测操作符栈是否为空
    while (!stk.empty())
    {
        prefix.push_back(stk.top());
        stk.pop();
    }
    // 将prefix翻转
    reverse(prefix.begin(), prefix.end());
    return;
}

void Display(const vector<string>& fix)
{
    for (auto i = 0; i != fix.size(); ++i)
    {
        cout << fix[i] << ' ';
    }
    cout << endl;
}

int main()
{
    map<string, int> opers;
    InitOperators(opers);
    cout<<"begin test:"<<endl;
    while (true)
    {
        vector<string> infix, prefix;
        GetInfix(infix);

        Display(infix);

        InfixToPrefix(infix, prefix, opers);
        Display(prefix);
        cout << endl;
    }
    return 0;
}
