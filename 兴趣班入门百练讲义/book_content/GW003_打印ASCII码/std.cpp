#include <iostream>
#include <limits>

/**
 * @brief 主函数，用于读取字符并输出其ASCII码。
 * 
 * 核心原理是利用C++中char类型作为整数类型的特性，通过类型转换获取其数值。
 */
int main() {
  // 提高输入输出效率，尽管对于单次字符读取影响很小，但这是竞赛编程的标准实践。
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(NULL);

  // 定义一个char变量用于存储输入的字符。
  char input_char;

  // 读取一个可见字符。
  // 注意：C++的 >> 操作符默认会跳过输入流前的空白字符，
  // 题目保证输入是非空格的可见字符，因此直接读取是合适的。
  if (!(std::cin >> input_char)) {
    // 如果读取失败，通常在竞赛中不处理，但为了严谨性可以返回。
    return 0;
  }

  // 核心逻辑：进行显式类型转换。
  // 将 char 类型强制转换为 int 类型，C++ 会自动取出存储在 char 
  // 变量中的数值（即 ASCII 码）。
  int ascii_value = static_cast<int>(input_char);

  // 输出结果。
  std::cout << ascii_value << "\n";

  return 0;
}