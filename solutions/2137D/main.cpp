// https://codeforces.com/contest/2137/problem/D

#include <iostream>
#include <unordered_map>
#include <vector>

int arr[200000];

int main() 
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t,n,x;
    std::cin >> t;
    while(t--){
        std::cin >> n;
        std::unordered_map<int, std::vector<int>> d;
        for(int i = 0; i < n; i++){
            std::cin >> x;
            d[x].push_back(i);
        }
        int ok = 1, cur = 1;
        for(auto& [k,v]: d){
            if(v.size()%k){
                ok = 0;
                break;
            }
            int count = 0;
            for(int idx: v){
                arr[idx] = cur;
                ++count;
                if(count == k){
                    count = 0;
                    ++cur;
                }
            }
        }
        if(ok == 0){
            std::cout << -1 << '\n';
            continue;
        }
        for(int i = 0; i < n; i++){
            std::cout << arr[i] << ' ';
        }
        std::cout << '\n';
    }
    return 0;
}
