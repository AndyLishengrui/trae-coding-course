#!/usr/bin/env python3
"""第4章：数组与线性存储（12题）"""
import json,re,os,sys,time,tempfile,zipfile,shutil,subprocess
from pathlib import Path
BOOK_ROOT=Path(__file__).parent.parent

PROBLEMS=[
    {"nq":"NQ043","acw":737,"title":"数组替换","desc":"小鲁学习了数组。给定一个长度为10的数组，将其中所有小于等于0的元素替换为1，然后输出整个数组。","input_fmt":"10行，每行一个整数。","output_fmt":"10行，每行\"X[i] = Y\"，i从0到9，Y为替换后的值。","sample_in":"0\n-5\n63\n-8\n0\n...","sample_out":"X[0] = 1\nX[1] = 1\nX[2] = 63\n...","constraint":"−10⁹ ≤ 值 ≤ 10⁹","solution":"遍历数组，如果元素≤0则替换为1。用下标循环或for-each+索引。C++用for(int i=0;i<10;i++)，Python用enumerate()同时获取索引和值。","technique":"Python的enumerate(arr)返回(index, value)元组。C++中arr[i]访问元素。数组索引从0开始。","cpp":"#include <iostream>\nusing namespace std;\nint main() {\n    int x;\n    for (int i = 0; i < 10; i++) {\n        cin >> x;\n        if (x <= 0) x = 1;\n        cout << \"X[\" << i << \"] = \" << x << endl;\n    }\n    return 0;\n}","py":"for i in range(10):\n    x = int(input())\n    if x <= 0: x = 1\n    print(f\"X[{i}] = {x}\")","gen":"arr_replace"},
    {"nq":"NQ044","acw":738,"title":"数组填充","desc":"给定一个整数V，构造一个长度为10的数组，第0个元素是V，此后每个元素是前一个的两倍。","input_fmt":"一个整数V。","output_fmt":"10行，每行\"N[i] = X\"。","sample_in":"1","sample_out":"N[0] = 1\nN[1] = 2\nN[2] = 4\n...","constraint":"−10⁴ ≤ V ≤ 10⁴","solution":"递推生成数组：arr[0]=V, arr[i]=arr[i-1]*2。Python用列表推导或循环。C++用vector或直接输出。","technique":"Python的列表推导：[v*(2**i) for i in range(10)]直接用位移运算。C++中1<<i等价于2^i。","cpp":"#include <iostream>\nusing namespace std;\nint main() {\n    int v;\n    cin >> v;\n    for (int i = 0; i < 10; i++, v *= 2)\n        cout << \"N[\" << i << \"] = \" << v << endl;\n    return 0;\n}","py":"v = int(input())\nfor i in range(10):\n    print(f\"N[{i}] = {v}\")\n    v *= 2","gen":"arr_fill"},
    {"nq":"NQ045","acw":739,"title":"数组选择","desc":"读取100个浮点数。对于每个小于等于10的数，按格式输出它在数组中的位置和值。","input_fmt":"100行（或一行多个），每行一个浮点数。","output_fmt":"对每个≤10的数，输出\"A[i] = X\"（保留1位小数）。","sample_in":"0\n-5\n63\n...","sample_out":"A[0] = 0.0\nA[1] = -5.0\n...","constraint":"−10⁶ ≤ 值 ≤ 10⁶","solution":"遍历100次读入，条件判断≤10则输出。Python无需存储全部数据，边读边输出即可，节省内存。C++同样。","technique":"流式处理：不需要把100个数都存下来，读一个判断一个输出一个。这种思维在处理大数据时很重要。","cpp":"#include <cstdio>\nint main() {\n    for (int i = 0; i < 100; i++) {\n        double x;\n        scanf(\"%lf\", &x);\n        if (x <= 10) printf(\"A[%d] = %.1f\\n\", i, x);\n    }\n    return 0;\n}","py":"for i in range(100):\n    x = float(input())\n    if x <= 10:\n        print(f\"A[{i}] = {x:.1f}\")","gen":"arr_select"},
    {"nq":"NQ046","acw":743,"title":"数组中的行","desc":"给定一个12×12的二维数组。读取行号L和操作类型T（'S'求和或'M'求平均），计算第L行所有元素的和或平均值。","input_fmt":"第一行L(0-11)。第二行T('S'或'M')。接下来144个浮点数（12×12矩阵）。","output_fmt":"结果保留1位小数。","sample_in":"2\nS\n(144个浮点数...)","sample_out":"(第2行之和,1位小数)","constraint":"矩阵元素−10⁶到10⁶","solution":"双层循环遍历矩阵，遇到目标行L时累加。如果是'M'求平均则除以12。","technique":"二维数组读入：外层for i in range(12)，内层for j in range(12)。Python用嵌套列表推导生成矩阵。","cpp":"#include <cstdio>\nint main() {\n    int l; char t;\n    scanf(\"%d %c\", &l, &t);\n    double sum = 0, x;\n    for (int i = 0; i < 12; i++)\n        for (int j = 0; j < 12; j++) {\n            scanf(\"%lf\", &x);\n            if (i == l) sum += x;\n        }\n    printf(\"%.1lf\\n\", t == 'S' ? sum : sum / 12);\n    return 0;\n}","py":"l = int(input())\nt = input().strip()\nsum_val = 0\nfor i in range(12):\n    for j in range(12):\n        x = float(input())\n        if i == l: sum_val += x\nprint(f\"{sum_val if t == 'S' else sum_val / 12:.1f}\")","gen":"array_row"},
    {"nq":"NQ047","acw":740,"title":"数组变换","desc":"给定一个20个整数的数组。将数组前后对称位置互换（第0个和第19个交换，第1个和第18个交换...），输出变换后的数组。","input_fmt":"20个整数。","output_fmt":"20行，每行\"N[i] = X\"。","sample_in":"0\n1\n2\n...\n19","sample_out":"N[0] = 19\nN[1] = 18\n...","constraint":"−10⁹ ≤ 值 ≤ 10⁹","solution":"对称交换：arr[i] ↔ arr[19-i]，只需循环10次（i从0到9）。Python用切片arr[::-1]一行翻转。","technique":"Python的arr[::-1]是最简洁的数组翻转方式。C++用reverse()或手写交换。","cpp":"#include <iostream>\nusing namespace std;\nint main() {\n    int arr[20];\n    for (int i = 0; i < 20; i++) cin >> arr[i];\n    for (int i = 0; i < 10; i++) swap(arr[i], arr[19 - i]);\n    for (int i = 0; i < 20; i++)\n        cout << \"N[\" << i << \"] = \" << arr[i] << endl;\n    return 0;\n}","py":"arr = [int(input()) for _ in range(20)]\narr.reverse()\nfor i, v in enumerate(arr):\n    print(f\"N[{i}] = {v}\")","gen":"arr_reverse"},
    {"nq":"NQ048","acw":741,"title":"斐波那契数列","desc":"小鲁在学数列。斐波那契数列的前两项是0和1，之后每一项都是前两项之和。给定N，输出前N项。","input_fmt":"一个整数N（1≤N≤60）。","output_fmt":"一行，空格隔开的N个整数。","sample_in":"5","sample_out":"0 1 1 2 3","constraint":"1 ≤ N ≤ 60（结果可能超过32位int范围！）","solution":"递推：a=0, b=1; for i in range(N): print(a); a,b = b, a+b。注意用long long（C++）避免溢出，Python自动大整数。","technique":"Python的a,b=b,a+b是递推的标准写法。C++注意用long long（64位），N=60时结果约1.5×10¹²超出32位int。这是DP思想的萌芽——用前面算出的结果推导后面。","cpp":"#include <iostream>\nusing namespace std;\nint main() {\n    int n;\n    cin >> n;\n    long long a = 0, b = 1;\n    for (int i = 0; i < n; i++) {\n        if (i) cout << \" \";\n        cout << a;\n        long long t = a + b; a = b; b = t;\n    }\n    cout << endl;\n    return 0;\n}","py":"n = int(input())\na, b = 0, 1\nresult = []\nfor _ in range(n):\n    result.append(str(a))\n    a, b = b, a + b\nprint(' '.join(result))","gen":"fib"},
    {"nq":"NQ049","acw":742,"title":"最小数和它的位置","desc":"给定N和一个包含N个整数的数组，找出数组中的最小值及其位置（如果有多个最小值，输出第一个的位置）。","input_fmt":"第一行N。第二行N个整数。","output_fmt":"第一行\"Menor valor: X\"。第二行\"Posicao: Y\"（位置从0开始）。","sample_in":"10\n1 2 3 4 -5 6 7 8 9 10","sample_out":"Menor valor: -5\nPosicao: 4","constraint":"1 ≤ N ≤ 1000","solution":"遍历数组维护最小值和位置。Python用min(arr)和arr.index(min_val)一行搞定，但手写循环理解查找逻辑。","technique":"Python的enumerate()同时获得索引和值。min(arr)找最小值，arr.index(v)找位置。","cpp":"#include <iostream>\nusing namespace std;\nint main() {\n    int n, x, mn, pos = 0;\n    cin >> n;\n    for (int i = 0; i < n; i++) {\n        cin >> x;\n        if (i == 0 || x < mn) { mn = x; pos = i; }\n    }\n    cout << \"Menor valor: \" << mn << endl;\n    cout << \"Posicao: \" << pos << endl;\n    return 0;\n}","py":"n = int(input())\narr = list(map(int, input().split()))\nmn = min(arr)\nprint(f\"Menor valor: {mn}\")\nprint(f\"Posicao: {arr.index(mn)}\")","gen":"min_pos_n"},
    {"nq":"NQ050","acw":744,"title":"数组中的列","desc":"与NQ046类似，但这次操作的是列。给定列号C和操作类型T，计算12×12矩阵第C列的和或平均值。","input_fmt":"第一行列号C。第二行操作类型T。接下来144个浮点数。","output_fmt":"结果保留1位小数。","sample_in":"2\nS\n(144个浮点数...)","sample_out":"(第2列之和,1位小数)","constraint":"同NQ046","solution":"与行操作对称：当内层循环到目标列j==C时累加。其他逻辑相同。","technique":"行操作和列操作的双重循环结构完全相同，只在判断条件上差一个字母（i==L vs j==C）。注意对比理解。","cpp":"#include <cstdio>\nint main() {\n    int c; char t;\n    scanf(\"%d %c\", &c, &t);\n    double sum = 0, x;\n    for (int i = 0; i < 12; i++)\n        for (int j = 0; j < 12; j++) {\n            scanf(\"%lf\", &x);\n            if (j == c) sum += x;\n        }\n    printf(\"%.1lf\\n\", t == 'S' ? sum : sum / 12);\n    return 0;\n}","py":"c = int(input())\nt = input().strip()\nsum_val = 0\nfor i in range(12):\n    for j in range(12):\n        x = float(input())\n        if j == c: sum_val += x\nprint(f\"{sum_val if t == 'S' else sum_val / 12:.1f}\")","gen":"array_col"},
    {"nq":"NQ051","acw":717,"title":"简单斐波那契","desc":"计算斐波那契数列的第N项。N从0开始：F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)。","input_fmt":"一个整数N。","output_fmt":"第N项的值。","sample_in":"4","sample_out":"3","constraint":"1 ≤ N ≤ 60","solution":"与NQ048类似，但只输出第N项。递推直到第N项。注意N=0的情况。","technique":"Python的a,b=b,a+b在循环中递推。只输出最后一项，无需存储中间结果。","cpp":"#include <iostream>\nusing namespace std;\nint main() {\n    int n;\n    cin >> n;\n    long long a = 0, b = 1;\n    if (n == 0) { cout << 0 << endl; return 0; }\n    for (int i = 1; i < n; i++) {\n        long long t = a + b; a = b; b = t;\n    }\n    cout << b << endl;\n    return 0;\n}","py":"n = int(input())\na, b = 0, 1\nfor _ in range(n):\n    a, b = b, a + b\nprint(a)","gen":"fib_one"},
    {"nq":"NQ052","acw":722,"title":"数字序列和它的和","desc":"对于每一对输入的正整数M和N（M<N），输出从M到N的所有整数及它们的和。以读入的M或N≤0为结束标志。","input_fmt":"多行，每行两个整数M和N。以M≤0或N≤0结束。","output_fmt":"对每对M,N，输出一行所有整数（空格隔开）和\"Sum=X\"。","sample_in":"5 10\n2 3\n0 0","sample_out":"5 6 7 8 9 10 Sum=45\n2 3 Sum=5","constraint":"M,N ≤ 100","solution":"while循环读取，遇到非正数break。对每对M,N确保M≤N（必要时交换），然后for循环输出并累加。","technique":"Python的range(m,n+1)生成连续整数。用join(map(str,...))拼接输出整洁。注意先交换保证M≤N。","cpp":"#include <iostream>\nusing namespace std;\nint main() {\n    int m, n;\n    while (cin >> m >> n, m > 0 && n > 0) {\n        if (m > n) swap(m, n);\n        int sum = 0;\n        for (int i = m; i <= n; i++) {\n            cout << i << \" \";\n            sum += i;\n        }\n        cout << \"Sum=\" << sum << endl;\n    }\n    return 0;\n}","py":"while True:\n    m, n = map(int, input().split())\n    if m <= 0 or n <= 0: break\n    if m > n: m, n = n, m\n    nums = range(m, n + 1)\n    print(' '.join(map(str, nums)), f\"Sum={sum(nums)}\")","gen":"seq_sum"},
    {"nq":"NQ053","acw":725,"title":"完全数","desc":"一个数的所有真因子（不含自身）之和等于自身，称为完全数。给定N，输出不超过N的所有完全数。","input_fmt":"一个整数N。","output_fmt":"每行一个完全数。","sample_in":"30","sample_out":"6\n28","constraint":"1 ≤ N ≤ 10⁸","solution":"10⁸以内只有四个完全数：6, 28, 496, 8128。直接判断它们是否≤N即可。不需要枚举计算！这是数学知识在编程中的应用。","technique":"利用数学事实简化计算。C++可以预计算或直接判断。Python同样。","cpp":"#include <iostream>\nusing namespace std;\nint main() {\n    int n;\n    cin >> n;\n    int perfect[] = {6, 28, 496, 8128};\n    for (int x : perfect)\n        if (x <= n) cout << x << endl;\n    return 0;\n}","py":"n = int(input())\nfor x in [6, 28, 496, 8128]:\n    if x <= n:\n        print(x)","gen":"perfect"},
    {"nq":"NQ054","acw":726,"title":"质数","desc":"给定N，输出2到N之间所有的质数（素数）。质数指大于1且只有1和自身两个因子的数。","input_fmt":"一个整数N。","output_fmt":"每行一个质数。","sample_in":"10","sample_out":"2\n3\n5\n7","constraint":"2 ≤ N ≤ 10⁶","solution":"枚举2到N的每个数，判断是否为质数。优化：只需检查到√i。判断函数：for j in range(2, int(sqrt(i))+1): if i%j==0: break。","technique":"√n优化将复杂度从O(n²)降到O(n√n)。使用math.isqrt()（Python 3.8+）精确整数平方根。","cpp":"#include <iostream>\n#include <cmath>\nusing namespace std;\nint main() {\n    int n;\n    cin >> n;\n    for (int i = 2; i <= n; i++) {\n        bool prime = true;\n        for (int j = 2; j * j <= i; j++) {\n            if (i % j == 0) { prime = false; break; }\n        }\n        if (prime) cout << i << endl;\n    }\n    return 0;\n}","py":"import math\nn = int(input())\nfor i in range(2, n + 1):\n    prime = True\n    for j in range(2, int(math.sqrt(i)) + 1):\n        if i % j == 0:\n            prime = False\n            break\n    if prime:\n        print(i)","gen":"prime"},
]

def make_gen(p):
    lines=['#include <iostream>\n#include <cstdlib>\n#include <ctime>\nusing namespace std;\nint main(int argc,char*argv[]){\n    int tc=argc>1?atoi(argv[1]):1;\n    srand(time(0)+tc*1000);\n    switch(tc){']
    g=p['gen']
    if g=='arr_replace':
        for i in range(1,11):
            if i<=2:lines.append(f'        case {i}:cout<<"0\\n-5\\n63\\n-8\\n0\\n1\\n2\\n-100\\n50\\n200"<<endl;break;')
            elif i<=4:lines.append(f'        case {i}:cout<<"-1\\n-2\\n-3\\n-4\\n-5\\n-6\\n-7\\n-8\\n-9\\n-10"<<endl;break;')
            elif i<=7:lines.append(f'        case {i}:for(int j=0;j<10;j++)printf("%d\\n",rand()%100-50);break;')
            else:lines.append(f'        case {i}:for(int j=0;j<10;j++)printf("%d\\n",rand()%2000000-1000000);break;')
    elif g=='arr_fill':
        for i in range(1,11):
            if i<=2:lines.append(f'        case {i}:cout<<"1"<<endl;break;')
            elif i<=4:lines.append(f'        case {i}:cout<<"-1"<<endl;break;')
            elif i<=7:lines.append(f'        case {i}:cout<<rand()%100-50<<endl;break;')
            else:lines.append(f'        case {i}:cout<<rand()%10000-5000<<endl;break;')
    elif g=='arr_select':
        for i in range(1,11):
            if i<=2:lines.append(f'        case {i}:for(int j=0;j<100;j++)printf("%.1f\\n",(rand()%200-100)*1.0);break;')
            else:lines.append(f'        case {i}:for(int j=0;j<100;j++)printf("%.1f\\n",(rand()%2000-1000)*0.1);break;')
    elif g=='array_row':
        for i in range(1,11):
            t = 'S' if i%2 else 'M'
            if i<=4:lines.append(f'        case {i}:cout<<rand()%12<<"\\n{t}\\n";for(int j=0;j<144;j++)printf("%.1f\\n",(rand()%100)*1.0);break;')
            else:lines.append(f'        case {i}:printf("%d\\n%c\\n",rand()%12,\'{t}\');for(int j=0;j<144;j++)printf("%.1f\\n",(rand()%200-100)*1.0);break;')
    elif g=='arr_reverse':
        for i in range(1,11):
            if i<=2:lines.append(f'        case {i}:for(int j=0;j<20;j++)cout<<j<<endl;break;')
            elif i<=4:lines.append(f'        case {i}:for(int j=0;j<20;j++)cout<<rand()%10<<endl;break;')
            else:lines.append(f'        case {i}:for(int j=0;j<20;j++)cout<<rand()%1000-500<<endl;break;')
    elif g=='fib':
        for i in range(1,11):
            if i<=2:lines.append(f'        case {i}:cout<<"5"<<endl;break;')
            elif i<=4:lines.append(f'        case {i}:cout<<"1"<<endl;break;')
            elif i<=7:lines.append(f'        case {i}:cout<<rand()%30+1<<endl;break;')
            else:lines.append(f'        case {i}:cout<<rand()%30+30<<endl;break;')
    elif g=='min_pos_n':
        for i in range(1,11):
            if i<=2:lines.append(f'        case {i}:cout<<"10\\n1 2 3 4 -5 6 7 8 9 10"<<endl;break;')
            elif i<=4:lines.append(f'        case {i}:cout<<"3\\n100 100 100"<<endl;break;')
            elif i<=7:lines.append(f'        case {i}:printf("%d\\n",rand()%20+5);for(int j=0;j<10;j++)printf("%d ",rand()%100);printf("\\n");break;')
            else:lines.append(f'        case {i}:printf("%d\\n",rand()%500+10);for(int j=0;j<50;j++)printf("%d ",rand()%1000-500);printf("\\n");break;')
    elif g=='array_col':
        for i in range(1,11):
            t = 'S' if i%2 else 'M'
            if i<=4:lines.append(f'        case {i}:cout<<rand()%12<<"\\n{t}\\n";for(int j=0;j<144;j++)printf("%.1f\\n",(rand()%100)*1.0);break;')
            else:lines.append(f'        case {i}:printf("%d\\n%c\\n",rand()%12,\'{t}\');for(int j=0;j<144;j++)printf("%.1f\\n",(rand()%200-100)*1.0);break;')
    elif g=='fib_one':
        for i in range(1,11):
            if i<=2:lines.append(f'        case {i}:cout<<"4"<<endl;break;')
            elif i<=4:lines.append(f'        case {i}:cout<<"0"<<endl;break;')
            elif i<=7:lines.append(f'        case {i}:cout<<rand()%30+1<<endl;break;')
            else:lines.append(f'        case {i}:cout<<rand()%30+30<<endl;break;')
    elif g=='seq_sum':
        for i in range(1,11):
            if i<=2:lines.append(f'        case {i}:cout<<"5 10\\n2 3\\n0 0"<<endl;break;')
            elif i<=4:lines.append(f'        case {i}:cout<<"1 5\\n-1 -1"<<endl;break;')
            else:lines.append(f'        case {i}:printf("%d %d\\n%d %d\\n-1 -1\\n",rand()%50+1,rand()%50+1,rand()%50+1,rand()%50+1);break;')
    elif g=='perfect':
        for i in range(1,11):
            vals=['30','6','500','9000','1','100','1000','10000','100000000','10']
            lines.append(f'        case {i}:cout<<"{vals[i-1]}"<<endl;break;')
    elif g=='prime':
        for i in range(1,11):
            if i<=2:lines.append(f'        case {i}:cout<<"10"<<endl;break;')
            elif i<=4:lines.append(f'        case {i}:cout<<"2"<<endl;break;')
            elif i<=7:lines.append(f'        case {i}:cout<<rand()%50+10<<endl;break;')
            else:lines.append(f'        case {i}:cout<<rand()%1000+100<<endl;break;')
    lines.extend(['    }','    return 0;','}'])
    return '\n'.join(lines)+'\n'

def build_bank():
    BANK=BOOK_ROOT/"chapter4_bank"
    if BANK.exists():shutil.rmtree(BANK)
    BANK.mkdir()
    for i,p in enumerate(PROBLEMS):
        pid=f"ACW{p['acw']:03d}";d=BANK/f"{pid}.{p['title'].replace(' ','_')}";d.mkdir()
        (d/"Andy.cpp").write_text(p['cpp']+'\n');(d/"Andy.py").write_text(p['py']+'\n')
        (d/"problem.json").write_text(json.dumps({"display_id":f"ACW{p['acw']}","title":p["title"],"description":{"format":"html","value":f"<p>{p['desc']}</p>"},"tags":["基础语法"],"input_description":{"format":"html","value":f"<p>{p['input_fmt']}</p>"},"output_description":{"format":"html","value":f"<p>{p['output_fmt']}</p>"},"test_case_score":[{"score":10,"input_name":f"{j}.in","output_name":f"{j}.out"}for j in range(1,11)],"hint":{"format":"html","value":f'<a href="https://www.acwing.com/problem/content/{p["acw"]}/" target="_blank">原题链接</a>'},"time_limit":1000,"memory_limit":256,"samples":[{"input":p["sample_in"],"output":p["sample_out"]}],"template":{},"spj":None,"rule_type":"OI","source":f"AcWing {p['acw']} | {p['nq']} | 第4章","allow_public_test_case_download":False,"answers":[]},indent=2,ensure_ascii=False))
        (d/"gen.cpp").write_text(make_gen(p))
        subprocess.run(['g++','-std=c++11','-O2',str(d/'gen.cpp'),'-o',str(d/'gen.out')],capture_output=True)
        subprocess.run(['g++','-std=c++11','-O2',str(d/'Andy.cpp'),'-o',str(d/'Andy.out')],capture_output=True)
        tc_dir=d/'testcase';tc_dir.mkdir()
        for tc in range(1,11):
            g=subprocess.run([str(d/'gen.out'),str(tc)],capture_output=True,text=True);(tc_dir/f'{tc}.in').write_text(g.stdout)
            a=subprocess.run([str(d/'Andy.out')],input=g.stdout,capture_output=True,text=True);(tc_dir/f'{tc}.out').write_text(a.stdout)
        tmp=d/'1';(tmp/'testcase').mkdir(parents=True);shutil.copy(d/'problem.json',tmp/'problem.json')
        for tc in range(1,11):shutil.copy(tc_dir/f'{tc}.in',tmp/'testcase'/f'{tc}.in');shutil.copy(tc_dir/f'{tc}.out',tmp/'testcase'/f'{tc}.out')
        with zipfile.ZipFile(d/'xmuoj-import.zip','w',zipfile.ZIP_DEFLATED)as zf:
            for root,dirs,files in os.walk(str(tmp)):
                for fn in files:fp=os.path.join(root,fn);zf.write(fp,os.path.relpath(fp,str(d)))
        shutil.rmtree(tmp)
        for f in['gen.out','Andy.out']:(d/f).unlink(missing_ok=True)
        print(f'  [{i+1:2d}/12] {pid} {p["title"]} ✅')
    print(f'\n✅ Chapter 4 bank: {BANK}')

from pygments import highlight;from pygments.lexers import CppLexer,PythonLexer;from pygments.formatters import HtmlFormatter;from pygments.token import Token
CPP_FMT=HtmlFormatter(style='vs',noclasses=True);PY_FMT=HtmlFormatter(style='vs',noclasses=True)
def hl(code,lexer,fmt):
    h=highlight(code,lexer,fmt);m=re.search(r'<pre[^>]*>(.*)</pre>',h,re.DOTALL)
    return re.sub(r'<span></span>\n?','',m.group(1))if m else code
def hcpp(c):return hl(c,CppLexer(),CPP_FMT)
def hpy(c):return hl(c,PythonLexer(),PY_FMT)

CSS=r"""@page{size:A4;margin:2.2cm 2cm 2.2cm 2cm;@top-center{content:string(chapter);font-size:7.5pt;color:#999;font-family:"PingFang SC",sans-serif}@bottom-center{content:counter(page);font-size:7.5pt;color:#999}}
body{font-family:"PingFang SC","Hiragino Sans GB","Noto Serif CJK SC","STSong",serif;font-size:9.5pt;line-height:1.7;color:#222;string-set:chapter "第4章 数据的容器 —— 数组与线性存储"}
.chapter-title{text-align:center;font-size:20pt;font-weight:bold;margin:1.5em 0 .1em 0;letter-spacing:3pt}
.chapter-subtitle{text-align:center;font-size:10pt;color:#777;margin-bottom:1.5em;padding-bottom:.8em;border-bottom:1px solid #bbb}
.preface{font-size:10pt;margin-bottom:2em;color:#444}.preface p{margin:.4em 0;text-indent:2em}
.problem-title{font-size:12pt;font-weight:bold;margin:1.5em 0 .4em 0;padding-bottom:.15em;border-bottom:1pt solid #444}
.problem-title .nq{color:#2563eb;margin-right:.6em;font-size:11pt}.problem-title .acw{font-size:7.5pt;color:#aaa;font-weight:normal;margin-left:1em}
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
    html=f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><title>第4章 数据的容器</title><style>{CSS}</style></head><body>
<div class="chapter-title">数据的容器</div><div class="chapter-subtitle">数组与线性存储 · 12题 · C++ &amp; Python 双语对照</div>
<div class="preface"><p>本章进入数据结构的核心——数组。12道题目覆盖一维数组的遍历、替换、填充、筛选、翻转、递推（斐波那契）、最值查找、二维数组的行列操作，以及质数判定的算法优化。你将掌握Python的列表推导、enumerate、切片翻转，以及C++的vector/array操作。</p></div>
{chr(10).join(parts)}<div class="chapter-end">— 第4章完 · 共12题 —</div></body></html>"""
    (BOOK_ROOT/"textbook"/"chapter04_print.html").write_text(html,encoding="utf-8")

def build_docx():
    from docx import Document;from docx.shared import Pt,Cm,RGBColor;from docx.enum.text import WD_ALIGN_PARAGRAPH;from docx.enum.table import WD_TABLE_ALIGNMENT;from docx.oxml.ns import qn,nsdecls;from docx.oxml import parse_xml
    doc=Document();s=doc.sections[0];s.page_width=Cm(21);s.page_height=Cm(29.7);s.top_margin=Cm(2.2);s.bottom_margin=Cm(2.2);s.left_margin=Cm(2);s.right_margin=Cm(2)
    st=doc.styles['Normal'];st.font.name='等线';st.font.size=Pt(9.5);st.paragraph_format.line_spacing=1.35;st.paragraph_format.space_after=Pt(3);st.element.rPr.rFonts.set(qn('w:eastAsia'),'等线')
    BL=RGBColor(0x25,0x63,0xEB);GR=RGBColor(0x05,0x96,0x69);OR=RGBColor(0xD9,0x77,0x06);GY=RGBColor(0x66,0x66,0x66);LG=RGBColor(0x99,0x99,0x99)
    def acr(para,text,color=None,bold=False,italic=False,fs=Pt(7.5)):
        r=para.add_run(text);r.font.name='Courier New';r.font.size=fs
        if color:r.font.color.rgb=color
        if bold:r.font.bold=True
        if italic:r.font.italic=True;return r
    tp=doc.add_paragraph();tp.alignment=WD_ALIGN_PARAGRAPH.CENTER;tr=tp.add_run('数据的容器');tr.font.size=Pt(20);tr.font.bold=True
    sp=doc.add_paragraph();sp.alignment=WD_ALIGN_PARAGRAPH.CENTER;sr=sp.add_run('数组与线性存储 · 12题 · C++ & Python 双语对照');sr.font.size=Pt(10);sr.font.color.rgb=GY
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
    ep=doc.add_paragraph();ep.alignment=WD_ALIGN_PARAGRAPH.CENTER;ep.paragraph_format.space_before=Pt(24);er=ep.add_run('— 第4章完 · 共12题 —');er.font.size=Pt(8);er.font.color.rgb=LG
    doc.save(str(BOOK_ROOT/"textbook"/"chapter04.docx"))

if __name__=="__main__":
    print("=== Step 1: Build Bank ===");build_bank()
    print("\n=== Step 2: Build HTML ===");build_html();print("✅ chapter04_print.html")
    print("\n=== Step 3: Build DOCX ===");build_docx();print("✅ chapter04.docx")
