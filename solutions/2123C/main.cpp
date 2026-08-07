// https://codeforces.com/contest/2123/problem/C
#include <iostream>
#include <vector> 
#include <unordered_set>
using namespace std;

int main() 
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,t;
    cin >> t;
    vector<int> A(200000, 0), rA(200000, 0);
    for(; t > 0; t--){
        cin >> n; 
        int tmp;
        for(int i = 0; i < n; i++){
            cin >> tmp; 
            A[i] = tmp; 
        }
        int mx = 0;
        for(int i = n-1; i >= 0; i--){
            mx = max(mx, A[i]);
            rA[i] = mx;
        }
        int mn = 1000000;
        unordered_set<int> possible;
        for(int i = 0; i < n; i++){
            mn = min(mn, A[i]);
            if(i + 1 < n){
                int s = rA[i+1];
                possible.insert(min(s, mn));
                possible.insert(max(s, mn));
            }
        }
        string res = "";
        for(int i = 0; i < n; i++){
            res += possible.count(A[i]) ? "1":"0";
        }
        cout << res << '\n';
    }
    return 0;
}
