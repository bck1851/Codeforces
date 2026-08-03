//https://codeforces.com/contest/2158/problem/C
#include <iostream>
#include <climits>

long long a[200000], b[200000], memo[200000][2], visited[200000][2];

long long f(int idx, int rem, int n){
    if(idx == n) return 0;
    if(visited[idx][rem]) return memo[idx][rem];
    long long stop = a[idx], go = stop + f(idx+1, rem, n), ans = std::max(go, stop);
    if(rem > 0){
        long long stop2 = a[idx] + b[idx], go2 = stop2 + f(idx+1, rem-1, n);
        ans = std::max(ans, std::max(stop2, go2));
    }
    visited[idx][rem] = 1;
    return memo[idx][rem] = ans;
}

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t,n,k,x;
    std::cin >> t;
    while(t--){
        std::cin >> n;
        std::cin >> k;
        for(int i = 0; i < n; i++){
            std::cin >> x;
            a[i] = x;
            visited[i][0] = 0; visited[i][1] = 0;
        }
        for(int i = 0; i < n; i++){
            std::cin >> x;
            b[i] = x;
        }
        long long res = LLONG_MIN;
        for(int i = 0; i < n; i++){
            res = std::max(res, f(i, k&1, n));
        }
        std::cout << res << '\n';
    }
}
