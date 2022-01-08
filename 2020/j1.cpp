#include <iostream>

using namespace std;

int main() {

  int small, medium, large;
  cin >> small >> medium >> large;

  int score = small + (2 * medium) + (3 * large);

  if (score >= 10) {
    cout << "happy";
  } else {
    cout << "sad";
  }

}