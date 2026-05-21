# NQ030 小球进盒子
# R:红球数, B:黑球数, r:红球放入红盒得分, b:黑球放入黑盒得分, A:放入对方盒子得分
def main():
    R, B, r, b, A = map(int, input().split())
    if r + b > 2 * A:
        # r+b>2*A情况，红黑球都放自己盒子
        print(R * r + B * b)
    else:
        # r+b<=2*A情况，交换盒子可能得分更高
        if R > B:
            # 红比黑多，红黑球交换盒子后，剩余红球放红盒
            print(B * A + B * A + (R - B) * r)
        elif B > R:
            # 黑比红多，红黑球交换盒子后，剩余黑球放黑盒
            print(R * A + R * A + (B - R) * b)
        else:
            # 红和黑相等，红黑球交换盒子
            print(R * 2 * A)
if __name__ == "__main__":
    main()