// NQ014X 数组的左下半部分
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double a[12][12];
    char t;
    cin >> t;
    for(int i=0;i<12;++i) {
        for(int j=0;j<12;++j) {
            cin >> a[i][j];
        }
    }
    double s = 0;
    int cnt = 0;
    for(int i=0;i<12;++i) {
        for(int j=0;j<i;++j) {
            s += a[i][j];
            cnt++;
        }
    }
    cout << fixed << setprecision(1);
    if(t == 'S') cout << s << endl;
    else cout << s/cnt << endl;
    return 0;
}