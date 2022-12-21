#include <iostream>
#include <bitset>

using namespace std;

int value(char ch) {
    if (ch >= 'a') {
        return ch - 'a';
    }

    return ch - 'A' + 26;
}

int main() {
    string input;
    bitset<53> letters;

    int ans {};

    while (cin >> input) {
        for (int i {}; i < input.size() / 2; ++i) {
            char ch {input[i]};

            letters[value(ch)] = 1;
        }

        for (int i {int(input.size() / 2)}; i < input.size(); ++i) {
            char ch {input[i]};

            int val {value(ch)};

            if (letters[val]) {
                ans += val + 1;
                
                break;
            }
        }

        letters.reset();
    }

    cout << ans << '\n';

    return 0;
}
