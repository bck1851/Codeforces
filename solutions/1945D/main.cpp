// https://codeforces.com/contest/1945/problem/D

#pragma GCC target("avx2")
#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")
#include <iostream>
#include <climits>
#include <cstring>

long long a[200000], b[200000], memo[200000];

long long f(int idx, int m){
    if(idx < 0) return (long long)1e15;
    if(memo[idx] != -1) return memo[idx];
    long long res = f(idx-1, m) + b[idx];
    res = std::min(res, a[idx] + (idx < m ? 0: f(idx-1,m)));
    return memo[idx] = res;
}

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t,n,m,x;
    std::cin >> t;
    while(t--){
        std::cin >> n;
        memset(memo, -1, sizeof(long long)*n);
        std::cin >> m;
        for(int i = 0; i < n; i++){
            std::cin >> x;
            a[i] = x;
        }
        for(int i = 0; i < n; i++){
            std::cin >> x;
            b[i] = x;
        }
        std::cout << f(n-1,m) << '\n';
    }
}
