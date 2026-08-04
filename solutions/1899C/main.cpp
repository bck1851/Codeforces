// https://codeforces.com/contest/1899/problem/C

#include <iostream>


long long memo[200000][2][2];
long long arr[200000];
long long mn = -1000000000;

long long f(int idx, int parity, int taken, int n){
    if(idx == n){
        return taken ? 0: mn;
    }
    if(memo[idx][parity][taken] != -1){
        return memo[idx][parity][taken];
    }
    long long stop = (taken ? 0:mn), go = arr[idx] + f(idx+1, parity^1, 1, n), res;
    if((std::abs(arr[idx])&1) != parity){
        res = stop;
    }
    else res = std::max(stop, go);
    return memo[idx][parity][taken] = res;
}

int main() 
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t,n,x;
    std::cin >> t;
    for(; t > 0; t--){
        std::cin >> n;
        for(int i = 0; i < n; i++){
            std::cin >> x;
            arr[i] = x;
            for(int j = 0; j < 2; j++){
                for(int x = 0; x < 2; x++){
                    memo[i][j][x] = -1;
                }
            }
        }
        long long res = mn;
        for(int i = 0; i < n; i++){
            res = std::max(res, f(i,0,0,n));
            res = std::max(res, f(i,1,0,n));
        }
        std::cout << res << '\n';
    }
    return 0;
}
