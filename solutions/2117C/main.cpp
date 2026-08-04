// https://codeforces.com/contest/2117/problem/C

#include <iostream>
#include <unordered_set>

int arr[200000];

int main() 
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t,n,x;
    std::cin >> t;
    while(t--){
        std::cin >> n;
        for(int i = 0; i < n; i++){
            std::cin >> x;
            arr[i] = x;
        }
        std::unordered_set<int> pre = {arr[0]}, cur = {};
        int res = 1;
        for(int i = 1; i < n; i++){
            int elem = arr[i];
            cur.insert(elem);
            if(pre.count(elem)){
                pre.erase(elem);
            }
            if(pre.empty()){
                ++res;
                pre = cur;
                cur = std::unordered_set<int>();
            }
        }
        std::cout << res << '\n';
    }
    return 0;
}
