// NQ041 统计字符个数初步
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;
    cin.ignore();
    char vowels[] = "aeiou";
    for (int t = 0; t < n; t++) {
        int counts[5] = {0};
        string str;
        getline(cin, str);
        transform(str.begin(), str.end(), str.begin(), ::tolower);
        for (char c : str) {
            for (int i = 0; i < 5; i++) {
                if (c == vowels[i]) {
                    counts[i]++;
                    break;
                }
            }
        }
        for (int i = 0; i < 5; i++)
            cout << vowels[i] << ":" << counts[i] << endl;
        if (t < n - 1)
            cout << endl;
    }
    return 0;
}