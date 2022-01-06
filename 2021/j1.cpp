#include <iostream>

using namespace std;

int main() {

  const int PRESSURE_AT_SEA_LEVEL = 100;

  int boiling;
  cin >> boiling;

  int pressure = 5 * boiling - 400;

  cout << pressure << endl;

  if (pressure < PRESSURE_AT_SEA_LEVEL) {
    cout << 1;
  } else if (pressure > PRESSURE_AT_SEA_LEVEL) {
    cout << -1;
  } else {
    cout << 0;
  }

}