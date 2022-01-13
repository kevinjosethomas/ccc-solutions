#include <string>
#include <iostream>

using namespace std;

int main() {

  string encrypted, shift;

  cin >> encrypted >> shift;

  for (int i = 0; i < shift.length(); i++) {

    if (encrypted.find(shift) != string::npos) {
      cout << "yes";
      return 0;
    }

    shift = shift.substr(1, shift.length()-1) + shift[0];

  }

  cout << "no";

}