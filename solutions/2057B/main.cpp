// https://codeforces.com/contest/2057/problem/B
#include <iostream>
#include <unordered_map>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int main(){
    int t, n, k, x;
    cin >> t;
    vector<int> A(100000, 0), B(100000, 0);
    for(; t > 0; t--){
        cin >> n; 
        cin >> k;
        for(int i = 0; i < n; i++){
            cin >> x;
            A[i] = x;
        }
        sort(A.begin(), A.begin()+n);
        int j = 0;
        for(int i = 0; i < n;){
            int count = 0, start = A[i];
            while(i < n && A[i] == start){
                ++count;
                ++i;
            }
            B[j++] = count;
        }
        sort(B.begin(), B.begin() + j);
        int groups = 0;
        for(int i = 0; i < j; i++){
            if(B[i] <= k) k -= B[i];
            else ++groups;
        }
        cout << max(1, groups) << '\n';
    }
}
