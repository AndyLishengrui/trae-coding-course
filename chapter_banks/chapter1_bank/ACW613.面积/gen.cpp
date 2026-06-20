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
        case 1: cout << "3.0 4.0 5.2" << endl; break;
        case 2: cout << "3.0 4.0 5.2" << endl; break;
        case 3: cout << "1.0 1.0 1.0" << endl; break;
        case 4: cout << "1.0 1.0 1.0" << endl; break;
        case 5: printf("%.1f %.1f %.1f ", (rand()%100)/10.0+0.1, (rand()%100)/10.0+0.1, (rand()%100)/10.0+0.1); break;
        case 6: printf("%.1f %.1f %.1f ", (rand()%100)/10.0+0.1, (rand()%100)/10.0+0.1, (rand()%100)/10.0+0.1); break;
        case 7: printf("%.1f %.1f %.1f ", (rand()%100)/10.0+0.1, (rand()%100)/10.0+0.1, (rand()%100)/10.0+0.1); break;
        case 8: printf("%.1f %.1f %.1f ", (rand()%1000)/10.0, (rand()%1000)/10.0, (rand()%1000)/10.0); break;
        case 9: printf("%.1f %.1f %.1f ", (rand()%1000)/10.0, (rand()%1000)/10.0, (rand()%1000)/10.0); break;
        case 10: cout << "100.0 100.0 100.0" << endl; break;
    }
    return 0;
}
