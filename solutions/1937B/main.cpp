//https://codeforces.com/contest/1937/problem/B

#include <iostream>
#include <string>
#include <vector>
#include <cstring>

std::string a,b;
long long memo[2][200000];

long long f(int r, int c, std::vector<char>& res, int n){
    if(r == 1 && c == n-1) return 1;
    if(r > 1 || c == n)    return 0;
    if(memo[r][c] != -1)   return memo[r][c];
    std::string& s = (r == 0) ? a:b;
    int idx = r + c;
    if(s[c] != res[idx])   return 0;
    return memo[r][c] = (f(r+1,c,res,n) + f(r,c+1,res,n)); 
}

int main() 
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t,n;
    std::cin >> t;
    while(t--){
        std::cin >> n;
        std::cin >> a;
        std::cin >> b;
        for(int i = 0; i < 2; i++){
            memset(memo[i], -1, sizeof(long long)*n);
        }
        std::vector<char> res;
        res.reserve(n+1);
        res.push_back(a[0]);
        int j = 1;
        while(j < n && a[j] <= b[j-1]){
            res.push_back(a[j++]);
        }
        if(j == n) res.push_back(b[n-1]);
        else{
            for(int i = j-1; i < n; i++) res.push_back(b[i]);
        }
        for(char ch: res) std::cout << ch;
        std::cout << '\n';
        std::cout << f(0,0,res,n) << '\n';
    }
    return 0;
}
