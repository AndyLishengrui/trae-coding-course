#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc, char* argv[]) {
    int tc = argc > 1 ? atoi(argv[1]) : 1;
    srand(time(0) + tc * 1000);
    switch(tc) {
        case 1: cout << "6.0 4.0 2.0" << endl; break;
        case 2: cout << "3.0 4.0 5.0" << endl; break;
        case 3: cout << "5.0 5.0 5.0" << endl; break;
        case 4: cout << "1.0 2.0 3.0" << endl; break;
        case 5: cout << "10.0 10.0 1.0" << endl; break;
        case 6: printf("%.1f %.1f %.1f ", (rand()%100+1)*1.0, (rand()%100+1)*1.0, (rand()%100+1)*1.0); break;
        case 7: printf("%.1f %.1f %.1f ", (rand()%100+1)*1.0, (rand()%100+1)*1.0, (rand()%100+1)*1.0); break;
        case 8: printf("%.1f %.1f %.1f ", (rand()%100+1)*1.0, (rand()%100+1)*1.0, (rand()%100+1)*1.0); break;
        case 9: printf("%.1f %.1f %.1f ", (rand()%100+1)*1.0, (rand()%100+1)*1.0, (rand()%100+1)*1.0); break;
        case 10: printf("%.1f %.1f %.1f ", (rand()%100+1)*1.0, (rand()%100+1)*1.0, (rand()%100+1)*1.0); break;
    }
    return 0;
}
