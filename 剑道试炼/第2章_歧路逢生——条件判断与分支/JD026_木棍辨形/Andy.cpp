#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    double a, b, c;
    cin >> a >> b >> c;
    if (b > a) swap(a, b);
    if (c > a) swap(a, c);
    if (c > b) swap(b, c);
    if (a >= b + c) cout << "Not a triangle" << endl;
    else {
        if (a*a == b*b + c*c) cout << "Right" << endl;
        if (a*a > b*b + c*c) cout << "Obtuse" << endl;
        if (a*a < b*b + c*c) cout << "Acute" << endl;
        if (a == b && b == c) cout << "Equilateral" << endl;
        else if (a == b || a == c || b == c) cout << "Isosceles" << endl;
    }
    return 0;
}
