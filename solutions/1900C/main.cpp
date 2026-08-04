//https://codeforces.com/contest/1900/problem/C

#include <iostream>
#include <string>
#include <cstring>

std::string s;
int left[300005], right[300005], memo[300005];

int f(int node, int n){
    if(left[node] == 0 && right[node] == 0) return 0;
    if(memo[node] != -1) return memo[node];
    int res = n+1;
    char cur = s[node-1];
    if(left[node] != 0) res = std::min(res, (cur == 'L' ? 0:1) + f(left[node],n));
    if(right[node] != 0) res = std::min(res,(cur == 'R' ? 0:1) + f(right[node],n));
    return memo[node] = res;
}

int main(){
    int t,n,l,r;
    std::cin >> t;
    while(t--){
        std::cin >> n;
        std::cin >> s;
        memset(memo, -1, sizeof(int)*(n+1));
        for(int i = 1; i <= n; i++){
            std::cin >> l;
            std::cin >> r;
            left[i] = l;
            right[i] = r;
        }
        std::cout << f(1,n) << '\n';
    }
}
