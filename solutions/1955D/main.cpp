//https://codeforces.com/contest/1955/problem/D
#include <iostream>
#include <unordered_map>
#include <chrono>

struct customhash {
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
int a[200000];

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t,n,m,k,x;
    std::cin >> t;
    while(t--){
        std::cin >> n;
        std::cin >> m;
        std::cin >> k;
        for(int i = 0; i < n; i++){
            std::cin >> x;
            a[i] = x;
        }
        std::unordered_map<int,int,customhash> cnt;
        for(int i = 0; i < m; i++){
            std::cin >> x;
            cnt[x]++;
        }
        int res = 0, match = 0;
        for(int i = 0; i < n; i++){
            int elem = a[i]; 
            if(--cnt[elem] >= 0) ++match;
            if(i >= m-1){
                if(match >= k) ++res;
                if(++cnt[a[i-m+1]] >= 1) --match;
            }   
        }
        std::cout << res << '\n';
    }
}
