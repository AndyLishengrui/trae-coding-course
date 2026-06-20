# 题库3 章节处理指南（Goal 命令用）

## 目标

按以下流程处理题库3（剑道录）的每个章节，确保题面质量、代码正确性、OJ数据一致。

---

## 一、章节处理完整流程

### Step 1：审查现状
- 列出章节目录，检查每题是否具备：problem.md、problem.json、Andy.cpp、testcase/（10组.in/.out）
- 标记缺失项

### Step 2：重写题面（最关键的一步）

**必须满足的规范：**

1. **叙事扣题展开**
   - 标题是武侠风的，题面内容也必须是武侠场景
   - 禁止出现"赵晴儿：写一个函数int max(int x, int y)"这种干瘪格式
   - 正确做法：先描述武侠场景（炼丹、比剑、采药、剑阵、兵器库等），场景自然引出编程任务

2. **应用题风格**
   - 叙事和问题融为一体，不单独分"剧情"段
   - 结构：场景 → 困境/需求 → 自然引出编程任务

3. **格式要求**
   - 人物对话正确分段，每段对话单独一行
   - 题目描述不能挤成一行，要有合理的段落间距
   - 使用中文引号「」""，不用英文引号

4. **不变项**
   - AcWing ID、知识点标签、输入输出格式、样例、解题思路保持不变
   - 只改写「题目描述」段落

5. **一致性检查**
   - problem.md 的输入输出格式描述必须与 testcase 实际数据一致
   - problem.md 的样例必须与 problem.json 的 samples 字段一致
   - 不能有葡萄牙语残留（Fora、Novo、Entrada、Saida 等）

### Step 3：本地编译测试
- 每题的 Andy.cpp 用 g++ -std=c++11 -O2 编译
- 对全部 10 组 testcase 运行，diff -b 比较输出
- 必须 10/10 PASS，否则修正 Andy.cpp 或 testcase

### Step 4：更新 OJ 数据库
- **不重新导入 ZIP**（会产生重复题目）
- 直接通过 Django shell 更新数据库字段：
  - description（题目描述 HTML）
  - samples（样例 JSON）
  - hint（解题提示，如有改动）
  - input_description / output_description（如有改动）
- 更新方法：
  ```python
  # 生成脚本 → docker cp 到容器 → docker exec 执行
  docker exec onlinejudgedeploy-oj-backend-1 python manage.py shell -c "exec(open('/tmp/update_script.py').read())"
  ```

### Step 5：多 Agent AC 验证
- 启动 2-3 个 agent 并行提交代码到 OJ
- 每题提交 Andy.cpp，检查 result=0（Accepted）且 score=100
- 如果有未通过的题，检查 visibility 和 contest 关联

### Step 6：修复 test case 中的未定义行为
- 如果测试用例依赖未初始化栈内存（读取了未赋值的数组元素），需要：
  1. 重写 Andy.cpp 使用全局数组（自动零初始化）
  2. 重新生成 testcase（确保 size ≤ n，不读越界数据）

---

## 二、关键文件路径

```
题库3/
├── 第N章_章名——知识点/
│   ├── JDxxx_题名/
│   │   ├── problem.md        ← 题面（武侠叙事）
│   │   ├── problem.json      ← OJ 导入格式（description/samples/hint）
│   │   ├── Andy.cpp          ← C++ 参考答案（需通过全部 testcase）
│   │   ├── Andy.py           ← Python 参考答案
│   │   └── testcase/
│   │       ├── 1.in ~ 10.in  ← 10 组测试输入
│   │       ├── 1.out ~ 10.out← 10 组期望输出
│   │       └── info           ← 测试元数据
├── _import_zips/              ← ZIP 文件（仅首次导入用）
├── jd_mapping.json            ← JD ↔ NQ 映射
└── GOAL_章节处理指南.md        ← 本文件
```

---

## 三、OJ 数据库操作速查

### 查看题目
```python
from problem.models import Problem
p = Problem.objects.filter(_id='JD081').order_by('-id').first()
print(p.description, p.samples)
```

### 更新题目描述
```python
p.description = '<p>新的HTML描述</p>'
p.samples = '[{"input": "...", "output": "..."}]'
p.save()
```

### 设置可见性
```python
p.visible = True
p.save()
```

### 加入实验
```python
from contest.models import Contest
c = Contest.objects.get(id=367)
c.problem_set.add(p)
```

### 删除重复题目
```python
# 保留实验中的那份，删除其他
for p in Problem.objects.filter(_id='JDxxx'):
    if p.id not in contest_ids:
        p.delete()
```

---

## 四、已处理章节状态

| 章节 | 题号范围 | 题数 | AC验证 | 题面质量 |
|------|---------|:----:|:------:|:--------:|
| 第1章 持剑叩门 | JD001-JD014 | 14 | ✅ | ✅ |
| 第2章 歧路逢生 | JD015-JD028 | 14 | ✅ | ✅ |
| 第3章 千回百转 | JD029-JD042 | 14 | ✅ | ✅ |
| 第4章 排兵布阵 | JD043-JD054 | 12 | ✅ | ✅ |
| 第5章 十二宫剑阵 | JD055-JD066 | 12 | ✅ | ✅ |
| 第6章 古卷密文 | JD067-JD080 | 14 | ✅ | ✅ |
| 第7章 以招创招 | JD081-JD095 | 15 | ✅ | ✅ 已重写 |
| 第8章 百器图谱 | JD096-JD102 | 7 | ✅ | ⚠️ 待审查 |
| 第9章 照妖镜 | JD103-JD109 | 7 | ❌ | ❌ 待处理 |
| 第10章 蓄势心法 | JD110-JD116 | 7 | ❌ | ❌ 待处理 |
| 第11章 精铸阁 | JD117-JD123 | 7 | ❌ | ❌ 待处理 |
| 第12章 奇门兵器 | JD124-JD131 | 8 | ❌ | ❌ 待处理 |
| 第13章 迷踪林 | JD132-JD139 | 8 | ❌ | ❌ 待处理 |
| 第14章 城际连横 | JD140-JD147 | 8 | ❌ | ❌ 待处理 |
| 第15章 谋略堂 | JD148-JD155 | 8 | ❌ | ❌ 待处理 |
| 第16章 掌门之争 | JD156-JD161 | 6 | ❌ | ❌ 待处理 |

---

## 五、常见问题

### Q: 导入 ZIP 后题目重复了怎么办？
A: 通过 Django shell 删除重复，保留实验中的那份。

### Q: 提交代码返回 "Problem not exist"？
A: 检查题目是否 visible=True 且已加入 contest。

### Q: 测试用例依赖未初始化内存？
A: 用全局数组替代局部数组，重新生成 testcase。

### Q: problem.md 和 testcase 不一致？
A: 以 testcase（AC验证通过的）为准，修正 problem.md 的描述。
