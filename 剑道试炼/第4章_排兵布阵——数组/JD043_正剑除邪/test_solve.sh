#!/bin/bash
set -euo pipefail
DIR="/Users/andyshengruilee/Downloads/基于Trae的编程兴趣班入门百练.worktrees/agents-inland-mule/题库3/第4章_排兵布阵——数组/JD043_正剑除邪"
g++ -std=c++11 -o "$DIR/solve" "$DIR/solve.cpp"
pass=0
fail=0
for i in $(seq 1 10); do
    in="$DIR/testcase/$i.in"
    out="$DIR/testcase/$i.out"
    got=$(mktemp)
    "$DIR/solve" < "$in" > "$got"
    if diff -q "$got" "$out" > /dev/null; then
        echo "Case $i: PASS"
        pass=$((pass+1))
    else
        echo "Case $i: FAIL"
        diff "$got" "$out" | head -10
        fail=$((fail+1))
    fi
    rm -f "$got"
done
echo "--- JD043: $pass passed, $fail failed ---"
rm -f "$DIR/solve"
