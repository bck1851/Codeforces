// https://codeforces.com/problemset/problem/1974/C
#include <iostream>
#include <unordered_map> 
#include <chrono>
#include <string>
 
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
 
std::string a[200000];
long long mod = 1e9 + 7;
 
long long hash(std::string& s){
    long long res1 = 0, res2 = 0, t = 1;
    for(char ch: s){
        int val = (ch == '-' ? 1: ch == '$' ? 2: ch - '0' + 3);
        res1 = res1*29 + val;
        if(res1 >= mod) res1 -= mod ;
        res2 = res2 + val*t;
        if(res2 >= mod) res2 -= mod;
        t = t*29;
        if(t >= mod) t -= mod;
    }
    return res1 | (res2 << 32);
}
 
int main() 
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t,n;
    std::string x;
    std::cin >> t;
    while(t--){
        std::cin >> n;
        for(int i = 0; i < n; i++){
            std::cin >> x;
            a[i] = x;
        }
        std::unordered_map<long long,int, custom_hash> cnt;
        long long res = 0;
        for(int i = 0; i < n-2; i++){
            std::string 
                x = a[i] + "-" + a[i+1] + "-" + a[i+2],
                y = "$-" + a[i+1] + "-" + a[i+2],
                z = a[i] + "-$" + "-" + a[i+2],
                p = a[i] + "-" + a[i+1] + "-$";
            long long hx = hash(x), hy = hash(y), hz = hash(z), hp = hash(p);
            res += cnt[hy] + cnt[hz] + cnt[hp] - 3*cnt[hx];
            ++cnt[hx];
            ++cnt[hy];
            ++cnt[hz];
            ++cnt[hp];
        }
        std::cout << res << '\n';
    }
}
