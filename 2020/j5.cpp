#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

const int mn = 1005;
int room[mn][mn];
int height, length;

vector<vector<int>> history;

bool find_path(int product, vector<vector<int>> history) {
  if (product == 1) {
    return true;
  }

  for (int row = 0; row < height; row++) {
    for (int col = 0; col < length; col++) {
      if ((room[row][col]) != product) {
        continue;
      }

      vector<int> pair = {row, col};

      if (count(history.begin(), history.end(), pair)) {
        return false;
      }

      history.push_back(pair);

      if (find_path((row+1) * (col+1), history)) {
        return true;
      }

    }
  }

  return false;
}

int main() {
  cin >> height >> length;

  for (int m = 0; m < height; m++) {
    for (int n = 0; n < length; n++) {
      int x; cin >> x;
      room[m][n] = x;
    }
  }

  bool success = find_path(height * length, history);

  if (success) {
    cout << "yes";
  } else {
    cout << "no";
  }

}
