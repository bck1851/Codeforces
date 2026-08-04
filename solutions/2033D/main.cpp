// https://codeforces.com/contest/2033/problem/D

#pragma GCC optimize("O3")
#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>
#include <chrono>

struct custom_hash {
    static uint64_t splitmix64(uint64_t x) {
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }

    size_t operator()(uint64_t x) const {
        static const uint64_t FIXED_RANDOM = std::chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x + FIXED_RANDOM);
    }
};

int memo[100005];

int f(std::vector<long long>& arr, std::vector<int>& nxt_idx){
    int n = arr.size(), res = 0;
    for(int i = n - 1; i >= 0; i--){
        int cur = 0;
        if(i + 1 < n) cur = memo[i+1];
        int j = nxt_idx[i];
        if(j < arr.size()) cur = std::max(cur, 1 + memo[j]);
        memo[i] = cur;
        res = std::max(res, cur);
    }
    return res;
}

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    
    long long t, n, x;
    if (!(std::cin >> t)) return 0;
    
    while(t--){
        std::cin >> n;
        std::vector<long long> arr;
        arr.reserve(n + 1);
        arr.push_back(0LL);
        memo[0] = 0;
        
        for(int i = 0; i < n; i++){
            std::cin >> x;
            arr.push_back(arr.back() + x);
            memo[i+1] = 0;
        }
        
        std::unordered_map<long long, int, custom_hash> last_seen;
        last_seen.reserve(n); 
        
        std::vector<int> nxt_idx(arr.size(), 200000);
        for(int i = arr.size() - 1 ; i >= 0; i--){
            long long num = arr[i];
            if(last_seen.count(num)) nxt_idx[i] = last_seen[num];
            last_seen[num] = i;
        }
        
        std::cout << f(arr, nxt_idx) << '\n';
    }
    return 0;
}
