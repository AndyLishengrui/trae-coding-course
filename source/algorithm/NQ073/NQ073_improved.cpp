#include <iostream>
using namespace std;
double calc() {
    char token[32];
    cin >> token;
    switch (token[0]) {
        case '+': return calc() + calc();
        case '-': return calc() - calc();
        case '*': return calc() * calc();
        case '/': return calc() / calc();
        default: return atof(token);
    }
}
int main() {
    double res = calc(); // 递归计算波兰表达式
    printf("%lf", res);
    return 0;
}
