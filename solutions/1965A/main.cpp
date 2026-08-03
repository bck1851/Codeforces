//https://codeforces.com/contest/1965/problem/A
#pragma GCC optimize("O3")
#include <vector>
#include <iostream>
#include <algorithm>
 
int memo[200000][2];
 
int f(int idx, int turn, std::vector<int>& A){
    if(idx == A.size()) return (turn == 1) ? 1:0;
    if(memo[idx][turn] != -1) return memo[idx][turn];
    int dif = A[idx] - A[idx-1], res;
    int a = f(idx+1, turn^1, A), b = f(idx+1, turn, A);
    res = (dif == 1) ? a: (turn == 0) ? (a|b): (a&b);
    return memo[idx][turn] = res;
}
 
int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t,n,x;
    std::cin >> t;
    while(t--){
        std::cin >> n;
        std::vector<int> A;
        A.reserve(n+1);
        A.push_back(0);
        for(int i = 0; i < n; i++){
            std::cin >> x;
            A.push_back(x);
        }
        for(int i = 0; i < A.size(); i++){
            memo[i][0] = -1;
            memo[i][1] = -1;
        }
        sort(A.begin(), A.end());
        A.erase(unique(A.begin(), A.end()), A.end());
        std::cout << (f(1, 0, A) ? "Alice": "Bob") << '\n';
    }
}
