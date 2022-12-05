#include <iostream>
#include <bitset>

using namespace std;

int main() {
    string input;
    bitset<53> letters;

    int ans {};

    while (cin >> input) {
        for (int i {}; i < input.size() / 2; ++i) {
            char ch {input[i]};
            int shift {ch >= 'a' ? 1 : 27};
            int pos {};

            if (ch >= 'a') {
                pos = ch - 'a';
            } else {
                pos = ch - 'A';
            }

            letters[pos + shift] = 1;
        }

        for (int i {int(input.size() / 2)}; i < input.size(); ++i) {
            char ch {input[i]};
            int shift {ch >= 'a' ? 1 : 27};
            int pos {};

            if (ch >= 'a') {
                pos = ch - 'a';
            } else {
                pos = ch - 'A';
            }

            pos += shift;

            if (letters[pos]) {
                ans += pos;
                
                break;
            }
        }

        letters.reset();
    }

    cout << ans << '\n';

    return 0;
}