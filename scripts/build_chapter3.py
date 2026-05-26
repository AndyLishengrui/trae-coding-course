#!/usr/bin/env python3
"""第3章：循环结构——for/while与嵌套循环（14题）"""
import json, re, os, sys, time, tempfile, zipfile, shutil, subprocess
from pathlib import Path

BOOK_ROOT = Path(__file__).parent.parent

PROBLEMS = [
    {"nq":"NQ029","acw":708,"title":"偶数","desc":"小鲁想列出从2到100之间的所有偶数。请你写一个程序，按顺序每行输出一个偶数。这是for循环最基础的应用。","input_fmt":"无输入。","output_fmt":"每行一个偶数，从2到100。","sample_in":"(无)","sample_out":"2\n4\n6\n...\n100","constraint":"输出2到100的所有偶数。","solution":"用for循环从2开始每次步进2：range(2, 101, 2)（Python）或 for(int i=2;i<=100;i+=2)（C++）。这是循环的最简形式——固定次数、固定步长。","technique":"Python的range(start, end, step)三步控制：起始、终止（不含）、步长。C++的for语句分三部分：初始化、条件、增量。","cpp":"#include <iostream>\nusing namespace std;\nint main() {\n    for (int i = 2; i <= 100; i += 2)\n        cout << i << endl;\n    return 0;\n}","py":"for i in range(2, 101, 2):\n    print(i)","gen":"even"},
    {"nq":"NQ030","acw":709,"title":"奇数","desc":"给定一个正整数X，请你输出从1到X（含）之间的所有奇数。","input_fmt":"一行，一个正整数X。","output_fmt":"每行一个奇数，从1到X。","sample_in":"8","sample_out":"1\n3\n5\n7","constraint":"1 ≤ X ≤ 1000","solution":"从1开始每次加2输出奇数。range(1, X+1, 2)（Python）或 for(int i=1;i<=X;i+=2)（C++）。注意上限是X（包含）。","technique":"range(start, end, step)中end是不包含的，所以用X+1。C++中用<=确保X被包含。","cpp":"#include <iostream>\nusing namespace std;\nint main() {\n    int x;\n    cin >> x;\n    for (int i = 1; i <= x; i += 2)\n        cout << i << endl;\n    return 0;\n}","py":"x = int(input())\nfor i in range(1, x + 1, 2):\n    print(i)","gen":"odd"},
    {"nq":"NQ031","acw":712,"title":"正数","desc":"小鲁在分析一组数据。给定6个浮点数，统计其中正数（大于0）的个数。","input_fmt":"6行，每行一个浮点数。","output_fmt":"\"X positive numbers\"，X为正数个数。","sample_in":"7\n-5\n6\n-3.4\n4.6\n12","sample_out":"4 positive numbers","constraint":"−100 ≤ 数值 ≤ 100","solution":"计数循环的标准模板：循环6次，每次读入一个数，如果大于0则计数器加1。Python中可用sum(1 for _ in range(6) if float(input())>0)。","technique":"Python生成器表达式+sum()一行完成计数。C++需显式循环+条件判断。两种写法对照理解计数模式的本质。","cpp":"#include <iostream>\nusing namespace std;\nint main() {\n    int cnt = 0;\n    for (int i = 0; i < 6; i++) {\n        double x; cin >> x;\n        if (x > 0) cnt++;\n    }\n    cout << cnt << \" positive numbers\" << endl;\n    return 0;\n}","py":"cnt = sum(1 for _ in range(6) if float(input()) > 0)\nprint(f\"{cnt} positive numbers\")","gen":"positive"},
    {"nq":"NQ032","acw":714,"title":"连续奇数的和1","desc":"给定两个整数X和Y，计算它们之间（不含X和Y）所有奇数的和。","input_fmt":"一行，两个整数X和Y。","output_fmt":"一个整数，表示奇数和。","sample_in":"6 -5","sample_out":"5","constraint":"−10⁴ ≤ X, Y ≤ 10⁴","solution":"先确保X≤Y（若X>Y则交换），然后从X+1到Y-1遍历，奇数累加。用i%2判断奇数（i%2==1或i%2!=0）。注意负数取模的符号问题。","technique":"Python的if i%2可以判断奇数（因为1是truthy）。C++中注意负数%2可能得到-1，用i%2!=0或i&1判断更安全。","cpp":"#include <iostream>\n#include <algorithm>\nusing namespace std;\nint main() {\n    int x, y, sum = 0;\n    cin >> x >> y;\n    if (x > y) swap(x, y);\n    for (int i = x + 1; i < y; i++)\n        if (i % 2) sum += i;\n    cout << sum << endl;\n    return 0;\n}","py":"x, y = map(int, input().split())\nif x > y: x, y = y, x\nprint(sum(i for i in range(x + 1, y) if i % 2))","gen":"odd_sum"},
    {"nq":"NQ033","acw":716,"title":"最大数和它的位置","desc":"小鲁有一组数据，他想找到最大值以及它第一次出现的位置。给定N和N个整数，找出最大值和位置。","input_fmt":"第一行整数N。第二行N个整数。","output_fmt":"第一行输出最大值。第二行输出位置（从1开始）。","sample_in":"5\n3 2 5 1 4","sample_out":"5\n3","constraint":"1 ≤ N ≤ 100","solution":"循环最值查找的标准模板：初始化max_val=第一个数，pos=1；遍历后续数，如果遇到更大的则更新max_val和pos。注意只更新更大的（>），相等的保留第一个位置。","technique":"Python中max(arr)一行找到最值，arr.index(max_val)找位置。但手写循环理解查找逻辑更重要。enumerate(arr, 1)从1开始编号更直观。","cpp":"#include <iostream>\nusing namespace std;\nint main() {\n    int n, x, mx, pos = 1;\n    cin >> n;\n    for (int i = 1; i <= n; i++) {\n        cin >> x;\n        if (i == 1 || x > mx) { mx = x; pos = i; }\n    }\n    cout << mx << endl << pos << endl;\n    return 0;\n}","py":"n = int(input())\narr = list(map(int, input().split()))\nmx = max(arr)\nprint(mx)\nprint(arr.index(mx) + 1)","gen":"max_pos"},
    {"nq":"NQ034","acw":721,"title":"递增序列","desc":"小鲁发现数学中有很多有趣的数列。请写一个程序：读入整数X，如果X不是0，则输出从1到X的所有整数。重复这个过程直到读入0为止。","input_fmt":"多行，每行一个整数X。以0结束。","output_fmt":"对每个非0的X，输出一行从1到X的整数（空格隔开）。","sample_in":"5\n10\n3\n0","sample_out":"1 2 3 4 5\n1 2 3 4 5 6 7 8 9 10\n1 2 3","constraint":"0 ≤ X ≤ 1000","solution":"while循环的经典应用：当条件满足时持续循环。这里用while(cin>>x && x!=0)或Python的while True + if break。循环体内用for输出1到X。","technique":"Python的while True + break模式。C++的while(cin>>x, x)利用逗号表达式同时读入和判断。注意输出格式：空格隔开，换行结束。","cpp":"#include <iostream>\nusing namespace std;\nint main() {\n    int x;\n    while (cin >> x, x) {\n        for (int i = 1; i <= x; i++) {\n            if (i > 1) cout << \" \";\n            cout << i;\n        }\n        cout << endl;\n    }\n    return 0;\n}","py":"while True:\n    x = int(input())\n    if x == 0: break\n    print(' '.join(str(i) for i in range(1, x + 1)))","gen":"increasing"},
    {"nq":"NQ035","acw":720,"title":"连续整数相加","desc":"给定起始整数A和个数N（N>0），计算从A开始的N个连续整数的和。注意：输入的第二行可能有多余的负数或零，需要一直读入直到遇到第一个正数作为N。","input_fmt":"第一行：整数A。第二行：若干整数，其中第一个大于0的数是N。","output_fmt":"从A开始N个连续整数的和。","sample_in":"3\n-5 0 -3 4 -1","sample_out":"18","constraint":"1 ≤ A,N ≤ 10000","solution":"先读A，然后用while循环跳过第二行的非正数，找到第一个大于0的N。然后for循环累加A, A+1, ..., A+N-1。","technique":"C++的while(cin>>n, n<=0);利用逗号表达式+空循环体跳过非正数。Python用嵌套while True读取并判断。边读边过滤是竞赛编程的常见模式。","cpp":"#include <iostream>\nusing namespace std;\nint main() {\n    int a, n, sum = 0;\n    cin >> a;\n    while (cin >> n, n <= 0);\n    for (int i = 0; i < n; i++) sum += a++;\n    cout << sum << endl;\n    return 0;\n}","py":"a = int(input())\nwhile True:\n    for n in map(int, input().split()):\n        if n > 0: break\n    if n > 0: break\nprint(sum(a + i for i in range(n)))","gen":"consec_sum"},
    {"nq":"NQ036","acw":724,"title":"约数","desc":"小鲁在数学课上学了约数的概念。给定一个正整数N，输出它的所有正约数（从小到大，每行一个）。","input_fmt":"一个正整数N。","output_fmt":"每行一个约数，从小到大。","sample_in":"6","sample_out":"1\n2\n3\n6","constraint":"1 ≤ N ≤ 10⁶","solution":"从1到N遍历，如果N%i==0则i是约数。优化：只需遍历1到√N，找到一个约数i后同时输出N/i。但标准方法更直接。","technique":"约数枚举是理解循环条件判断的经典题。进一步优化可用i*i<=n作循环条件，只枚举到√n。","cpp":"#include <iostream>\nusing namespace std;\nint main() {\n    int n;\n    cin >> n;\n    for (int i = 1; i <= n; i++)\n        if (n % i == 0) cout << i << endl;\n    return 0;\n}","py":"n = int(input())\nfor i in range(1, n + 1):\n    if n % i == 0:\n        print(i)","gen":"divisor"},
    {"nq":"NQ037","acw":723,"title":"PUM","desc":"小鲁在学循环输出格式控制。给定N和M，输出一个N行M列的矩阵，每行从1开始递增，但第M列用\"PUM\"替代数字。","input_fmt":"一行，两个整数N和M。","output_fmt":"N行，每行M个元素。前M-1个是递增数字（空格隔开），第M个是\"PUM\"。","sample_in":"7 4","sample_out":"1 2 3 PUM\n5 6 7 PUM\n9 10 11 PUM\n13 14 15 PUM\n17 18 19 PUM\n21 22 23 PUM\n25 26 27 PUM","constraint":"1 ≤ N,M ≤ 20","solution":"嵌套循环+条件输出的经典题。外层循环控制行（N次），内层循环控制列（M次）。用%M判断是否到达最后一列：每M个位置输出\"PUM\"。","technique":"C++中用cout<<endl换行。Python的print默认换行，print(x, end=' ')可以不换行。在第M个位置用print('PUM')自动换行。","cpp":"#include <iostream>\nusing namespace std;\nint main() {\n    int n, m;\n    cin >> n >> m;\n    for (int i = 1; i <= n * m; i++) {\n        if (i % m == 0) cout << \"PUM\" << endl;\n        else cout << i << \" \";\n    }\n    return 0;\n}","py":"n, m = map(int, input().split())\nfor i in range(1, n * m + 1):\n    if i % m == 0:\n        print(\"PUM\")\n    else:\n        print(i, end=' ')","gen":"pum"},
    {"nq":"NQ038","acw":710,"title":"六个奇数","desc":"给定一个整数X，输出从X开始的连续6个奇数（每个一行）。如果X本身是奇数就是第一个，否则从X+1开始。","input_fmt":"一个整数X。","output_fmt":"6行，每行一个奇数。","sample_in":"8","sample_out":"9\n11\n13\n15\n17\n19","constraint":"0 ≤ X ≤ 10⁹","solution":"先判断X的奇偶性：如果X是偶数，从X+1开始；否则从X开始。然后步进2循环6次输出。简洁写法：if X%2==0: X+=1; for i in range(6): print(X+2*i)。","technique":"用X += 1 - X%2可以一行修正起始值到奇数（X%2==0则+1，==1则+0）。Python中更清晰：X += (X % 2 == 0)。","cpp":"#include <iostream>\nusing namespace std;\nint main() {\n    int x;\n    cin >> x;\n    if (x % 2 == 0) x++;\n    for (int i = 0; i < 6; i++, x += 2)\n        cout << x << endl;\n    return 0;\n}","py":"x = int(input())\nif x % 2 == 0:\n    x += 1\nfor _ in range(6):\n    print(x)\n    x += 2","gen":"six_odds"},
    {"nq":"NQ039","acw":711,"title":"乘法表","desc":"小鲁在背九九乘法表。给定一个整数N，请输出N的乘法表：从1×N到10×N。","input_fmt":"一个整数N。","output_fmt":"10行，每行\"i x N = result\"。","sample_in":"140","sample_out":"1 x 140 = 140\n2 x 140 = 280\n...\n10 x 140 = 1400","constraint":"1 ≤ N ≤ 1000","solution":"for循环从1到10，输出i×N的结果。这是嵌套循环的基础——固定次数的重复计算。","technique":"Python的f\"{i} x {n} = {i*n}\"格式清晰。C++用printf或cout。","cpp":"#include <cstdio>\nint main() {\n    int n;\n    scanf(\"%d\", &n);\n    for (int i = 1; i <= 10; i++)\n        printf(\"%d x %d = %d\\n\", i, n, i * n);\n    return 0;\n}","py":"n = int(input())\nfor i in range(1, 11):\n    print(f\"{i} x {n} = {i * n}\")","gen":"mult_table"},
    {"nq":"NQ040","acw":718,"title":"实验","desc":"小鲁在上生物实验课。记录了N次观察，每次观察有一种动物类型（C=兔子、R=老鼠、F=青蛙）和数量。请统计总数及每种动物的数量和百分比。","input_fmt":"第一行N。接下来N行，每行一个整数和一个字符（数量和类型）。","output_fmt":"按格式输出总计和各类统计及百分比。","sample_in":"10\n10 C\n6 R\n15 F\n5 C\n14 R\n9 C\n6 R\n8 F\n5 C\n14 R","sample_out":"Total: 92 animals\nTotal coneys: 29\nTotal rats: 40\nTotal frogs: 23\nPercentage of coneys: 31.52 %\nPercentage of rats: 43.48 %\nPercentage of frogs: 25.00 %","constraint":"1 ≤ N ≤ 100","solution":"循环读入+分类累加。用三个变量分别累加C、R、F的数量。最后计算总数和各占比。Python中可用collections.Counter简化统计。","technique":"Python的Counter可以一行完成分类统计。但手写累加理解计数模式更重要。输出百分比注意浮点转double和格式化。","cpp":"#include <cstdio>\n#include <iostream>\nusing namespace std;\nint main() {\n    int n, c = 0, r = 0, f = 0;\n    cin >> n;\n    for (int i = 0; i < n; i++) {\n        int k; char t;\n        cin >> k >> t;\n        if (t == 'C') c += k;\n        else if (t == 'R') r += k;\n        else f += k;\n    }\n    int s = c + r + f;\n    printf(\"Total: %d animals\\n\", s);\n    printf(\"Total coneys: %d\\n\", c);\n    printf(\"Total rats: %d\\n\", r);\n    printf(\"Total frogs: %d\\n\", f);\n    printf(\"Percentage of coneys: %.2lf %%\\n\", 100.0 * c / s);\n    printf(\"Percentage of rats: %.2lf %%\\n\", 100.0 * r / s);\n    printf(\"Percentage of frogs: %.2lf %%\\n\", 100.0 * f / s);\n    return 0;\n}","py":"n = int(input())\nc = r = f = 0\nfor _ in range(n):\n    k, t = input().split()\n    k = int(k)\n    if t == 'C': c += k\n    elif t == 'R': r += k\n    else: f += k\ns = c + r + f\nprint(f\"Total: {s} animals\")\nfor name, cnt in [('coneys',c),('rats',r),('frogs',f)]:\n    print(f\"Total {name}: {cnt}\")\nfor name, cnt in [('coneys',c),('rats',r),('frogs',f)]:\n    print(f\"Percentage of {name}: {cnt/s*100:.2f} %\")","gen":"experiment"},
    {"nq":"NQ041","acw":715,"title":"余数","desc":"给定一个整数N。对于1到10000中的每个整数，如果它除以N的余数为2，则输出这个数。","input_fmt":"一个整数N。","output_fmt":"每个满足条件的数一行。","sample_in":"13","sample_out":"2\n15\n28\n41\n...","constraint":"1 ≤ N ≤ 10000","solution":"从1到10000遍历，用i%N==2判断。这是模运算在循环中的基本应用。","technique":"Python可以用列表推导：print(*(i for i in range(1,10001) if i%N==2), sep='\\n')。但逐行输出更清晰。","cpp":"#include <iostream>\nusing namespace std;\nint main() {\n    int n;\n    cin >> n;\n    for (int i = 1; i <= 10000; i++)\n        if (i % n == 2) cout << i << endl;\n    return 0;\n}","py":"n = int(input())\nfor i in range(1, 10001):\n    if i % n == 2:\n        print(i)","gen":"remainder"},
    {"nq":"NQ042","acw":713,"title":"区间2","desc":"小鲁在统计区间内的数据。给定N和N个整数，统计落在[10,20]区间内和区间外的数的个数。","input_fmt":"第一行N。接下来N行，每行一个整数。","output_fmt":"\"X in\"换行\"Y out\"。","sample_in":"4\n14\n123\n10\n-25","sample_out":"2 in\n2 out","constraint":"1 ≤ N ≤ 10000","solution":"循环+分类计数。读入每个数，判断是否在10到20之间（含边界），分别累加。","technique":"Python可以用sum()+生成器一行统计：sum(1 for _ in range(n) if 10<=int(input())<=20)。C++中注意用<=包含边界。","cpp":"#include <iostream>\nusing namespace std;\nint main() {\n    int n, x, in = 0, out = 0;\n    cin >> n;\n    for (int i = 0; i < n; i++) {\n        cin >> x;\n        if (x >= 10 && x <= 20) in++;\n        else out++;\n    }\n    cout << in << \" in\" << endl;\n    cout << out << \" out\" << endl;\n    return 0;\n}","py":"n = int(input())\nin_cnt = sum(1 for _ in range(n) if 10 <= int(input()) <= 20)\nprint(f\"{in_cnt} in\")\nprint(f\"{n - in_cnt} out\")","gen":"interval_count"},
]

# ============================================================
def make_gen_cpp(p):
    lines=['#include <iostream>\n#include <cstdlib>\n#include <ctime>\nusing namespace std;\nint main(int argc,char*argv[]){\n    int tc=argc>1?atoi(argv[1]):1;\n    srand(time(0)+tc*1000);\n    switch(tc){']
    g=p['gen']
    if g=='even': # no input
        for i in range(1,11): lines.append(f'        case {i}: break;')
    elif g=='odd':
        for i in range(1,11):
            if i<=2: lines.append(f'        case {i}: cout<<"8"<<endl; break;')
            elif i<=4: lines.append(f'        case {i}: cout<<"1"<<endl; break;')
            elif i<=7: lines.append(f'        case {i}: cout<<rand()%100+1<<endl; break;')
            else: lines.append(f'        case {i}: cout<<rand()%1000+900<<endl; break;')
    elif g=='positive':
        for i in range(1,11):
            if i<=2: lines.append(f'        case {i}: cout<<"7\\n-5\\n6\\n-3.4\\n4.6\\n12"<<endl; break;')
            elif i<=4: lines.append(f'        case {i}: cout<<"-1\\n-2\\n-3\\n-4\\n-5\\n-6"<<endl; break;')
            elif i<=7: lines.append(f'        case {i}: printf("%.1f\\n%.1f\\n%.1f\\n%.1f\\n%.1f\\n%.1f\\n",(rand()%200-100)*1.0,(rand()%200-100)*1.0,(rand()%200-100)*1.0,(rand()%200-100)*1.0,(rand()%200-100)*1.0,(rand()%200-100)*1.0); break;')
            else: lines.append(f'        case {i}: cout<<"0.1\\n0.2\\n0.3\\n0.4\\n0.5\\n0.6"<<endl; break;')
    elif g=='odd_sum':
        for i in range(1,11):
            if i<=2: lines.append(f'        case {i}: cout<<"6 -5"<<endl; break;')
            elif i<=4: lines.append(f'        case {i}: cout<<"-3 3"<<endl; break;')
            elif i<=7: lines.append(f'        case {i}: printf("%d %d\\n",rand()%50-25,rand()%50-25); break;')
            else: lines.append(f'        case {i}: printf("%d %d\\n",rand()%5000-2500,rand()%5000-2500); break;')
    elif g=='max_pos':
        for i in range(1,11):
            if i<=2: lines.append(f'        case {i}: cout<<"5\\n3 2 5 1 4"<<endl; break;')
            elif i<=4: lines.append(f'        case {i}: cout<<"3\\n1 1 1"<<endl; break;')
            elif i<=7: lines.append(f'        case {i}: printf("%d\\n",rand()%10+1); for(int j=0;j<5;j++)printf("%d ",rand()%100);	printf("\\n"); break;')
            else: lines.append(f'        case {i}: printf("%d\\n",rand()%100+1); for(int j=0;j<20;j++)printf("%d ",rand()%1000); printf("\\n"); break;')
    elif g=='increasing':
        for i in range(1,11):
            if i<=2: lines.append(f'        case {i}: cout<<"5\\n10\\n3\\n0"<<endl; break;')
            elif i<=5: lines.append(f'        case {i}: cout<<rand()%10+1<<"\\n0"<<endl; break;')
            else: lines.append(f'        case {i}: cout<<rand()%50+1<<"\\n"<<rand()%50+1<<"\\n0"<<endl; break;')
    elif g=='consec_sum':
        for i in range(1,11):
            if i<=2: lines.append(f'        case {i}: cout<<"3\\n-5 0 -3 4 -1"<<endl; break;')
            elif i<=4: lines.append(f'        case {i}: cout<<"1\\n1"<<endl; break;')
            elif i<=7: lines.append(f'        case {i}: printf("%d\\n%d\\n",rand()%100+1,rand()%100+1); break;')
            else: lines.append(f'        case {i}: printf("%d\\n-1 0 -2 %d\\n",rand()%10000+1,rand()%10000+1); break;')
    elif g=='divisor':
        for i in range(1,11):
            if i<=2: lines.append(f'        case {i}: cout<<"6"<<endl; break;')
            elif i<=4: lines.append(f'        case {i}: cout<<"1"<<endl; break;')
            elif i<=7: lines.append(f'        case {i}: cout<<rand()%1000+1<<endl; break;')
            else: lines.append(f'        case {i}: cout<<rand()%100000+1000<<endl; break;')
    elif g=='pum':
        for i in range(1,11):
            if i<=2: lines.append(f'        case {i}: cout<<"7 4"<<endl; break;')
            elif i<=5: lines.append(f'        case {i}: printf("%d %d\\n",rand()%10+1,rand()%10+1); break;')
            else: lines.append(f'        case {i}: printf("%d %d\\n",rand()%20+1,rand()%20+1); break;')
    elif g=='six_odds':
        for i in range(1,11):
            if i<=2: lines.append(f'        case {i}: cout<<"8"<<endl; break;')
            elif i<=4: lines.append(f'        case {i}: cout<<"0"<<endl; break;')
            elif i<=7: lines.append(f'        case {i}: cout<<rand()%100<<endl; break;')
            else: lines.append(f'        case {i}: cout<<rand()%1000000+100<<endl; break;')
    elif g=='mult_table':
        for i in range(1,11):
            if i<=2: lines.append(f'        case {i}: cout<<"140"<<endl; break;')
            elif i<=4: lines.append(f'        case {i}: cout<<"1"<<endl; break;')
            elif i<=7: lines.append(f'        case {i}: cout<<rand()%100+1<<endl; break;')
            else: lines.append(f'        case {i}: cout<<rand()%1000+900<<endl; break;')
    elif g=='experiment':
        for i in range(1,11):
            if i<=2: lines.append(f'        case {i}: cout<<"10\\n10 C\\n6 R\\n15 F\\n5 C\\n14 R\\n9 C\\n6 R\\n8 F\\n5 C\\n14 R"<<endl; break;')
            elif i<=5:
                lines.append(f'        case {i}: cout<<rand()%20+1; for(int j=0;j<3;j++){{char t="CRF"[rand()%3]; printf("\\n%d %c",rand()%20+1,t);}} printf("\\n"); break;')
            else:
                lines.append(f'        case {i}: cout<<rand()%50+10; for(int j=0;j<10;j++){{char t="CRF"[rand()%3]; printf("\\n%d %c",rand()%20+1,t);}} printf("\\n"); break;')
    elif g=='remainder':
        for i in range(1,11):
            if i<=2: lines.append(f'        case {i}: cout<<"13"<<endl; break;')
            elif i<=4: lines.append(f'        case {i}: cout<<"2"<<endl; break;')
            elif i<=7: lines.append(f'        case {i}: cout<<rand()%100+1<<endl; break;')
            else: lines.append(f'        case {i}: cout<<rand()%10000+1<<endl; break;')
    elif g=='interval_count':
        for i in range(1,11):
            if i<=2: lines.append(f'        case {i}: cout<<"4\\n14\\n123\\n10\\n-25"<<endl; break;')
            elif i<=4: lines.append(f'        case {i}: cout<<"3\\n10\\n20\\n-1"<<endl; break;')
            elif i<=7:
                lines.append(f'        case {i}: cout<<rand()%20+5; for(int j=0;j<5;j++)printf("\\n%d",rand()%200-50); printf("\\n"); break;')
            else:
                lines.append(f'        case {i}: cout<<rand()%100+10; for(int j=0;j<20;j++)printf("\\n%d",rand()%200-50); printf("\\n"); break;')
    lines.extend(['    }','    return 0;','}'])
    return '\n'.join(lines)+'\n'

# ============================================================
def build_bank():
    BANK = BOOK_ROOT / "chapter3_bank"
    if BANK.exists(): shutil.rmtree(BANK)
    BANK.mkdir()
    for i, p in enumerate(PROBLEMS):
        pid = f"ACW{p['acw']:03d}"
        d = BANK / f"{pid}.{p['title'].replace(' ','_')}"
        d.mkdir()
        (d/"Andy.cpp").write_text(p['cpp']+'\n')
        (d/"Andy.py").write_text(p['py']+'\n')
        (d/"problem.json").write_text(json.dumps({
            "display_id":f"ACW{p['acw']}","title":p["title"],
            "description":{"format":"html","value":f"<p>{p['desc']}</p>"},
            "tags":["基础语法"],
            "input_description":{"format":"html","value":f"<p>{p['input_fmt']}</p>"},
            "output_description":{"format":"html","value":f"<p>{p['output_fmt']}</p>"},
            "test_case_score":[{"score":10,"input_name":f"{j}.in","output_name":f"{j}.out"}for j in range(1,11)],
            "hint":{"format":"html","value":f'<a href="https://www.acwing.com/problem/content/{p["acw"]}/" target="_blank">原题链接</a>'},
            "time_limit":1000,"memory_limit":256,
            "samples":[{"input":p["sample_in"],"output":p["sample_out"]}],
            "template":{},"spj":None,"rule_type":"OI",
            "source":f"AcWing {p['acw']} | {p['nq']} | 第3章",
            "allow_public_test_case_download":False,"answers":[],
        },indent=2,ensure_ascii=False))
        (d/"gen.cpp").write_text(make_gen_cpp(p))
        subprocess.run(['g++','-std=c++11','-O2',str(d/'gen.cpp'),'-o',str(d/'gen.out')],capture_output=True)
        subprocess.run(['g++','-std=c++11','-O2',str(d/'Andy.cpp'),'-o',str(d/'Andy.out')],capture_output=True)
        tc_dir=d/'testcase';tc_dir.mkdir()
        for tc in range(1,11):
            g=subprocess.run([str(d/'gen.out'),str(tc)],capture_output=True,text=True)
            (tc_dir/f'{tc}.in').write_text(g.stdout)
            a=subprocess.run([str(d/'Andy.out')],input=g.stdout,capture_output=True,text=True)
            (tc_dir/f'{tc}.out').write_text(a.stdout)
        tmp=d/'1';(tmp/'testcase').mkdir(parents=True)
        shutil.copy(d/'problem.json',tmp/'problem.json')
        for tc in range(1,11):shutil.copy(tc_dir/f'{tc}.in',tmp/'testcase'/f'{tc}.in');shutil.copy(tc_dir/f'{tc}.out',tmp/'testcase'/f'{tc}.out')
        with zipfile.ZipFile(d/'xmuoj-import.zip','w',zipfile.ZIP_DEFLATED)as zf:
            for root,dirs,files in os.walk(str(tmp)):
                for fn in files:fp=os.path.join(root,fn);zf.write(fp,os.path.relpath(fp,str(d)))
        shutil.rmtree(tmp)
        for f in['gen.out','Andy.out']:(d/f).unlink(missing_ok=True)
        print(f'  [{i+1:2d}/14] {pid} {p["title"]} ✅')
    print(f'\n✅ Chapter 3 bank: {BANK}')
    return BANK

# ============================================================
from pygments import highlight
from pygments.lexers import CppLexer,PythonLexer
from pygments.formatters import HtmlFormatter
from pygments.token import Token
CPP_FMT=HtmlFormatter(style='vs',noclasses=True)
PY_FMT=HtmlFormatter(style='vs',noclasses=True)
def hl(code,lexer,fmt):
    h=highlight(code,lexer,fmt);m=re.search(r'<pre[^>]*>(.*)</pre>',h,re.DOTALL)
    return re.sub(r'<span></span>\n?','',m.group(1)) if m else code
def hcpp(c):return hl(c,CppLexer(),CPP_FMT)
def hpy(c):return hl(c,PythonLexer(),PY_FMT)

CSS=r"""@page{size:A4;margin:2.2cm 2cm 2.2cm 2cm;@top-center{content:string(chapter);font-size:7.5pt;color:#999;font-family:"PingFang SC",sans-serif}@bottom-center{content:counter(page);font-size:7.5pt;color:#999}}
body{font-family:"PingFang SC","Hiragino Sans GB","Noto Serif CJK SC","STSong",serif;font-size:9.5pt;line-height:1.7;color:#222;string-set:chapter "第3章 循环的魔力 —— for/while与嵌套循环"}
.chapter-title{text-align:center;font-size:20pt;font-weight:bold;margin:1.5em 0 .1em 0;letter-spacing:3pt}
.chapter-subtitle{text-align:center;font-size:10pt;color:#777;margin-bottom:1.5em;padding-bottom:.8em;border-bottom:1px solid #bbb}
.preface{font-size:10pt;margin-bottom:2em;color:#444}.preface p{margin:.4em 0;text-indent:2em}
.problem-title{font-size:12pt;font-weight:bold;margin:1.5em 0 .4em 0;padding-bottom:.15em;border-bottom:1pt solid #444}
.problem-title .nq{color:#2563eb;margin-right:.6em;font-size:11pt}
.problem-title .acw{font-size:7.5pt;color:#aaa;font-weight:normal;margin-left:1em}
.problem-desc{margin:.6em 0 1em 0;text-indent:2em;line-height:1.85}
.spec-table{width:100%;border-collapse:collapse;margin:.3em 0 .5em 0;font-size:9pt}
.spec-table td{padding:.3em .8em;vertical-align:top;border:none}
.spec-table .spec-label{width:4em;font-size:8pt;font-weight:bold;text-align:right;padding-right:1em;white-space:nowrap}
.spec-table .spec-label .tag{display:inline-block;padding:.15em .5em;border-radius:2px;color:#fff;font-size:7.5pt;letter-spacing:.5pt}
.spec-table .spec-label .tag.in{background:#2563eb}.spec-table .spec-label .tag.out{background:#059669}.spec-table .spec-label .tag.lim{background:#d97706}
.spec-table .spec-value{color:#333;font-size:9pt}
.sample-box{background:#f7f8fa;border:.5pt solid #dde;border-radius:4px;padding:.7em 1em;margin:1em 0 1.2em 0}
.sample-grid{display:flex;gap:2em}.sample-col{flex:1}
.sample-col .col-label{font-size:7.5pt;color:#888;margin-bottom:.2em;font-weight:bold}
.sample-col pre{background:none;border:none;padding:.3em 0;margin:0;font-family:"SF Mono","Menlo","Consolas",monospace;font-size:9pt;line-height:1.4;white-space:pre-wrap;color:#333}
.insight-block{margin:.8em 0;padding:.5em .8em;border-left:3px solid #2563eb;background:#f8faff}
.insight-block .insight-label{font-size:8pt;font-weight:bold;color:#2563eb;margin-right:.5em}
.code-dual{display:flex;gap:1.5em;margin:1.2em 0;page-break-inside:avoid}.code-col{flex:1;min-width:0}
.code-col .lang-badge{display:inline-block;font-size:7.5pt;font-weight:bold;color:#fff;background:#2563eb;padding:.2em .7em;border-radius:3px;margin-bottom:.4em}
.code-col pre{background:#f8f8f0;border:.5pt solid #e0e0e0;border-radius:4px;padding:.7em .9em;font-family:"SF Mono","Menlo","Consolas","Courier New",monospace;font-size:7.5pt;line-height:1.45;overflow-x:auto;margin:0;white-space:pre-wrap;word-break:break-all}
.section-divider{border:none;border-top:.3pt solid #e0e0e0;margin:1em 0 0 0}.chapter-end{text-align:center;margin-top:3em;font-size:8pt;color:#999}"""

def build_html():
    parts=[]
    for p in PROBLEMS:
        pb=['<div class="problem-block">']
        pb.append(f'<div class="problem-title"><span class="nq">{p["nq"]}</span>{p["title"]}<span class="acw">AcWing {p["acw"]}</span></div>')
        pb.append(f'<div class="problem-desc">{p["desc"]}</div>')
        pb.append('<table class="spec-table">')
        pb.append(f'<tr><td class="spec-label"><span class="tag in">输入</span></td><td class="spec-value">{p["input_fmt"]}</td></tr>')
        pb.append(f'<tr><td class="spec-label"><span class="tag out">输出</span></td><td class="spec-value">{p["output_fmt"]}</td></tr>')
        pb.append(f'<tr><td class="spec-label"><span class="tag lim">范围</span></td><td class="spec-value">{p["constraint"]}</td></tr>')
        pb.append('</table>')
        pb.append('<div class="sample-box"><div class="sample-grid">')
        pb.append(f'<div class="sample-col"><div class="col-label">输入</div><pre>{p["sample_in"]}</pre></div>')
        pb.append(f'<div class="sample-col"><div class="col-label">输出</div><pre>{p["sample_out"]}</pre></div>')
        pb.append('</div></div>')
        pb.append(f'<div class="insight-block"><span class="insight-label">思路</span><span>{p["solution"]}</span></div>')
        pb.append(f'<div class="insight-block"><span class="insight-label">技巧</span><span>{p["technique"]}</span></div>')
        pb.append('<div class="code-dual">')
        pb.append(f'<div class="code-col"><div class="lang-badge">C++</div><pre>{hcpp(p["cpp"])}</pre></div>')
        pb.append(f'<div class="code-col"><div class="lang-badge">Python</div><pre>{hpy(p["py"])}</pre></div>')
        pb.append('</div></div><hr class="section-divider">')
        parts.append('\n'.join(pb))
    html=f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><title>第3章 循环的魔力</title><style>{CSS}</style></head><body>
<div class="chapter-title">循环的魔力</div><div class="chapter-subtitle">for/while与嵌套循环 · 14题 · C++ &amp; Python 双语对照</div>
<div class="preface"><p>本章进入编程最强大的控制结构——循环。14道题目从步进循环开始，逐步掌握条件计数、最值查找、while不定循环、嵌套循环格式控制和分类统计。你将学会用Python的range()、sum()+生成器、列表推导，以及C++的for/while来高效处理重复性计算。</p></div>
{chr(10).join(parts)}<div class="chapter-end">— 第3章完 · 共14题 —</div></body></html>"""
    (BOOK_ROOT/"textbook"/"chapter03_print.html").write_text(html,encoding="utf-8")

def build_docx():
    from docx import Document;from docx.shared import Pt,Cm,RGBColor;from docx.enum.text import WD_ALIGN_PARAGRAPH;from docx.enum.table import WD_TABLE_ALIGNMENT;from docx.oxml.ns import qn,nsdecls;from docx.oxml import parse_xml
    doc=Document();s=doc.sections[0];s.page_width=Cm(21);s.page_height=Cm(29.7)
    s.top_margin=Cm(2.2);s.bottom_margin=Cm(2.2);s.left_margin=Cm(2);s.right_margin=Cm(2)
    st=doc.styles['Normal'];st.font.name='等线';st.font.size=Pt(9.5);st.paragraph_format.line_spacing=1.35;st.paragraph_format.space_after=Pt(3);st.element.rPr.rFonts.set(qn('w:eastAsia'),'等线')
    BL=RGBColor(0x25,0x63,0xEB);GR=RGBColor(0x05,0x96,0x69);OR=RGBColor(0xD9,0x77,0x06);GY=RGBColor(0x66,0x66,0x66);LG=RGBColor(0x99,0x99,0x99)
    def acr(para,text,color=None,bold=False,italic=False,fs=Pt(7.5)):
        r=para.add_run(text);r.font.name='Courier New';r.font.size=fs
        if color:r.font.color.rgb=color
        if bold:r.font.bold=True
        if italic:r.font.italic=True;return r
    tp=doc.add_paragraph();tp.alignment=WD_ALIGN_PARAGRAPH.CENTER;tr=tp.add_run('循环的魔力');tr.font.size=Pt(20);tr.font.bold=True
    sp=doc.add_paragraph();sp.alignment=WD_ALIGN_PARAGRAPH.CENTER;sr=sp.add_run('for/while与嵌套循环 · 14题 · C++ & Python 双语对照');sr.font.size=Pt(10);sr.font.color.rgb=GY
    for p in PROBLEMS:
        tp=doc.add_paragraph();tp.paragraph_format.space_before=Pt(14)
        nq=tp.add_run(f'{p["nq"]} ');nq.font.size=Pt(12);nq.font.bold=True;nq.font.color.rgb=BL
        tt=tp.add_run(p['title']);tt.font.size=Pt(12);tt.font.bold=True
        aw=tp.add_run(f'  AcWing {p["acw"]}');aw.font.size=Pt(7.5);aw.font.color.rgb=LG
        pPr=tp._p.get_or_add_pPr();pBdr=parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="6" w:space="1" w:color="444444"/></w:pBdr>');pPr.append(pBdr)
        dp=doc.add_paragraph(p['desc']);dp.paragraph_format.first_line_indent=Cm(0.7)
        st2=doc.add_table(rows=3,cols=2);st2.autofit=True
        for i,(label,value,color) in enumerate([('输入',p['input_fmt'],BL),('输出',p['output_fmt'],GR),('范围',p['constraint'],OR)]):
            cl=st2.cell(i,0);cl.width=Cm(1.5);cl.paragraphs[0].alignment=WD_ALIGN_PARAGRAPH.LEFT
            trun=cl.paragraphs[0].add_run(f' {label} ');trun.font.size=Pt(7.5);trun.font.bold=True;trun.font.color.rgb=RGBColor(0xFF,0xFF,0xFF)
            shd=parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color}" w:val="clear"/>');trun._r.get_or_add_rPr().append(shd)
            cv=st2.cell(i,1);cv.width=Cm(14);vr=cv.paragraphs[0].add_run(value);vr.font.size=Pt(9)
        st3=doc.add_table(rows=1,cols=2);st3.autofit=True
        for col,(label,text) in enumerate([('输入',p['sample_in']),('输出',p['sample_out'])]):
            c=st3.cell(0,col);c.width=Cm(7.5);tcPr=c._tc.get_or_add_tcPr();shd=parse_xml(f'<w:shd {nsdecls("w")} w:fill="F7F8FA" w:val="clear"/>');tcPr.append(shd)
            lr=c.paragraphs[0].add_run(label);lr.font.size=Pt(7.5);lr.font.bold=True;lr.font.color.rgb=LG
            vp=c.add_paragraph();vr=vp.add_run(text);vr.font.name='Courier New';vr.font.size=Pt(9)
        for lbl,txt in [('思路',p['solution']),('技巧',p['technique'])]:
            ip=doc.add_paragraph();ip.paragraph_format.space_after=Pt(4);ip.paragraph_format.space_before=Pt(4)
            pPr=ip._p.get_or_add_pPr();shd=parse_xml(f'<w:shd {nsdecls("w")} w:fill="F8FAFF" w:val="clear"/>');pPr.append(shd)
            lr=ip.add_run(f'{lbl} ');lr.font.size=Pt(8);lr.font.bold=True;lr.font.color.rgb=BL;ip.add_run(txt).font.size=Pt(9)
        ct=doc.add_table(rows=1,cols=2);ct.autofit=False;ct.alignment=WD_TABLE_ALIGNMENT.CENTER
        for col,(lang,code,lexer) in enumerate([('C++',p['cpp'],CppLexer()),('Python',p['py'],PythonLexer())]):
            c=ct.cell(0,col);c.width=Cm(7.5);c.paragraphs[0].clear()
            bp2=c.paragraphs[0];bp2.paragraph_format.left_indent=Cm(0.1)
            br=bp2.add_run(f' {lang} ');br.font.size=Pt(7);br.font.bold=True;br.font.color.rgb=RGBColor(0xFF,0xFF,0xFF)
            shd=parse_xml(f'<w:shd {nsdecls("w")} w:fill="2563EB" w:val="clear"/>');br._r.get_or_add_rPr().append(shd)
            for line in code.split('\n'):
                cp2=c.add_paragraph();cp2.paragraph_format.left_indent=Cm(0.1);cp2.paragraph_format.space_before=Pt(0);cp2.paragraph_format.space_after=Pt(0);cp2.paragraph_format.line_spacing=1.1
                pPr=cp2._p.get_or_add_pPr();shd=parse_xml(f'<w:shd {nsdecls("w")} w:fill="F0F0F0" w:val="clear"/>');pPr.append(shd)
                if not line.strip():acr(cp2,' ',fs=Pt(6));continue
                for ttype,ttext in lexer.get_tokens(line):
                    if not ttext:continue
                    cm={Token.Keyword:RGBColor(0,0,255),Token.Keyword.Type:RGBColor(0x2B,0x91,0xAF),Token.Name.Builtin:RGBColor(0,0,255),Token.String:RGBColor(0xA3,0x15,0x15),Token.Comment:RGBColor(0,0x80,0),Token.Comment.Preproc:RGBColor(0,0,255),Token.Number:RGBColor(0x09,0x80,0x85)}
                    cf=None;is_kw=ttype in Token.Keyword or ttype in Token.Keyword.Type;is_cm=ttype in Token.Comment or ttype in Token.Comment.Preproc
                    for tk,clr in cm.items():
                        if ttype in tk or tk in ttype:cf=clr;break
                    acr(cp2,ttext,cf,is_kw,is_cm)
        sep=doc.add_paragraph();sep.paragraph_format.space_before=Pt(8)
        pPr=sep._p.get_or_add_pPr();pBdr=parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="4" w:space="1" w:color="E0E0E0"/></w:pBdr>');pPr.append(pBdr)
    ep=doc.add_paragraph();ep.alignment=WD_ALIGN_PARAGRAPH.CENTER;ep.paragraph_format.space_before=Pt(24);er=ep.add_run('— 第3章完 · 共14题 —');er.font.size=Pt(8);er.font.color.rgb=LG
    doc.save(str(BOOK_ROOT/"textbook"/"chapter03.docx"))

# ============================================================
if __name__=="__main__":
    print("=== Step 1: Build Bank ===");build_bank()
    print("\n=== Step 2: Build HTML ===");build_html();print("✅ chapter03_print.html")
    print("\n=== Step 3: Build DOCX ===");build_docx();print("✅ chapter03.docx")
