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

int result(string &a, string &b) {
    int choice_a {choice_result(a)}, choice_b {choice_result(b)}, diff {choice_b - choice_a};

    if (choice_a == choice_b) {
        return choice_b + 3;
    } else if (diff == -2 || diff == 1) {
        return choice_b + 6;
    }

    return choice_b;
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
