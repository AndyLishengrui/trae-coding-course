#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main(int argc, char* argv[]) {
    int tc = argc > 1 ? atoi(argv[1]) : 1;
    srand(time(0) + tc * 9973);
    
    if (tc == 1) { cout << "25\n100\n5.50" << endl; return 0; }
    if (tc == 2) { cout << "0 0" << endl; return 0; }
    if (tc == 3) { printf("%.2f\n", (rand()%100)/100.0); return 0; }
    if (tc == 4) { printf("%.2f\n", (rand()%100)/100.0); return 0; }
    if (tc == 5) { printf("%.4f\n", (rand()%100000)/100.0); return 0; }
    if (tc == 6) { printf("%.4f\n", (rand()%100000)/100.0); return 0; }
    if (tc == 7) { printf("%.4f\n", (rand()%100000)/100.0); return 0; }
    if (tc == 8) { printf("%.4f\n", (rand()%10000000)/100.0); return 0; }
    if (tc == 9) { printf("%.4f\n", (rand()%10000000)/100.0); return 0; }
    if (tc == 10) { printf("%.4f\n", (rand()%10000000)/100.0); return 0; }
    return 0;
}
