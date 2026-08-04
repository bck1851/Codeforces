// https://codeforces.com/contest/1982/problem/C

#include <iostream>
#include <vector>
#include <algorithm>

std::vector<int> memo(100000, -1);

long long f(int idx, int n, int l, int r, std::vector<long long>& arr){
    if(idx >= n) return 0;
    if(memo[idx] != -1) return memo[idx];
    long long res = f(idx+1, n, l, r, arr), pre = (idx == 0) ? 0: arr[idx-1];
    int left = lower_bound(arr.begin() + idx, arr.end(), pre + l) - arr.begin();
    int right = (upper_bound(arr.begin() + idx, arr.end(), pre + r) - arr.begin()) - 1;
    if(right >= left) res = std::max(res, 1 + f(left + 1, n, l, r, arr));
    return memo[idx] = res;
}

int main() 
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t,n,l,r,x;
    std::cin >> t;
    while(t--){
        std::cin >> n;
        std::cin >> l;
        std::cin >> r;
        std::vector<long long> arr;
        for(int i = 0; i < n; i++){
            std::cin >> x;
            memo[i] = -1;
            arr.push_back(x);
            if(i > 0) arr[i] += arr[i-1];
        }
        std::cout << f(0,n,l,r, arr) << '\n';
    }
    return 0;
}
