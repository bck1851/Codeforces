// https://codeforces.com/contest/1566/problem/C
#include <string>
#include <iostream>

int memo[100000][4];

int f_miss(int mask){
    int miss = 2;
    for(int i = 0; i < 2; i++){
        if(!((mask >> i)&1)){
            miss = i;
            break;
        }
    }
    return miss;
}

int f(std::string& a, std::string& b, int idx, int mask){
    if(idx == a.length()){
        return f_miss(mask);
    }
    if(memo[idx][mask] != -1){
        return memo[idx][mask];
    }
    int x = a[idx] - '0', y = b[idx] - '0';
    int new_mask = mask | (1<<x) | (1<<y);
    int miss = f_miss(new_mask);
    int res = std::max(miss + f(a,b,idx+1,0), f(a,b,idx+1,new_mask));
    return memo[idx][mask] = res;
}

int main() 
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t,n;
    std::cin >> t;
    std::string A, B;
    for(; t > 0; t--){
        std::cin >> n;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < 4; j++){
                memo[i][j] = -1;
                }
        }
        std::cin >> A;
        std::cin >> B;
        std::cout << f(A,B,0,0) << '\n';
    }
}
