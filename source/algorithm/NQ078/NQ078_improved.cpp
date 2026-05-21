// NQ078 表达式求值
#include <cstdlib>
#include <cstring>
#include <iostream>
using namespace std;
int factor_value();     // 递归函数读入并处理因子
int term_value();       // 递归函数读入并处理项
int expression_value(); // 递归函数读入并处理表达式
int main() {
    cout << expression_value() << endl;
    return 0;
}

int expression_value() // 求一个表达式的值
{
    int result = term_value(); // 求第一项的值
    bool more = true;
    while (more) {
        char op = cin.peek(); // 看一个字符,不取走
        if (op == '+' || op == '-') {
            cin.get(); // 从输入中取走一个字符
            int value = term_value();
            if (op == '+')
                result += value;
            else
                result -= value;
        } else
            more = false;
    }
    return result;
}

int term_value() // 求一个项的值
{
    int result = factor_value(); // 求第一个因子的值
    while (true) {
        char op = cin.peek();
        if (op == '*' || op == '/') {
            cin.get();
            int value = factor_value();
            if (op == '*')
                result *= value;
            else
                result /= value;
        } else
            break;
    }
    return result;
}

int factor_value() // 求一个因子的值
{
    int result = 0;
    char c = cin.peek();
    if (c == '(') {
        cin.get(); // 读入左括号
        result = expression_value();
        cin.get(); // 读入右括号，不做任何处理
    } else {
        while (isdigit(c)) { // 按字符读入十进制数
            result = 10 * result + c - '0';
            cin.get();
            c = cin.peek();
        }
    }
    return result;
}
