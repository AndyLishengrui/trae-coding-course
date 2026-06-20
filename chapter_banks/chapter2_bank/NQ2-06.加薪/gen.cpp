#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc, char* argv[]) {
    int tc = argc > 1 ? atoi(argv[1]) : 1;
    srand(time(0) + tc * 1000);
    switch(tc) {
        case 1: cout << "400.00" << endl; break;
        case 2: cout << "800.01" << endl; break;
        case 3: cout << "1200.00" << endl; break;
        case 4: cout << "2000.00" << endl; break;
        case 5: cout << "3000.00" << endl; break;
        case 6: printf("%.2f ", (rand()%50000)/100.0+0.01); break;
        case 7: printf("%.2f ", (rand()%50000)/100.0+0.01); break;
        case 8: printf("%.2f ", (rand()%50000)/100.0+0.01); break;
        case 9: printf("%.2f ", (rand()%50000)/100.0+0.01); break;
        case 10: printf("%.2f ", (rand()%50000)/100.0+0.01); break;
    }
    return 0;
}
