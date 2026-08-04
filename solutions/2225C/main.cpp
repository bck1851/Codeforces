// https://codeforces.com/contest/2225/problem/C

#include <iostream>
#include <string>

int memo[200000];
std::string a,b;


int f(int idx, int n){
    if(idx >= n){
        return 0;
    }
    if(memo[idx] != -1){
        return memo[idx];
    }
    int res = (a[idx] == b[idx] ? 0:1) + f(idx+1, n);
    if(idx+1 < n){
        int x = (a[idx] == a[idx+1]) ? 0:1;
        int y = (b[idx] == b[idx+1]) ? 0:1;
        res = std::min(res, x + y + f(idx+2,n));
    }
    return memo[idx] = res;
}

int main() 
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t,n;
    std::cin >> t;
    for(; t > 0; t--){
        std::cin >> n;
        std::cin >> a;
        std::cin >> b;
        for(int i = 0; i < n; i++){
            memo[i] = -1;
        }
        std::cout << f(0,n) << '\n'; 
    }
    return 0;
}
