#include <iostream>
using namespace std;
int main() {
    int arr[20];
    for (int i = 0; i < 20; i++) cin >> arr[i];
    for (int i = 0; i < 10; i++) swap(arr[i], arr[19 - i]);
    for (int i = 0; i < 20; i++)
        cout << "N[" << i << "] = " << arr[i] << endl;
    return 0;
}
