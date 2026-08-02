//https://codeforces.com/contest/1866/problem/B
#include <iostream>
#include <unordered_map>
#include <chrono>
#include <vector>

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

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t,n,m,x;
    t = 1;
    while(t--){ 
        std::cin >> n;
        std::unordered_map<int, int, customhash> X,Y;
        std::vector<int> xArr, yArr;
        for(int i = 0; i < n; i++){
            std::cin >> x;
            xArr.push_back(x);
        }
        for(int i = 0; i < n; i++){
            std::cin >> x;
            X[xArr[i]] = x;
        }
        std::cin >> m;
        for(int i = 0; i < m; i++){
            std::cin >> x;
            yArr.push_back(x);
        }
        for(int i = 0; i < m; i++){
            std::cin >> x;
            Y[yArr[i]] = x;
        }
        long long res = 1;
        int mod = 998244353, ok = 1;
        for(auto& [k,v]: Y){
            if(X[k] < v){
                ok = 0;
                break;
            }
        }
        if(!ok){
            std::cout << 0;
            continue;
        }
        for(auto& [k,v]: X){
            int v2 = Y[k];
            if(v != v2) res = res*2%mod;
        }
        std::cout << res << '\n';
    }
}
