#include <iostream>
#include <string>

using namespace std;

int main() {
    string aux;

    int ans {}, curr {};

    while (getline(cin, aux)) {
        if (aux == "") {
            ans = max(ans, curr);

            curr = 0;
        } else {
            curr += stoi(aux);
        }
    }

    ans = max(ans, curr);

    cout << ans << '\n';

    return 0;
}
