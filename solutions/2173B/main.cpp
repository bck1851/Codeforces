// https://codeforces.com/contest/2173/problem/B

#include <iostream>


long long A[100000], B[100000], memo[100000][2];

long long f(int idx, int turn){
    if(idx < 0){
        return 0LL;
    }
    if(memo[idx][turn] != -1){
        return memo[idx][turn];
    }
    long long res = 0, a = f(idx-1, 1), b = f(idx-1, 0);
    if(turn == 1){
        res = std::max(-A[idx] + std::max(a,b), B[idx] - std::min(a,b));
    }
    else{
        res = std::min(-A[idx] + std::min(a,b), B[idx] - std::max(a,b));
    }
    return memo[idx][turn] = res;
}

int main() 
{
    int t,n,x;
    std::cin >> t;
    for(; t > 0; t--){
        std::cin >> n;
        for(int i = 0; i < n; i++){
            std::cin >> x;
            A[i] = x;
            memo[i][0] = -1;
            memo[i][1] = -1;
        }
        for(int i = 0; i < n; i++){
            std::cin >> x;
            B[i] = x;
        }
        std::cout << f(n-1, 1) << '\n';
    }
}
