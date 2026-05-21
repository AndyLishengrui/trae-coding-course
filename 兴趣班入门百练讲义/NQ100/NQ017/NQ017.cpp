//NQ017 计算绩点
#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    float s, c, gpa, ctot = 0, gpatot = 0; // 初始化ctot和gpatot为0
    int q;
    cin >> q;
    while (q--)
    {
        cin >> s >> c;
        
        gpa = 0.0; // 初始化gpa为0.0，避免未定义行为

        if (s >= 90 && s <= 100)
            gpa = 4.0;
        else if (s >= 85 && s < 90)
            gpa = 3.7;
        else if (s >= 81 && s < 85)
            gpa = 3.3;
        else if (s >= 78 && s < 81)
            gpa = 3.0;
        else if (s >= 75 && s < 78)
            gpa = 2.7;
        else if (s >= 72 && s < 75)
            gpa = 2.3;
        else if (s >= 68 && s < 72)
            gpa = 2.0;
        else if (s >= 64 && s < 68)
            gpa = 1.7;
        else if (s >= 60 && s < 64)
            gpa = 1.0;   
        ctot += c;
        gpatot += gpa * c;
    }

    cout << fixed << setprecision(4) << gpatot / ctot << endl; // 输出

    return 0;
}