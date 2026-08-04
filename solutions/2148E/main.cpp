// https://codeforces.com/contest/2148/problem/E

#include <iostream>
#include <unordered_map>
#include <vector>

std::vector<int> A(200000, 0);

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t,n,k,elem;
    std::cin >> t;
    while(t--){
        std::cin >> n;
        std::cin >> k;
        std::unordered_map<int,int> cur, cnt;
        for(int i = 0; i < n; i++){
            std::cin >> elem;
            A[i] = elem;
            cnt[elem]++;
        }
        if(n%k){
            std::cout << 0 << '\n';
            continue;
        }
        int ok = 1;
        for(auto& [key, val]: cnt){
            if(val%k){
                ok = 0;
                break;
            }
        }
        if(ok == 0){
            std::cout << 0 << '\n';
            continue;
        }   
        long long res = 0, left = 0;
        for(int i = 0; i < n; i++){
            cur[A[i]]++;
            while(cur[A[i]] > cnt[A[i]]/k){
                --cur[A[left++]];
            }
            //std::cout << i << "  " << left << std::endl;
            res += i - left + 1;
        }
        std::cout << res << '\n';
    }

    return 0;
}
