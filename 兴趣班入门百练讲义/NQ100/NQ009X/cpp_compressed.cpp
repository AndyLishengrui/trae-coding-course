// NQ009X 数组中的行
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double a[12][12];
    int l;
    char t;
    cin >> l >> t;
    for(int i=0;i<12;++i) {
        for(int j=0;j<12;++j) {
            cin >> a[i][j];
        }
    }
    double s = 0;
    for(int i=0;i<12;++i) s += a[l][i];
    cout << fixed << setprecision(1);
    if(t == 'S') cout << s << endl;
    else cout << s/12 << endl;
    return 0;
}