#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main() {
    string aux;

    vector<int> ans;

    int curr {};

    while (getline(cin, aux)) {
        if (aux == "") {
            ans.push_back(-curr);

            curr = 0;
        } else {
            curr += stoi(aux);
        }
    }

    ans.push_back(-curr);

    sort(ans.begin(), ans.end());

    cout << (ans[0] + ans[1] + ans[2]) * -1 << '\n';

    return 0;
}
