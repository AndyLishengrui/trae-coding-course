def main():
    t = int(input())
    for _ in range(t):
        u, v, w, l = map(float, input().split())
        res = w * l / (u + v)  # 计算时间：w*l/(u+v)
        print("{0:.3f}".format(res))

if __name__ == "__main__":
    main()