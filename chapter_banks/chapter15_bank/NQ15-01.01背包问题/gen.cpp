#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main(int argc, char* argv[]) {
    int tc = argc > 1 ? atoi(argv[1]) : 1;
    srand(time(0) + tc * 1000);
    
    int N, V;
    switch(tc) {
        case 1: N = 4; V = 5; break;
        case 2: N = 3; V = 10; break;
        case 3: N = 5; V = 15; break;
        case 4: N = 6; V = 20; break;
        case 5: N = 7; V = 25; break;
        case 6: N = 10; V = 100; break;
        case 7: N = 8; V = 50; break;
        case 8: N = 12; V = 80; break;
        case 9: N = 1; V = 10; break;
        case 10: N = 10; V = 200; break;
        default: N = 10; V = 100; break;
    }
    cout << N << " " << V << endl;
    for (int i = 0; i < N; i++) {
        int v = rand() % 50 + 1;
        int w = rand() % 100 + 1;
        cout << v << " " << w << endl;
    }
    return 0;
}
