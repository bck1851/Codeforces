// https://codeforces.com/contest/2050/problem/C

#include <iostream>
#include <string>

int memo[100000][10], num[100000];

int f(int idx, int rem, std::string& s){
    if(idx == s.length()) return rem == 0 ? 1:0;
    if(memo[idx][rem] != -1) return memo[idx][rem];
    int elem = s[idx] - '0', res = f(idx+1, (rem + elem)%9, s);;
    if(elem*elem < 10) res |= f(idx+1, (rem + elem*elem)%9, s);
    return memo[idx][rem] = res;
}


int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t;
    std::string s;
    std::cin >> t;
    while(t--){
        std::cin >> s;
        for(int i = 0; i < s.length(); i++){
            for(int j = 0; j <= 9; j++){
                memo[i][j] = -1;
            }
        }
        std::cout << (f(0,0,s) ? "YES":"NO")<< '\n';
    }
}
