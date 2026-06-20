"""Shared constants for xmuoj_cli.

NQ 编号说明：
  - V2_PLAN 中的 NQ 编号是 OJ 顺序编号（NQ1-01 = 第1章第1题 = AcWing 1 = A+B）
  - 兴趣班入门百练讲义/NQ100/ 中的 NQ 编号是原始教材编号（NQ001 = 求连续整数和）
  - 两者是不同的编号体系，不要混淆
"""
from typing import Dict, List, Tuple, Union

# 每个条目可以是 int（AcWing题号）或 dict（自定义题）
# dict 格式: {"nq": "NQ012", "title": "中文标题"}
V2_PLAN: Dict[int, List[Union[int, dict]]] = {
    1: [1, 608, 604, 606, 609, 615, 616, 653, 654, 605, 611, 612, 613, 614],
    2: [665, 660, 659, 664, 667, 669, 670, 657, 671, 662, 666, 668, 672, 663],
    3: [708, 709, 712, 714, 716, 721, 720, 724, 723, 710, 711, 718, 715, 713, {"nq": "NQ012", "title": "水仙花数"}],
    4: [737, 738, 739, 743, 740, 741, 742, 744, 717, 722, 725, 726, {"nq": "NQ029", "title": "蛇形矩阵"}, {"nq": "NQ027", "title": "矩阵加法"}],
    5: [745, 747, 749, 751, 753, 748, 746, 750, 752, 754, 755, 756],
    6: [760, 761, 763, 765, 769, 773, 772, 762, 767, 764, 770, 774, {"nq": "NQ053", "title": "字符串统计"}],
    7: [804, 805, 808, 811, 812, 813, 819, 820, 821, 822, 823, 818, {"nq": "NQ016", "title": "哥德巴赫猜想"}],
    8: [16, 17, 20, 21, 35, 36, 862, 810, 814, 816],
    9: [785, 786, 787, 788, 789, 790, 727],
    10: [795, 796, 797, 798, 799, 800, 2816, {"nq": "NQ059", "title": "二维前缀和"}, {"nq": "NQ070", "title": "双指针去重"}],
    11: [791, 792, 801, 793, 794, 802, 803],
    12: [826, 828, 829, 3302, 830, 154, 831, 839],
    13: [842, 843, 844, 845, 846, 847, 777, 778, {"nq": "NQ079", "title": "马的遍历"}, {"nq": "NQ080", "title": "八皇后"}],
    14: [848, 849, 850, 851, 854, 858, 859, 860],
    15: [2, 3, 898, 895, 897, 282, 902, 901],
    16: [905, 148, 836, 837, 240, 875, 868, 104, {"nq": "NQ099", "title": "逆序对计数"}],
}

CHAPTER_TITLES: Dict[int, str] = {
    1: "程序设计的第一个脚印——变量、输入输出与顺序结构",
    2: "选择的艺术——条件判断与分支结构",
    3: "循环的魔力——for/while与嵌套循环",
    4: "数据的容器——数组与线性存储",
    5: "矩阵的舞蹈——多维数组与矩阵模式",
    6: "字符的世界——字符串处理",
    7: "模块化的力量——函数、递归与库的威力",
    8: "指针与抽象——结构体、指针与STL容器",
    9: "分治之美——排序与二分",
    10: "预处理的艺术——前缀和、差分与双指针",
    11: "数字的奥秘——高精度、位运算与离散化",
    12: "结构的根基——基础数据结构",
    13: "搜索的疆域——搜索与回溯",
    14: "图的世界——图论入门",
    15: "最优子结构——动态规划",
    16: "智慧的策略——贪心、并查集与数学",
}


def normalize_pid(entry: Union[int, dict]) -> Tuple[str, str, Union[int, dict]]:
    """将 V2_PLAN 条目标准化为 (display_id, source_type, original_entry)

    Returns:
        display_id: OJ 中的题目显示 ID (如 "ACW785" 或 "NQ012")
        source_type: "acw" 表示 AcWing 题目，"nq" 表示自定义题目
        original_entry: 原始条目（int 或 dict）
    """
    if isinstance(entry, int):
        return f"ACW{entry}", "acw", entry
    elif isinstance(entry, dict):
        nq_id = entry.get("nq", "")
        return nq_id, "nq", entry
    else:
        raise ValueError(f"Invalid V2_PLAN entry type: {type(entry)}: {entry}")


def get_chapter_problems(chapter: int) -> List:
    """Get problem IDs for a chapter."""
    return V2_PLAN.get(chapter, [])


def get_chapter_title(chapter: int) -> str:
    """Get display title for a chapter."""
    return CHAPTER_TITLES.get(chapter, f"第{chapter}章")


def get_nq_sequential_num(chapter: int, index_in_chapter: int) -> int:
    """计算全局顺序 NQ 编号（1-based）

    例如：第1章第1题 → NQ1-01, 第2章第1题 → NQ1-15（第1章14题）
    """
    nq = 0
    for ch in range(1, chapter):
        nq += len(V2_PLAN.get(ch, []))
    return nq + index_in_chapter
