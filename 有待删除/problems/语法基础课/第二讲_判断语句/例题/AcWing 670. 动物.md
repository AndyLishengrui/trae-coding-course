# AcWing 670. 动物

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/670/

## 题目描述
> 待补充

### 输入格式
> 待补充

### 输出格式
> 待补充

### 样例
> 待补充

## AC代码

```cpp
if (a == "vertebrado")
{
  if (b == "ave")
  {
    if (c == "carnivoro") cout << "aguia" << endl;
    else cout << "pomba" << endl;
  }
  else
  {
    if (c == "onivoro") cout << "homem" << endl;
    else cout << "vaca" << endl;
  }
}
else 
{
 if (b == "inseto") 
  {
    if (c == "hematofago") cout << "pulga" << endl;
    else cout << "lagarta" << endl;
  }
  else
  {
    if (c == "hematofago") cout << "sanguessuga" << endl;
    else cout << "minhoca" << endl;
  }
}
```
