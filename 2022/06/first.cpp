#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
    string s;

    cin >> s;

    unordered_map<char, int> letters;
    int p1 {}, p2 {}, current {};

    while (p1 < s.size() && p2 < s.size()) {
        char ch {s[p2++]};

        ++letters[ch];
        ++current;

        if (letters[ch] != 1) {
            while (letters[ch] != 1) {
                char current_ch {s[p1++]};

                --letters[current_ch];
                --current;
            }
        }

        if (current == 4) {
            break;
        }
    }

    cout << p2 << '\n';

    return 0;
}