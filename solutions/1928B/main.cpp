// https://codeforces.com/contest/1928/problem/B
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() 
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t,n,x;
    std::cin >> t;
    while(t--){
        std::cin >> n;
        std::vector<int> A(n, -1);
        for(int i = 0; i < n; i++){
            std::cin >> x;
            A[i] = x;
        }
        sort(A.begin(), A.end());
        A.erase(std::unique(A.begin(), A.end()), A.end());
        int res = 0;
        for(int i = 0; i < A.size(); i++){
            int j = lower_bound(A.begin(), A.begin() + i, A[i] + 1 - n) - A.begin();
            res = std::max(res, i - j + 1);
        }
        std::cout << res << '\n';

    }
    return 0;
}
