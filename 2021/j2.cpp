#include <string>
#include <vector>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

struct Bid {
  int index, amount;
  string name;
};

bool compareBids(Bid b1, Bid b2) {
  return b1.amount > b2.amount;
}

int main() {

  int num_of_bids;
  vector<Bid> bids;

  cin >> num_of_bids;

  for (int i = 0; i < num_of_bids; i++) {
    int amount;
    string name;

    cin >> name >> amount;

    bids.push_back({ i, amount, name });
  }

  sort(bids.begin(), bids.end(), compareBids);

  cout << bids[0].name;

}

