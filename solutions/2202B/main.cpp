// https://codeforces.com/contest/2202/problem/B

#include <iostream>
#include <string>

int s[200000], memo[200000][2][2];

int f(int idx, int start, int end, int n){
    if(idx == n){
        return 1;
    }
    if(memo[idx][start][end] != -1){
        return memo[idx][start][end];
    }
    int res = 0;
    if(s[idx] == 2) res = f(idx+1, start^1, end, n) | f(idx+1, start, end^1, n);
    else{
        res |= (start == s[idx]) && f(idx+1, start^1, end, n);
        res |= (end == s[idx]) && f(idx+1, start, end^1, n);
    }
    return memo[idx][start][end] = res;
}

int main() 
{
    int t,n;
    char elem;
    std::string str;
    std::cin >> t;
    for(; t > 0; t--){
        std::cin >> n;
        std::cin >> str;
        for(int i = 0; i < n; i++){
            elem = str[i];
            s[i] = 2;
            if(elem == 'a' || elem == 'b') s[i] = elem - 'a';
            memo[i][0][0] = -1; memo[i][0][1] = -1;
            memo[i][1][0] = -1; memo[i][1][1] = -1;
        }
        std::cout << (f(0,0,(n-1)&1,n) ? "YES":"NO") << '\n';
    }
    return 0;
}
