// https://codeforces.com/contest/2178/problem/C
#include <iostream>
#include <climits>

long long arr[200000], memo[200000][2], visited[200000][2], acc[200000];

long long h(int idx, int go, int n){
    if(idx == n){
        return go == 0 ? 0: INT_MIN;
    }
    if(visited[idx][go]){
        return memo[idx][go];
    }
    long long res;
    if(go == 0){
        long long acc_val = acc[n-1] - acc[idx];
        res = std::max(-acc_val, arr[idx] + h(idx+1, 1, n));
    }
    else{
        res = std::max(h(idx, 0, n), -arr[idx] + h(idx+1, 1, n));
    }
    visited[idx][go] = 1;
    return memo[idx][go] = res;
}

int main() 
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t,n,x;
    std::cin >> t;
    while(t--){
        std::cin >> n;
        for(int i = 0; i < n; i++){
            std::cin >> x;
            arr[i] = x;
            acc[i] = x;
            visited[i][0] = 0;
            visited[i][1] = 0;
        }
        for(int i = 0; i < n; i++){
            acc[i] += acc[i-1];
        }
        std::cout << h(0,0,n) << '\n';
    }
    
    return 0;
}
