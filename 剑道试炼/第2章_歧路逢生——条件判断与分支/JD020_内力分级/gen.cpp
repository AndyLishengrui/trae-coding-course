#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc, char* argv[]) {
    int tc = argc > 1 ? atoi(argv[1]) : 1;
    srand(time(0) + tc * 1000);
    switch(tc) {
        case 1: cout << "25.01" << endl; break;
        case 2: cout << "-10.0" << endl; break;
        case 3: cout << "0" << endl; break;
        case 4: cout << "25" << endl; break;
        case 5: cout << "50" << endl; break;
        case 6: cout << "50.01" << endl; break;
        case 7: cout << "75" << endl; break;
        case 8: cout << "100" << endl; break;
        case 9: cout << "100.01" << endl; break;
        case 10: cout << "200" << endl; break;
    }
    return 0;
}
