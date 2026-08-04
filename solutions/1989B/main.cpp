// https://codeforces.com/contest/1989/problem/B

#include <iostream>
#include <string>

int memo[100][100];

int f(std::string& a, std::string& b, int i, int j){
    if(i == a.length() || j == b.length()) return  b.length() - j;
    if(memo[i][j] != -1) return memo[i][j];
    int res;
    if(a[i] == b[j]) res = f(a, b, i+1, j+1);
    else res = f(a,b,i+1,j);
    return memo[i][j] = res;
}

int main() 
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t;
    std::string a,b;
    std::cin >> t;
    while(t--){
        std::cin >> a;
        std::cin >> b;
        for(int i = 0; i < a.length(); i++){
            for(int j = 0; j < b.length(); j++){
                memo[i][j] = -1;
            }
        }
        int t = b.length();
        for(int i = 0; i < b.length(); i++){
            t = std::min(t, i + f(a,b,0,i));
        }
        std::cout << t + a.length() << '\n';
    }
    return 0;
}
