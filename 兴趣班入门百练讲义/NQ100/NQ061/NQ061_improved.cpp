#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    double rect1[4], rect2[4];
    while (scanf("%lf %lf %lf %lf %lf %lf %lf %lf", 
                &rect1[0], &rect1[1], &rect1[2], &rect1[3], 
                &rect2[0], &rect2[1], &rect2[2], &rect2[3]) != EOF) {
        // 确保每个矩形的x1 < x2, y1 < y2
        if (rect1[0] > rect1[2]) swap(rect1[0], rect1[2]);
        if (rect1[1] > rect1[3]) swap(rect1[1], rect1[3]);
        if (rect2[0] > rect2[2]) swap(rect2[0], rect2[2]);
        if (rect2[1] > rect2[3]) swap(rect2[1], rect2[3]);
        
        // 计算重叠区域的边界
        double min_x = max(rect1[0], rect2[0]);
        double max_x = min(rect1[2], rect2[2]);
        double min_y = max(rect1[1], rect2[1]);
        double max_y = min(rect1[3], rect2[3]);
        
        // 判断是否有重叠
        if (min_x >= max_x || min_y >= max_y) {
            printf("0.00\n");
        } else {
            printf("%.2lf\n", (max_x - min_x) * (max_y - min_y));
        }
    }
    return 0;
}