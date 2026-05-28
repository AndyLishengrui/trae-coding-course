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
        case 1: cout << "2.00" << endl; break;
        case 2: cout << "2.00" << endl; break;
        case 3: cout << "0.01" << endl; break;
        case 4: cout << "0.01" << endl; break;
        case 5: printf("%.2f ", (rand()%10000)/100.0); break;
        case 6: printf("%.2f ", (rand()%10000)/100.0); break;
        case 7: printf("%.2f ", (rand()%10000)/100.0); break;
        case 8: printf("%.2f ", (rand()%100000)/100.0); break;
        case 9: printf("%.2f ", (rand()%100000)/100.0); break;
        case 10: cout << "9999.99" << endl; break;
    }
    return 0;
}
