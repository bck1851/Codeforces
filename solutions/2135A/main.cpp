// https://codeforces.com/contest/2135/problem/A

#include <iostream>
#include <vector>
#include <algorithm>

int memo[200000];

int f(std::vector<std::vector<int>>& A, std::vector<int>& arr, int idx, int n){
    if(idx >= n) return 0;
    if(memo[idx] != -1) return memo[idx];
    int elem = arr[idx];
    int j = std::lower_bound(A[elem].begin(), A[elem].end(), idx) - A[elem].begin();
    int res = f(A, arr, idx+1, n);
    int tar = j + elem - 1;
    if(tar < A[elem].size()){
        int next_idx = A[elem][tar] + 1;
        res = std::max(res, elem + f(A, arr, next_idx, n));
    }
    return memo[idx] = res;
}

int main(){
    int t,n,x;
    std::cin >> t;
    for(; t > 0; t--){
        std::vector<std::vector<int>> A;
        std::cin >> n;
        std::vector<int> arr(n, -1);
        for(int i = 0; i < n; i++){
            std::cin >> x;
            while(A.size() < x + 1) A.push_back(std::vector<int>());
            A[x].push_back(i);
            arr[i] = x;
            memo[i] = -1;
        }
        std::cout << f(A, arr, 0, n) << '\n';
    }
}
