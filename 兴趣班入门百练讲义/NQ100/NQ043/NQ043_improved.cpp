#include <cstdio>
using namespace std;

const int MAX_STUDENTS = 50;
const int MAX_COURSES = 5;

int a[MAX_STUDENTS][MAX_COURSES]; // 存储成绩
double b[MAX_COURSES]; // 存储课程平均成绩

int main() {
    int n, m;
    double sum;
    
    while (scanf("%d %d", &n, &m) != EOF) {
        // 输入成绩
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                scanf("%d", &a[i][j]);
        
        // 输出学生平均成绩
        for (int i = 0; i < n; i++) {
            sum = 0;
            for (int j = 0; j < m; j++)
                sum += a[i][j];
            printf("%.2f", sum / m);
            if (i < n - 1) printf(" ");
        }
        printf("\n");
        
        // 计算并输出课程平均成绩
        for (int j = 0; j < m; j++) {
            sum = 0;
            for (int i = 0; i < n; i++)
                sum += a[i][j];
            b[j] = sum / n;
            printf("%.2f", b[j]);
            if (j < m - 1) printf(" ");
        }
        printf("\n");
        
        // 计算符合条件的学生数
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            bool ok = true;
            for (int j = 0; j < m; j++) {
                if (a[i][j] < b[j]) {
                    ok = false;
                    break;
                }
            }
            if (ok) cnt++;
        }
        printf("%d\n\n", cnt);
    }
    
    return 0;
}