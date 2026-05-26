#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <iomanip>
using namespace std;

int main(int argc, char* argv[]) {
    int tc = argc > 1 ? atoi(argv[1]) : 1;
    srand(time(0) + tc * 1000);
    
    switch(tc) {
        case 1: cout << "5.0\n7.1" << endl; break;
        case 2: cout << "5.0\n7.1" << endl; break;
        case 3: cout << "0.0\n10.0" << endl; break;
        case 4: cout << "0.0\n10.0" << endl; break;
        case 5: printf("%.1f\n%.1f\n", (rand()%100)/10.0, (rand()%100)/10.0); break;
        case 6: printf("%.1f\n%.1f\n", (rand()%100)/10.0, (rand()%100)/10.0); break;
        case 7: printf("%.1f\n%.1f\n", (rand()%100)/10.0, (rand()%100)/10.0); break;
        case 8: printf("%.1f\n%.1f\n", (rand()%100)/10.0, (rand()%100)/10.0); break;
        case 9: printf("%.1f\n%.1f\n", (rand()%100)/10.0, (rand()%100)/10.0); break;
        case 10: printf("%.1f\n%.1f\n", (rand()%100)/10.0, (rand()%100)/10.0); break;
    }
    return 0;
}
