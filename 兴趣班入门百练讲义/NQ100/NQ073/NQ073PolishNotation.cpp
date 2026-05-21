//NQ073 递归求波兰表达式
#include <iostream> 
#include <cmath>
using namespace std; 
double PolishNotation() 
{
    char str[32];
    cin>>str; //读入下一个表达式
    switch (str[0])
    {
    case '+': return PolishNotation() + PolishNotation();
        break;
    case '-': return PolishNotation() - PolishNotation();
        break;
    case '*': return PolishNotation() * PolishNotation();
        break;
    case '/':return PolishNotation() / PolishNotation();
    default:
        return atof(str); //把字符串转换为浮点数
    break;
    }
}
int main() {

    printf("%lf",PolishNotation());  
    return 0;
}
