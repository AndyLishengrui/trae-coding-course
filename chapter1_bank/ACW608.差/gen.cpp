#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc, char* argv[]) {
    int tc = argc > 1 ? atoi(argv[1]) : 1;
    srand(time(0) + tc * 1000);
    switch(tc) {
        case 1: cout << "5 6 7 8" << endl; break;
        case 2: cout << "1 2 3 4" << endl; break;
        case 3: cout << rand()%10 << " " << rand()%10 << " " << rand()%10 << " " << rand()%10 << endl; break;
        case 4: cout << "0 0 0 0" << endl; break;
        case 5: cout << rand()%100-50 << " " << rand()%100-50 << " " << rand()%100-50 << " " << rand()%100-50 << endl; break;
        case 6: cout << rand()%1000-500 << " " << rand()%1000-500 << " " << rand()%1000-500 << " " << rand()%1000-500 << endl; break;
        case 7: cout << rand()%5000-2500 << " " << rand()%5000-2500 << " " << rand()%5000-2500 << " " << rand()%5000-2500 << endl; break;
        case 8: cout << rand()%10000 << " " << rand()%10000 << " " << rand()%10000 << " " << rand()%10000 << endl; break;
        case 9: cout << rand()%100000 << " " << rand()%100000 << " " << rand()%100000 << " " << rand()%100000 << endl; break;
        case 10: cout << "10000 10000 10000 10000" << endl; break;
    }
    return 0;
}