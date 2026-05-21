#include <iostream>
#include <vector>
using namespace std;
const int MAX_YEAR = 1000;
vector<long long> precompute() {
    vector<long long> counts(MAX_YEAR + 1, 0);
    for (int year = 1; year <= 4; ++year)
        counts[year] = year;
    for (int year = 5; year <= MAX_YEAR; ++year)
        counts[year] = counts[year-1] + counts[year-3]; // 递推公式：第n年猫数=前一年+前三年
    return counts;
}
int main() {
    vector<long long> cat_counts = precompute();
    int n;
    cin >> n;
    while (n--) {
        int year;
        cin >> year;
        cout << cat_counts[year] << endl;
    }
    return 0;
}