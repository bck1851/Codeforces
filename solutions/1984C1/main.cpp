// https://codeforces.com/contest/1984/problem/C1

#include <iostream>
#include <vector>
#include <utility>


std::vector<long long> arr(200000, -1);
std::vector<std::pair<long long,long long>> memo(200000, std::pair<long long, long long>());
std::vector<int> visited(200000, -1);

std::pair<long long, long long> f(int idx, int n){
    if(idx == -1)          return std::pair<long long, long long>{0LL,0LL};
    if(visited[idx] != -1) return memo[idx];
    long long mx = -1e14, mn = 1e14;
    std::pair<long long, long long> pre = f(idx-1, n);
    for(long long a: {pre.first, pre.second}){
        mx = std::max(mx, std::max(arr[idx] + a, std::abs(-arr[idx] - a)));
        mn = std::min(mn, std::min(arr[idx] + a, std::abs(-arr[idx] - a)));
    }
    visited[idx] = 1;
    return memo[idx] = std::pair<long long, long long>{mn, mx}; 
}

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t,n,x;
    std::cin >> t;
    while(t--){
        std::cin >> n;
        for(int i = 0; i < n; i++){
            std::cin >> x;
            arr[i] = x;
            visited[i] = -1;
        }
        std::cout << f(n-1, n).second << '\n';
    }
}
