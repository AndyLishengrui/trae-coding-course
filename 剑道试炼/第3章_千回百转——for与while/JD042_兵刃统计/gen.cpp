#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc, char* argv[]) {
    int tc = argc > 1 ? atoi(argv[1]) : 1;
    srand(time(0) + tc * 1000);
    int n;
    switch(tc) {
        case 1: n = 11; break;
        case 2: n = 8; break;
        case 3: n = rand() % 15 + 5; break;
        case 4: n = rand() % 15 + 5; break;
        case 5: n = rand() % 15 + 5; break;
        case 6: n = rand() % 30 + 10; break;
        case 7: n = rand() % 30 + 10; break;
        case 8: n = rand() % 30 + 10; break;
        case 9: n = rand() % 50 + 10; break;
        case 10: n = rand() % 50 + 10; break;
    }
    cout << n << endl;
    for (int i = 0; i < n; i++) {
        int k = rand() % 15 + 1;
        char t = "CRF"[rand() % 3];
        cout << k << " " << t << endl;
    }
    return 0;
}
