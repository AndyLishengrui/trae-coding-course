#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc, char* argv[]) {
    int tc = argc > 1 ? atoi(argv[1]) : 1;
    srand(time(0) + tc * 1000);
    switch(tc) {
        case 1: cout << "4.5 -2.2" << endl; break;
        case 2: cout << "0 0" << endl; break;
        case 3: cout << "0 5" << endl; break;
        case 4: cout << "-3 0" << endl; break;
        case 5: cout << "10 20" << endl; break;
        case 6: cout << "-5 -5" << endl; break;
        case 7: cout << "-1 8" << endl; break;
        case 8: cout << "7 -3" << endl; break;
        case 9: cout << "0.1 0" << endl; break;
        case 10: cout << "0 -0.1" << endl; break;
    }
    return 0;
}
