#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {

  int num_of_drops;
  cin >> num_of_drops;

  vector<int> xs;
  vector<int> ys;

  for (int i = 0; i < num_of_drops; i++) {

    string drop;
    cin >> drop;

    int x, y;
    x = stoi(drop.substr(0,2));
    y = stoi(drop.substr(3,2));

    xs.push_back(x);
    ys.push_back(y);

  }

  int min_x, min_y, max_x, max_y;
  min_x = *min_element(xs.begin(), xs.end()) - 1;
  min_y = *min_element(ys.begin(), ys.end()) - 1;
  max_x = *max_element(xs.begin(), xs.end()) + 1;
  max_y = *max_element(ys.begin(), ys.end()) + 1;

  cout << min_x << "," << min_y << endl;
  cout << max_x << "," << max_y;

}