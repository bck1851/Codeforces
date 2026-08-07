// https://codeforces.com/contest/1831/problem/B
#include <iostream>


int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t,n,x;
    std::cin >> t;
    int A[200000], B[200000], C[400001];
    for(; t > 0; t--){
        std::cin >> n;
        for(int i = 0; i < n; i++){
            std::cin >> x;
            A[i] = x;
            C[x] = 0;
        }
        for(int i = 0; i < n; i++){
            std::cin >> x;
            B[i] = x;
            C[x] = 0;
        }
        int res = 1;
        for(int i = 0, cur = 0; i < n; i++){
            cur = (i > 0 && A[i] == A[i-1]) ? cur + 1: 1;
            C[A[i]] = std::max(C[A[i]], cur);
            res = std::max(res, cur);
        }
        for(int i = 0, cur = 0; i < n; i++){
            cur = (i > 0 && B[i] == B[i-1]) ? cur + 1: 1;
            res = std::max(res, cur + C[B[i]]);
        }
        std::cout << res << '\n';
    }

    return 0;
}
