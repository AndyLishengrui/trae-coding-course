#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc, char* argv[]) {
    int tc = argc > 1 ? atoi(argv[1]) : 1;
    srand(time(0) + tc * 1000);
    switch(tc) {
        case 1: cout << "16 2" << endl; break;
        case 2: cout << "0 0" << endl; break;
        case 3: cout << "7 8 9 10" << endl; break;
        case 4: cout << "0 0 0 0" << endl; break;
        case 5: cout << "23 59 0 0" << endl; break;
        case 6: printf("%d %d ", rand()%24, rand()%24); break;
        case 7: printf("%d %d ", rand()%24, rand()%24); break;
        case 8: printf("%d %d ", rand()%24, rand()%24); break;
        case 9: printf("%d %d ", rand()%24, rand()%24); break;
        case 10: printf("%d %d ", rand()%24, rand()%24); break;
    }
    return 0;
}
