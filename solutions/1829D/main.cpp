// https://codeforces.com/contest/1829/problem/D
#include <iostream>
#include <unordered_map>
#include <cstdint>

long long getHash(int a, int b) {
    return ((long long)(a)<<32) | b;
}

bool f(int cur, int tar, std::unordered_map<long long ,bool>& memo){
    if(cur <= tar) return cur == tar;
    long long hash = getHash(cur, tar);
    if(memo.count(hash)) return memo[hash];
    bool val = cur %3 ? false: f(cur/3, tar, memo) | f(2*cur/3, tar, memo);
    return memo[hash] = val;
}

int main() 
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::unordered_map<long long, bool> memo;
    int t,n,m;
    std::cin >> t;
    for(; t > 0; t--){
        std::cin >> n;
        std::cin >> m;
        std::cout << (f(n, m, memo) ? "YES":"NO") << "\n";
    }
    return 0;
}
