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
        case 1: cout << "1.0 7.0 5.0 9.0" << endl; break;
        case 2: cout << "1.0 7.0 5.0 9.0" << endl; break;
        case 3: cout << "0 0 0 0" << endl; break;
        case 4: cout << "0 0 0 0" << endl; break;
        case 5: printf("%.1f %.1f %.1f %.1f ", (rand()%200-100)*1.0, (rand()%200-100)*1.0, (rand()%200-100)*1.0, (rand()%200-100)*1.0); break;
        case 6: printf("%.1f %.1f %.1f %.1f ", (rand()%200-100)*1.0, (rand()%200-100)*1.0, (rand()%200-100)*1.0, (rand()%200-100)*1.0); break;
        case 7: printf("%.1f %.1f %.1f %.1f ", (rand()%200-100)*1.0, (rand()%200-100)*1.0, (rand()%200-100)*1.0, (rand()%200-100)*1.0); break;
        case 8: printf("%.1f %.1f %.1f %.1f ", (rand()%20000-10000)*1.0, (rand()%20000-10000)*1.0, (rand()%20000-10000)*1.0, (rand()%20000-10000)*1.0); break;
        case 9: printf("%.1f %.1f %.1f %.1f ", (rand()%20000-10000)*1.0, (rand()%20000-10000)*1.0, (rand()%20000-10000)*1.0, (rand()%20000-10000)*1.0); break;
        case 10: cout << "-10000 -10000 10000 10000" << endl; break;
    }
    return 0;
}
