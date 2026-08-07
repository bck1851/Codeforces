// https://codeforces.com/contest/1800/problem/B
#include <iostream>

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t, n, k;
    std::string s;
    std::cin >> t;
    for(; t > 0; t--){
        std::cin >> n;
        std::cin >> k;
        std::cin >> s; 
        int upper[26] = {}, lower[26] = {};
        for(int i = 0; i < n; i++){
            if(s[i] < 'a') upper[s[i] - 'A']++;
            else lower[s[i] - 'a']++;
        }
        int res = 0;
        for(int i = 0; i < 26; i++){
            int u = upper[i], l = lower[i], rem = (u > l) ? u-l:l-u;
            res += std::min(u, l);
            if(k){
                res += std::min(rem/2, k);
                k = std::max(0, k - rem/2);
            }
        }
        std::cout << res << '\n';
    }

    return 0;
}
