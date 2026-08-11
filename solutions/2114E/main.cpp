// https://codeforces.com/problemset/problem/2114/E
#include <iostream>
#include <vector>
 
int arr[200005], par[200005];
long long memo[200005][2];
 
void dfs(int node, int pre, std::vector<std::vector<int>>& tree){
    par[node] = pre;
    for(int nxt: tree[node]){
        if(nxt == pre) continue;
        dfs(nxt, node, tree);
    }
}
 
long long dp(int node, int factor){
    if(node == 0) return 0LL;
    int f_idx = factor == -1 ? 0:1;
    if(memo[node][f_idx] != -1) return memo[node][f_idx];
    long long res = arr[node]*factor + std::max(0LL, dp(par[node], -factor));
    return memo[node][f_idx] = res;
}
 
int main() 
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t,n,u,v,x;
    std::cin >> t;
    while(t--){
        std::cin >> n;
        for(int i = 0; i < n; i++){
            std::cin >> x;
            arr[i+1] = x;
            memo[i+1][0] = -1; memo[i+1][1] = -1;
        }
        std::vector<std::vector<int>> tree(n+1, std::vector<int>());
        for(int i = 0; i < n - 1; i++){
            std::cin >> u;
            std::cin >> v;
            tree[u].push_back(v);
            tree[v].push_back(u);
        }
        dfs(1, 0, tree);
        std::vector<long long> res;
        for(int i = 1; i <= n; i++){
            res.push_back(dp(i, 1));
        }
        for(long long i: res) std::cout << i << " ";
        std::cout << '\n';
    }
    return 0;
}
