// https://codeforces.com/contest/2114/problem/C
#include <iostream>
#include <vector>
using namespace std;

int h(int idx, int n, vector<int>& A, vector<int>& dp){
    if(idx >= n) return 0;
    if(dp[idx] != -1) return dp[idx];
    int res = max(1, h(idx+1, n, A, dp));
    int j = lower_bound(A.begin(), A.begin() + n, A[idx] + 2) - A.begin();
    if(j < n) res = max(res, 1 + h(j, n, A, dp));
    return dp[idx] = res;
}

int f(vector<int>& A, vector<int>& dp, int n){
    return h(0, n, A, dp);
}

int main() 
{
    int t,n;
    vector<int> A(200000, 0), dp(200000, -1);
    cin >> t;
    for(; t > 0; t--){
        cin >> n;
        for(int i = 0, num; i < n; i++){
            cin >> num;
            A[i] = num;
            dp[i] = -1;
        }
        cout << f(A, dp, n) << '\n';
    }
    return 0;
}
