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
        case 1: cout << "3\n9" << endl; break;
        case 2: cout << "3\n9" << endl; break;
        case 3: cout << rand()%100 << " " << rand()%100 << endl; break;
        case 4: cout << rand()%100 << " " << rand()%100 << endl; break;
        case 5: cout << rand()%10000-5000 << " " << rand()%10000-5000 << endl; break;
        case 6: cout << rand()%10000-5000 << " " << rand()%10000-5000 << endl; break;
        case 7: cout << rand()%10000-5000 << " " << rand()%10000-5000 << endl; break;
        case 8: cout << rand()%1000000 << " " << rand()%1000000 << endl; break;
        case 9: cout << rand()%1000000 << " " << rand()%1000000 << endl; break;
        case 10: cout << 1000000000 << " " << 1000000000 << endl; break;
    }
    return 0;
}
