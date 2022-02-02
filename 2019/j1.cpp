#include <iostream>

using namespace std;

int main() {


  int apples_3, apples_2, apples_1;
  cin >> apples_3 >> apples_2 >> apples_1;

  int bananas_3, bananas_2, bananas_1;
  cin >> bananas_3 >> bananas_2 >> bananas_1;

  int apples_score = (apples_3 * 3) + (apples_2 * 2) + apples_1;
  int bananas_score = (bananas_3 * 3) + (bananas_2 * 2) + bananas_1;

  if (apples_score > bananas_score) {
    cout << "A";
  } else if (apples_score < bananas_score) {
    cout << "B";
  } else {
    cout << "T";
  }

}