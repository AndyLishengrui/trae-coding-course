#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main(int argc, char* argv[]) {
    int tc = argc > 1 ? atoi(argv[1]) : 1;
    srand(time(0) + tc * 9973);
    
    if (tc == 1) { cout << "3\n9" << endl; return 0; }
    if (tc == 2) { cout << "0 0" << endl; return 0; }
    if (tc == 3) { cout << "2\n1 2\n3 4" << endl; return 0; }
    if (tc == 4) { cout << "2\n1 2\n3 4" << endl; return 0; }
    if (tc == 5) { int n=rand()%5+3; cout<<n<<endl; for(int j=0;j<n;j++){ for(int k=0;k<n;k++) cout<<(rand()%200-100)<<" "; cout<<endl; } return 0; }
    if (tc == 6) { int n=rand()%5+3; cout<<n<<endl; for(int j=0;j<n;j++){ for(int k=0;k<n;k++) cout<<(rand()%200-100)<<" "; cout<<endl; } return 0; }
    if (tc == 7) { int n=rand()%5+3; cout<<n<<endl; for(int j=0;j<n;j++){ for(int k=0;k<n;k++) cout<<(rand()%200-100)<<" "; cout<<endl; } return 0; }
    if (tc == 8) { int n=10; cout<<n<<endl; for(int j=0;j<n;j++){ for(int k=0;k<n;k++) cout<<(rand()%20000-10000)<<" "; cout<<endl; } return 0; }
    if (tc == 9) { int n=10; cout<<n<<endl; for(int j=0;j<n;j++){ for(int k=0;k<n;k++) cout<<(rand()%20000-10000)<<" "; cout<<endl; } return 0; }
    if (tc == 10) { int n=10; cout<<n<<endl; for(int j=0;j<n;j++){ for(int k=0;k<n;k++) cout<<(rand()%20000-10000)<<" "; cout<<endl; } return 0; }
    return 0;
}
