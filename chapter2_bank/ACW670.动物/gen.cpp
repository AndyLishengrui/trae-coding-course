#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(int argc, char* argv[]) {
    int tc = argc > 1 ? atoi(argv[1]) : 1;
    srand(time(0) + tc * 1000);
    switch(tc) {
        case 1: cout << "vertebrado\nmamifero\nonivoro" << endl; break;
        case 2: cout << "vertebrado\nave\ncarnivoro" << endl; break;
        case 3: cout << "invertebrado\ninseto\nhematofago" << endl; break;
        case 4: cout << "invertebrado\nanelideo\nonivoro" << endl; break;
        case 5: cout << "vertebrado\nmamifero\nonivoro" << endl; break;
        case 6: cout << "vertebrado\nave\ncarnivoro" << endl; break;
        case 7: cout << "invertebrado\ninseto\nhematofago" << endl; break;
        case 8: cout << "invertebrado\nanelideo\nonivoro" << endl; break;
        case 9: cout << "vertebrado\nmamifero\nonivoro" << endl; break;
        case 10: cout << "vertebrado\nave\ncarnivoro" << endl; break;
    }
    return 0;
}
