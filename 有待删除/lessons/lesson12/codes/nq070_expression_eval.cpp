#include <iostream>
#include <cstring>
#include <algorithm>
#include <stack>
#include <unordered_map>

using namespace std;

stack<int> num; //存储计算过程中的数字
stack<char> op; //存储操作符

void eval()
{
  auto b = num.top(); num.pop();//第二个数
  auto a = num.top(); num.pop();//第一个数
  auto c = op.top(); op.pop();

  int x;
  if (c == '+') x = a + b; 
  else if (c == '-') x = a - b;
  else if (c == '*') x = a * b;
  else x = a / b;
  num.push(x);
}

int main()
{
  //优先级，可扩展为其他符号的优先级
  unordered_map<char,int> pr{{'+',1}, {'-', 1}, {'*',2},{'/',2}};
  string str; //输入都存储在字符串内
  cin >> str; 
  for (int i = 0; i < str.size(); i ++)
  {
    auto c = str[i]; //读入每个char
    if (isdigit(c))  //判断是否是数字
    {
      int x = 0, j = i;
      while (j < str.size() && isdigit(str[j]))
        x = x * 10 + str[j ++] - '0';
      i = j  - 1; // 调整i的位置
      num.push(x); //压栈
    }
    else if (c == '(') op.push(c);
    else if (c == ')') 
    {
      //把前面所有的表达式都出栈运算
      while (op.top() != '(') eval();
      op.pop();
    }
    else 
    {//根据操作符的优先级执行运算
      while (op.size() && op.top() != '(' && pr[op.top()] >= pr[c]) 
      eval();
      op.push(c);
    }
  }
  //处理剩余的操作符
  while(op.size()) eval();
  cout<<num.top() <<endl;
  return 0;
}