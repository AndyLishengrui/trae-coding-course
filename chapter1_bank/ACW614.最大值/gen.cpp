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
        case 1: cout << "7 14 106" << endl; break;
        case 2: cout << "7 14 106" << endl; break;
        case 3: cout << "-100 -200 -300" << endl; break;
        case 4: cout << "-100 -200 -300" << endl; break;
        case 5: printf("%d %d %d\n", rand()%1000-500, rand()%1000-500, rand()%1000-500); break;
        case 6: printf("%d %d %d\n", rand()%1000-500, rand()%1000-500, rand()%1000-500); break;
        case 7: printf("%d %d %d\n", rand()%1000-500, rand()%1000-500, rand()%1000-500); break;
        case 8: printf("%d %d %d\n", rand()%2000000000-1000000000, rand()%2000000000-1000000000, rand()%2000000000-1000000000); break;
        case 9: printf("%d %d %d\n", rand()%2000000000-1000000000, rand()%2000000000-1000000000, rand()%2000000000-1000000000); break;
        case 10: cout << "1000000000 999999999 1000000000" << endl; break;
    }
    return 0;
}
