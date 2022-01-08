#include <iostream>

using namespace std;

int main() {

  int tippingPoint, infected, infectionRate;

  cin >> tippingPoint >> infected >> infectionRate;

  int iterations = 0;
  int newlyInfected = infected;

  while (infected <= tippingPoint) {
    iterations++;
    newlyInfected = newlyInfected * infectionRate;
    infected += newlyInfected;
  }

  cout << iterations;

}
