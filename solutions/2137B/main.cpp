// https://codeforces.com/contest/2137/problem/B
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int t, n;
    cin >> t;
    vector<int> A(200001, 0);
    for(; t > 0; t--){
        cin >> n;
        for(int i = 0, j; i < n; i++){
            cin >> j;
            A[i] = j;
        }
        for(int i = 0; i < n; i++){
            cout << n + 1 - A[i] << ' ';
        }
        cout << '\n';
    }

    return 0;
}
