#include <iostream>
#include <cstring>

using namespace std;

int letters[53];
int curr_letters[53];

int value(char ch) {
    if (ch >= 'a') {
        return ch - 'a';
    }

    return ch - 'A' + 26;
}

void iterate(string &a) {
    for (int i {}; i < a.size(); ++i) {
        char ch {a[i]};

        curr_letters[value(ch)] = 1;
    }

    for (int i {}; i < 53; ++i) {
        letters[i] += curr_letters[i];
    }

    memset(curr_letters, 0, sizeof(curr_letters));
}

int main() {
    string first_elf, second_elf, third_elf;

    int ans {};

    while (cin >> first_elf >> second_elf >> third_elf) {
        iterate(first_elf);
        iterate(second_elf);
        iterate(third_elf);

        for (int i {}; i < 53; ++i) {
            if (letters[i] == 3) {
                ans += i + 1;
            }

            letters[i] = 0;
        }
    }

    cout << ans << '\n';

    return 0;
}
