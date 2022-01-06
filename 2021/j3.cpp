#include <vector>
#include <iostream>

using namespace std;


struct Instruction {
  bool direction;
  int steps;
};

int main() {

  // false = left
  // true = right
  bool lastInstruction = false;
  vector<Instruction> instructions;

  while (true) {

    string instruction;
    cin >> instruction;

    if (instruction == "99999") {
      break;
    }

    int sum = (instruction[0] - '0') + (instruction[1] - '0');
    int steps = stoi(instruction.substr(2,3));

    if (sum % 2 == 0 && sum != 0) {
      lastInstruction = true;
    } else if (sum % 2 != 0) {
      lastInstruction = false;
    }

    instructions.push_back({ lastInstruction, steps });

  }

  for (int i = 0; i < instructions.size(); i++) {
    if (instructions[i].direction) {
      cout << "right " << instructions[i].steps << endl;
    } else {
      cout << "left " << instructions[i].steps << endl;
    }
  }

}

