#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc, char* argv[]) {
    int tc = argc > 1 ? atoi(argv[1]) : 1;
    srand(time(0) + tc * 1000);
    switch(tc) {
        case 1: cout << "11" << endl; break;
        case 2: cout << "61" << endl; break;
        case 3: cout << "71" << endl; break;
        case 4: cout << "21" << endl; break;
        case 5: cout << "32" << endl; break;
        case 6: cout << "19" << endl; break;
        case 7: cout << "27" << endl; break;
        case 8: cout << "31" << endl; break;
        case 9: cout << "99" << endl; break;
        case 10: cout << "100" << endl; break;
    }
    return 0;
}
