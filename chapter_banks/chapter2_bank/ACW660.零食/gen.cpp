#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc, char* argv[]) {
    int tc = argc > 1 ? atoi(argv[1]) : 1;
    srand(time(0) + tc * 1000);
    switch(tc) {
        case 1: cout << "3 2" << endl; break;
        case 2: cout << "3 2" << endl; break;
        case 3: cout << rand()%5+1 << " " << rand()%10+1 << endl; break;
        case 4: cout << rand()%5+1 << " " << rand()%10+1 << endl; break;
        case 5: cout << rand()%5+1 << " " << rand()%10+1 << endl; break;
        case 6: cout << rand()%5+1 << " " << rand()%100+1 << endl; break;
        case 7: cout << rand()%5+1 << " " << rand()%100+1 << endl; break;
        case 8: cout << rand()%5+1 << " " << rand()%100+1 << endl; break;
        case 9: cout << rand()%5+1 << " " << rand()%100+1 << endl; break;
        case 10: cout << rand()%5+1 << " " << rand()%100+1 << endl; break;
    }
    return 0;
}
