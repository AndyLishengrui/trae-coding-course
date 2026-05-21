// NQ035 字符串奇偶位互换
int main() {
  int n;
  // 输入n的值
  cin >> n;
  // 循环n次
  while (n--) {
    string s;
    // 输入字符串s
    cin >> s;
    // 遍历字符串s的索引，步长为2
    for (int i = 0; i < s.length() - 1; i += 2)
      // 交换s[i]与s[i+1]
      swap(s[i], s[i + 1]); 
    // 输出交换后的字符串s
    cout << s << endl;
  }
  return 0;
}