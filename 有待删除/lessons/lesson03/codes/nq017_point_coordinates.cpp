#include <iostream>

using namespace std;

int main()
{
    double x, y;
    cin >> x >> y;

    if (x > 0 && y > 0) cout << "Q1" << endl;
    else if (x < 0 && y > 0) cout << "Q2" << endl;
    else if (x < 0 && y < 0) cout << "Q3" << endl;
    else if (x > 0 && y < 0) cout << "Q4" << endl;
    else
    {
      if (!x && !y) cout << "Origem" << endl;
      else if (!y) cout << "Eixo X" << endl;
      else cout << "Eixo Y" << endl;
    }
  return 0;  
}