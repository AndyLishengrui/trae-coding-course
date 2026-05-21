// NQ042 不包含重复字符的最长子串长度
#include <cstring>
#include <iostream>
#include <unordered_map>
using namespace std;

int lengthOfLongestSubstring(string s) {
  //暴力枚举的思路：
  //枚举所有以i结尾的字串，对于每个以i结尾的字串，计算最长的不重复字符串长度
  unordered_map<char, int> heap;  //存储{char,出现次数}的哈希表
  //使用双指针的方法计算
  int res = 0;  //长度
  for (int i = 0, j = 0; i < s.size(); i++) {
    heap[s[i]]++;  //将s[i]插入堆，并且s[i]的映射项++
    //需要判断从s[j]-->s[i]的字符是否有重复，采用O(1)的堆最快
    //若[j,i]区间代表最长的不重复字串，那么唯有新的字符s[i]会导致出现重复字符
    //因此若s[i]已经出现，那么就移动j,从s[j,i]中间剔除与s[i]重复的字符
    while (heap[s[i]] > 1) heap[s[j++]]--;  //这是此方法的精华所在，大家仔细品味
    res = max(res, i - j + 1);  //取最大值
  }
  return res;
}
int main() {
  string s;
  cin >> s;
  cout << lengthOfLongestSubstring(s) << endl;
  return 0;
}
