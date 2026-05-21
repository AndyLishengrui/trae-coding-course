#include <iostream>
using namespace std;

const int N = 100007;
int son[N][26];     //输入数据只有小写字母26个
int pcount[N]; //字符串结束标记
int idx;            //Trie树一共有多少个节点
char str_op[2], str[N];
void insert(char str[])
{
    int parent = 0;
    for (int i = 0; str[i]; i++) //字符串最后一个为\0
    {
        int value = str[i] - 'a';
        if (!son[parent][value])
            son[parent][value] = ++idx;
        parent = son[parent][value]; //设置为父节点，接着执行插入
    }
    pcount[parent]++; //插入字符串的最后一个字母打上标记
}

int query(char str[])
{
    int parent = 0;
    for (int i = 0; str[i]; i++)
    {
        int value = str[i] - 'a';
        if (!son[parent][value])
            return 0; //查找不到，返回0
        parent = son[parent][value];
    }
    return pcount[parent]; //返回结束标记，0表示查找不到
}

int main()
{
    // 第一行包含整数N，表示操作数。
    int n;
    cin >> n;
    // 接下来N行，每行包含一个操作指令，指令为”I x”或”Q x”中的一种。
    while (n--)
    {
        cin >> str_op >> str;
        if (str_op[0] == 'I')
            insert(str);           //插入str
        else if (str_op[0] == 'Q') //查询并且输出
            cout << query(str) << endl;
    }

    return 0;
}