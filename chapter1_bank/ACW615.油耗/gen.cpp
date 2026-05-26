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
        case 1: cout << "500\n35.0" << endl; break;
        case 2: cout << "500\n35.0" << endl; break;
        case 3: cout << "1\n0.1" << endl; break;
        case 4: cout << "1\n0.1" << endl; break;
        case 5: printf("%.1f\n%.1f\n", (rand()%1000+1)*1.0, (rand()%100+1)*1.0); break;
        case 6: printf("%.1f\n%.1f\n", (rand()%1000+1)*1.0, (rand()%100+1)*1.0); break;
        case 7: printf("%.1f\n%.1f\n", (rand()%1000+1)*1.0, (rand()%100+1)*1.0); break;
        case 8: printf("%.1f\n%.1f\n", (rand()%10000+1)*1.0, (rand()%1000+1)*1.0); break;
        case 9: printf("%.1f\n%.1f\n", (rand()%10000+1)*1.0, (rand()%1000+1)*1.0); break;
        case 10: cout << "1000000\n1.0" << endl; break;
    }
    return 0;
}
