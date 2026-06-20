#!/bin/bash
set -e
echo "=== 编译 ==="
g++ -std=c++11 -O2 Andy.cpp -o Andy.out
g++ -std=c++11 -O2 gen.cpp -o gen.out
echo "=== 生成测试数据 ==="
mkdir -p testcase
for i in {1..10}; do
    ./gen.out $i > testcase/${i}.in
    ./Andy.out < testcase/${i}.in > testcase/${i}.out
    echo "  测试用例 ${i}: $(wc -c < testcase/${i}.in) bytes"
done
echo "=== 验证样例 ==="
head -1 testcase/1.in | while read line; do echo "  样例输入: $line"; done
head -1 testcase/1.out | while read line; do echo "  样例输出: $line"; done
echo "=== 打包 ==="
mkdir -p 1/testcase
cp problem.json 1/
cp testcase/*.in testcase/*.out 1/testcase/
rm -f xmuoj-import.zip
cd 1 && zip -r ../xmuoj-import.zip . && cd ..
rm -rf 1
echo "✅ 完成！xmuoj-import.zip 已生成"
