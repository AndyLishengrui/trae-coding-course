import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    
    while ptr < len(input):
        n, m = int(input[ptr]), int(input[ptr+1])
        ptr += 2
        
        # 读取成绩
        scores = []
        for _ in range(n):
            scores.append(list(map(int, input[ptr:ptr+m])))
            ptr += m
        
        # 输出学生平均成绩
        student_avgs = ["{:.2f}".format(sum(s)/m) for s in scores]
        print(' '.join(student_avgs))
        
        # 计算课程平均成绩
        course_avgs = []
        for j in range(m):
            total = sum(scores[i][j] for i in range(n))
            course_avgs.append(total / n)
        
        # 输出课程平均成绩
        course_avg_strs = ["{:.2f}".format(avg) for avg in course_avgs]
        print(' '.join(course_avg_strs))
        
        # 计算符合条件的学生数
        cnt = 0
        for s in scores:
            if all(s[j] >= course_avgs[j] for j in range(m)):
                cnt += 1
        print(cnt)
        print()  # 测试用例之间的空行

if __name__ == "__main__":
    main()