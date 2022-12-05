#include <iostream>

using namespace std;

int choice_result(string &a) {
    if (a == "X" || a == "A") {
        return 1;
    } else if (a == "Y" || a == "B") {
        return 2;
    } else {
        return 3;
    }
}

string which_choose(string &a, bool win) {
    if (a == "A") {
        return win ? "B" : "C";
    } else if (a == "B") {
        return win ? "C" : "A";
    }
    
    return win ? "A": "B";
}

int result(string &a, string &b) {
    if (b == "Y") {
        return 3 + choice_result(a);
    }

    string choice {which_choose(a, b != "X")};

    return choice_result(choice) + (b == "X" ? 0 : 6);
}

int main() {
    string op_move, my_move;

    int ans {};

    while (cin >> op_move >> my_move) {
        ans += result(op_move, my_move);
    }

    cout << ans << '\n';

    return 0;
}
