#include <iostream>
#include <cstring>

using namespace std;

int letters[53];
int curr_letters[53];

void iterate(string &a) {
    for (int i {}; i < a.size(); ++i) {
        char ch {a[i]};
        int shift {ch >= 'a' ? 1 : 27};
        int pos {};

        if (ch >= 'a') {
            pos = ch - 'a';
        } else {
            pos = ch - 'A';
        }

        curr_letters[pos + shift] = 1;
    }

    for (int i {1}; i < 53; ++i) {
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

        for (int i {1}; i < 53; ++i) {
            if (letters[i] == 3) {
                ans += i;
            }

            letters[i] = 0;
        }
    }

    cout << ans << '\n';

    return 0;
}