// https://codeforces.com/contest/1926/problem/D

#include <unordered_map>
#include <iostream>
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

int arr[200000];
int mask = (1<<31)-1;

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
        }
        int res = 0;
        std::unordered_map<int,int,custom_hash> cnt;
        for(int i = 0; i < n; i++){
            int elem = arr[i];
            if(cnt[elem^mask]){
                --cnt[elem^mask];
            }
            else{
                ++res;
                ++cnt[elem];
            }
        }
        std::cout << res << '\n';
    }
}
