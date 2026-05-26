#include <iostream>

using namespace std;

const int N = 1010;

void print(int a[], int size)
{
    for (int i = 0; i < size; i ++ )
        cout << a[i] << ' ';
    cout << endl;    

}

int main()
{
    int n, size;
    int a[N];

    cin >> n >> size;
    for (int i = 0; i < n; i ++ ) cin >> a[i];

    print(a, size);

    return 0;
}