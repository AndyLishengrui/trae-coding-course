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
        case 1: cout << "25\n100\n5.50" << endl; break;
        case 2: cout << "25\n100\n5.50" << endl; break;
        case 3: cout << "1\n1\n1.00" << endl; break;
        case 4: cout << "1\n1\n1.00" << endl; break;
        case 5: printf("%d\n%d\n%.2f\n", rand()%50+1, rand()%200+1, (rand()%5000)/100.0+1); break;
        case 6: printf("%d\n%d\n%.2f\n", rand()%50+1, rand()%200+1, (rand()%5000)/100.0+1); break;
        case 7: printf("%d\n%d\n%.2f\n", rand()%50+1, rand()%200+1, (rand()%5000)/100.0+1); break;
        case 8: printf("%d\n%d\n%.2f\n", rand()%100+1, rand()%200+1, (rand()%5000)/100.0+1); break;
        case 9: printf("%d\n%d\n%.2f\n", rand()%100+1, rand()%200+1, (rand()%5000)/100.0+1); break;
        case 10: cout << "100\n200\n50.00" << endl; break;
    }
    return 0;
}
