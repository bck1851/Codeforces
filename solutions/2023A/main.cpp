// https://codeforces.com/contest/2023/problem/A

#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <utility>

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t,n,x;
    std::cin >> t;
    while(t--){
        std::vector<int> a, sa;
        std::vector<std::pair<int,int>> groups;
        std::cin >> n;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < 2; j++){
                std::cin >> x;
                a.push_back(x);
                sa.push_back(x);
            }
        }
        sort(sa.begin(), sa.end());
        std::unordered_map<int,int> idx_map;
        for(int i = 0; i < 2*n; i++){
            idx_map[sa[i]] = i;
        }
        for(int i = 0; i < n; i++){
            int x = a[2*i], y = a[2*i+1], tot = 2*n - idx_map[x] + 2*n - idx_map[y] - 2;
            groups.push_back({-tot, i});
        }
        std::sort(groups.begin(), groups.end());
        for(int i = 0; i < n; i++){
            int group = groups[i].second;
            std::cout << a[group*2] << " " << a[group*2+1] << " ";
        }
        std::cout << '\n';
    }
}
