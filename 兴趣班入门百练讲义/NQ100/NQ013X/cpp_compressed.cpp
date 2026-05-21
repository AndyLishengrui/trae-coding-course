// NQ013X 数组中的列
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double a[12][12];
    int c;
    char t;
    cin >> c >> t;
    for(int i=0;i<12;++i) {
        for(int j=0;j<12;++j) {
            cin >> a[i][j];
        }
    }
    double s = 0;
    for(int i=0;i<12;++i) s += a[i][c];
    cout << fixed << setprecision(1);
    if(t == 'S') cout << s << endl;
    else cout << s/12 << endl;
    return 0;
}