
#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

// class Of Arighm
class Arighm
{
public:
	// 构造函数
	Arighm();
	// 构造函数
	~Arighm();
	// 生成含有numOfNode个运算数字的随机表达式框架
	void CreateEx(int numOfNode);
	// 给生成的表达式框架填入符合条件的随机的数字
	int Count();
	// 输出所生成的表达式
	void Display();
	
private:
	// 比较运算符的优先级
	bool OperIsHigher();
	// 得到运算符的权值
	int GetPriOfOper(const char oper);

private:
	int iResult;
		// 表达式的结果
	char oper;
		// 表达式的运算符
	Arighm *lhs;
		// 表达式的左节点
	Arighm *rhs;
		// 表达式的右节点
	bool isRoot;
		// 该表达式是否为最终的表达式
	Arighm *Parent;
		// 表达式的父节点
	bool isLeft;
		// 是否为左节点(为了输出是加括号用)
};
