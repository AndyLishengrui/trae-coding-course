#include <iostream>
#include <cstdlib>
#include <ctime>
#include <algorithm>
using namespace std;

int main(int argc, char* argv[]) {
    int tc = argc > 1 ? atoi(argv[1]) : 1;
    srand(time(0) + tc * 1000);
    int n = 5 + rand() % 10;
    int m = 5 + rand() % 10;
    cout << n << " " << m << " " << (rand() % 100 + 1) << endl;
    // Generate sorted array A
    int val = 0;
    for (int i = 0; i < n; i++) {
        val += rand() % 5 + 1;
        cout << val << (i < n-1 ? " " : "\n");
    }
    // Generate sorted array B
    val = 0;
    for (int i = 0; i < m; i++) {
        val += rand() % 5 + 1;
        cout << val << (i < m-1 ? " " : "\n");
    }
    return 0;
}
