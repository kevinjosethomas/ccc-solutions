#include <string>
#include <iostream>

using namespace std;

int main() {

  int num;
  cin >> num;

  for (int i = 0; i < num; i++) {

    int count;
    char character;
    cin >> count >> character;

    string coded(count, character);

    cout << coded << endl;

  }

}