#include <iostream>
#include <string>

// 引入常用的 std 命名空间元素，符合竞赛环境和可读性要求
using std::cin;
using std::cout;
using std::endl;
using std::string;

// 处理单个密码安全检查的逻辑
void CheckPasswordSafety() {
  string s;
  // 读取密码
  if (!(cin >> s)) {
    return;
  }

  int len = s.length();

  // 条件 (1): 检查密码长度 (必须在 8 到 16 之间，包含边界)
  if (len < 8 || len > 16) {
    cout << "NO" << endl;
    return; // 长度不符合要求，结束当前测试用例
  }

  // 记录四种字符类型是否出现过：
  // [0]: 小写字母, [1]: 大写字母, [2]: 数字, [3]: 特殊符号
  int type_present[4] = {0};

  for (char ch : s) {
    bool is_lower = (ch >= 'a' && ch <= 'z');
    bool is_upper = (ch >= 'A' && ch <= 'Z');
    bool is_digit = (ch >= '0' && ch <= '9');
    // 特殊符号集合: ~, !, @, #, $, %, ^
    bool is_special = (ch == '~' || ch == '!' || ch == '@' || ch == '#' ||
                       ch == '$' || ch == '%' || ch == '^');

    // 统计出现过的字符类型。根据题意，输入密码仅包含这四种字符。
    if (is_lower) {
      type_present[0] = 1;
    } else if (is_upper) {
      type_present[1] = 1;
    } else if (is_digit) {
      type_present[2] = 1;
    } else if (is_special) {
      type_present[3] = 1;
    }
    // 如果输入保证只包含这四种类型，则无需额外的输入校验失败处理。
  }

  // 统计出现的字符类型总数
  int types_count = type_present[0] + type_present[1] + type_present[2] + type_present[3];

  // 条件 (2): 密码中必须包含四种字符中至少三种 (types_count >= 3)
  if (types_count >= 3) {
    cout << "YES" << endl;
  } else {
    cout << "NO" << endl;
  }
}

int main() {
  // 优化输入输出速度
  std::ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int t;
  // 读取测试数据数量 T
  if (!(cin >> t)) {
    return 0;
  }

  // 循环处理 T 个测试用例
  while (t--) {
    CheckPasswordSafety();
  }

  return 0;
}