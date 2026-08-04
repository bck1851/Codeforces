// https://codeforces.com/contest/2144/problem/C

#include <iostream> 

long long A[1000], B[1000], memo[1000][2], mod = 998244353;

long long f(int idx, int pre, int n){
    if(idx == n)        return 1;
    if(memo[idx][pre] != -1) return memo[idx][pre];
    int res = 0;
    if(idx == 0) res += f(idx+1, 0, n) + f(idx+1, 1, n);
    if(idx > 0){
        int pa = pre ? B[idx-1] : A[idx-1];
        int pb = pre ? A[idx-1] : B[idx-1];
        if(A[idx] >= pa && B[idx] >= pb) res += f(idx+1, 0, n);
        if(A[idx] >= pb && B[idx] >= pa) res += f(idx+1, 1, n);
    }
    return memo[idx][pre] = res%mod;
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
            A[i] = x;
            memo[i][0] = -1;
            memo[i][1] = -1;
        }
        for(int i = 0; i < n; i++){
            std::cin >> x;
            B[i] = x;
        }
        std::cout << f(0,0,n) << '\n';
    }
}
