// https://codeforces.com/contest/2106/problem/C
#include <iostream>
using namespace std;

int main() 
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t,n,k,x;
    std::cin >> t;
    int A[200000], B[200000];
    for(; t > 0; t--){
        std::cin >> n;
        std::cin >> k;
        int check = 1;
        int tot = -1, tot_same = 1, mn = int(1e9), mx = -1;
        for(int i = 0; i < n; i++){
            std::cin >> x;
            A[i] = x;
            mn = min(mn, x);
            mx = max(mx, x);
        }
        for(int i = 0; i < n; i++){
            std::cin >> x;
            B[i] = x;
            if(x != -1){
                check = 0;
                if(tot != -1 && A[i] + B[i] != tot) tot_same = 0;
                tot = A[i] + B[i];
            }
        }
        int res;
        if(check){
            res = std::max(res, mn + k - mx + 1);
        }
        else if(tot_same != 0){
            int ok = 1;
            for(int i = 0; i < n; i++){
                if(tot - A[i] < 0 || tot - A[i] > k) ok = 0;
            }
            res = ok;
        }
        std::cout << res << "\n";

    }
    return 0;
}
