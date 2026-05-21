# 矩阵幂求和 (ID: ACW225)

## 题目描述
<p><span style="color: rgb(51, 51, 51);">给定</span><span style="color: rgb(51, 51, 51);">n×n</span><span style="color: rgb(51, 51, 51);">矩阵</span><span style="color: rgb(51, 51, 51);">A</span><span style="color: rgb(51, 51, 51);">和正整数</span><span style="color: rgb(51, 51, 51);">k</span><span style="color: rgb(51, 51, 51);">，求和</span><span style="color: rgb(51, 51, 51);">S=A+A^2+A<span style="color: rgb(51, 51, 51);">^</span>3+…+A<span style="color: rgb(51, 51, 51);">^k</span></span><span style="color: rgb(51, 51, 51);"><br /></span><br /></p>

## 输入描述
<p>输入只包含一个测试用例。</p><p>第一行输入包含三个正整数n，k，和m。</p><p>接下来n行，每行包含n个非负整数（均不超过32,768），用以描绘矩阵A。</p><p><br /></p><p><span style="color: rgb(51, 51, 51);">1≤n≤30</span></p><p><br /><span style="color: rgb(51, 51, 51);">1≤k≤10^9</span></p><p><br /><span style="color: rgb(51, 51, 51);">1≤m&lt;10^4</span></p>

## 输出描述
<p><span style="color: rgb(51, 51, 51);">按与描述矩阵</span><span style="color: rgb(51, 51, 51);">A</span><span style="color: rgb(51, 51, 51);">相同的方式，输出将</span><span style="color: rgb(51, 51, 51);">S</span><span style="color: rgb(51, 51, 51);">中所有元素对</span><span style="color: rgb(51, 51, 51);">m</span><span style="color: rgb(51, 51, 51);">取模后得到的矩阵。</span><br /></p>

## 样例
### Sample 1
**Input:**
```
2 2 4
0 1
1 1
```
**Output:**
```
1 2
2 3
```

## 提示

