#include <cstdio>
#include <cmath>
int main() {
    int t, h, m, s;
    scanf("%d", &t);
    while (t--) {
        scanf("%d%d%d", &h, &m, &s);
        // 分针角度：(m + s/60) * 6
        double m_ang = (m + s / 60.0) * 6.0;
        // 时针角度：(h%12 + (m + s/60)/60) * 30
        double h_ang = (h % 12 + (m + s / 60.0) / 60.0) * 30.0;
        double diff = fabs(h_ang - m_ang);
        if (diff > 180) diff = 360 - diff;
        printf("%d\n", (int)diff);
    }
    return 0;
}
