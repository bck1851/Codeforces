//http://codeforces.com/contest/1878/problem/E
#include <iostream>
#include <vector>
#include <utility>

int arr[200000][32], nums[200000];

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t,n,x,q,l,k;
    std::cin >> t;
    while(t--){
        std::cin >> n;
        for(int i = 0; i < n; i++){
            std::cin >> x;
            nums[i] = x;
            for(int j = 0; j < 32; j++){
                int bit = (x >> j)&1;
                arr[i][j] = bit;
                if(i > 0) arr[i][j] += arr[i-1][j];
            }
        }
        std::cin >> q;
        std::vector<std::pair<int,int>> Q;
        Q.reserve(q);
        for(int i = 0; i < q; i++){
            std::cin >> l;
            std::cin >> k;
            Q.push_back(std::pair<int,int>{l-1,k});
        }
        std::vector<int> res;
        res.reserve(q);
        for(auto& [l,k]: Q){
            if(nums[l] < k) res.push_back(-1);
            else{
                int lo = l, hi = n-1, ans = l;
                while(lo  <= hi){
                    int mid = (lo + hi)/2, cur = 0;
                    for(int i = 0; i < 32; i++){
                        int bits = arr[mid][i] - (l == 0 ? 0 : arr[l-1][i]);
                        if(bits == (mid - l + 1)) cur += 1<<i;
                    }
                    if(cur >= k){
                        lo = mid + 1;
                        ans = mid;
                    }
                    else hi = mid-1; 
                }
                res.push_back(ans+1);
            } 
        }
        for(int num: res) std::cout << num << " ";
        std::cout << '\n';
    }
}
