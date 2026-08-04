//https://codeforces.com/contest/1999/problem/E
#include <iostream>
#include <cstring>

int memo_f[200005], memo_h[200005];

int f(int num){
    if(memo_f[num] != -1) return memo_f[num];
    int res = 0;
    while(num > 0){
        ++res;
        num /= 3;
    }
    return memo_f[num] = res;
}

int h(int x){
    if(x == 0) return 0;
    if(memo_h[x] != -1) return memo_h[x];
    return memo_h[x] = f(x) + h(x-1);
}

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t,l,r;
    std::cin >> t;
    memset(memo_f, -1, sizeof(memo_f));
    memset(memo_h, -1, sizeof(memo_h));
    while(t--){
        std::cin >> l;
        std::cin >> r;
        std::cout << h(r) - h(l) + 2*f(l) << '\n';
    }
}
