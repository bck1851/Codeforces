// https://codeforces.com/contest/2149/problem/C
#include <iostream> 
#include <vector>
#include <unordered_map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t, n, k;
    cin >> t;
    for(; t > 0; t--){
        cin >> n >> k;
        vector<int> A;
        unordered_map<int, int> cnt;
        for(int z = 0, elem = 0; z < n; z++){
            cin >> elem;
            A.push_back(elem);
            ++cnt[elem];
        }
        int num_k = cnt[k], x = k;
        for(const auto& [elem, freq]: cnt){
            if(elem < k) --x;
        }
        cout << max(num_k, x) << endl;
    }
}
