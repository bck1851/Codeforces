// https://codeforces.com/contest/1469/problem/A
#include <iostream>
#include <string>


int memo[101][201];

int f(std::string& s, int idx, int j){
    if(j < 0){
        return 0;
    }
    if(idx == s.length()){
        return j == 0;
    }
    if(memo[idx][j+100] != -1){
        return memo[idx][j+100];
    }
    int res = 0;
    if(s[idx] == '?'){
        res = f(s, idx+1, j+1) | f(s, idx+1, j-1);
    }
    else{
        int nj = j + (s[idx] == '(' ? 1:-1);
        res = f(s, idx+1, nj);
    }
    return memo[idx][j+100] = res;
}

int main() 
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t;
    std::string s;
    std::cin >> t;
    for(; t > 0; t--){
        std::cin >> s;
        for(int i = 0; i < s.length(); i++){
            for(int j = 0; j < 2*s.length(); j++){
                memo[i][100 + j] = -1;
            }
        }
        std::cout << (f(s,0,0) ? "YES":"NO") << '\n';

    }
    return 0;
}
