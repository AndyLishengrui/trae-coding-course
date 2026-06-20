#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    double a, b, c;
    cin >> a >> b >> c;
    if (b > a) swap(a, b);
    if (c > a) swap(a, c);
    if (c > b) swap(b, c);
    if (a >= b + c) cout << "NAO FORMA TRIANGULO" << endl;
    else {
        if (a*a == b*b + c*c) cout << "TRIANGULO RETANGULO" << endl;
        if (a*a > b*b + c*c) cout << "TRIANGULO OBTUSANGULO" << endl;
        if (a*a < b*b + c*c) cout << "TRIANGULO ACUTANGULO" << endl;
        if (a == b && b == c) cout << "TRIANGULO EQUILATERO" << endl;
        else if (a == b || a == c || b == c) cout << "TRIANGULO ISOSCELES" << endl;
    }
    return 0;
}
