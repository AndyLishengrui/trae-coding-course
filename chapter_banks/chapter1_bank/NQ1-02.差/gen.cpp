#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main(int argc, char* argv[]) {
    int tc = argc > 1 ? atoi(argv[1]) : 1;
    srand(time(0) + tc * 9973);
    
    int a, b, c;
    // case 1: sample
    if (tc == 1) { cout << "5 6 7 8" << endl; return 0; }
    // case 2: sample
    if (tc == 2) { cout << "0 0" << endl; return 0; }
    if (tc == 3) { cout << rand()%10 << " " << rand()%10 << endl; return 0; }
    if (tc == 4) { cout << rand()%10 << " " << rand()%10 << endl; return 0; }
    if (tc == 5) { cout << rand()%1000-500 << " " << rand()%1000-500 << endl; return 0; }
    if (tc == 6) { cout << rand()%1000-500 << " " << rand()%1000-500 << endl; return 0; }
    if (tc == 7) { cout << rand()%1000-500 << " " << rand()%1000-500 << endl; return 0; }
    if (tc == 8) { cout << rand()%1000000 << " " << rand()%1000000 << endl; return 0; }
    if (tc == 9) { cout << rand()%1000000 << " " << rand()%1000000 << endl; return 0; }
    if (tc == 10) { cout << "1000000000 1000000000" << endl; return 0; }
    return 0;
}
