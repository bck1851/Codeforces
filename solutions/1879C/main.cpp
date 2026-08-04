// https://codeforces.com/contest/1879/problem/C

#pragma GCC optimize ("O3")
#include <iostream>
#include <cstring> 
#include <string> 

using namespace std;
 
string s;
int precompute = 0;
long long factorial[200001], memo[200001][2], mod = 998244353;
int n;
 
void start(){
    factorial[0] = 1;
    for(int i = 1; i <= 200000; i++){
        factorial[i] = factorial[i-1]*i%mod;
    }
    precompute = 1;
}
 
long long f(int idx, int pre){
    if(idx == n) return ((1LL<<32));
    long long &mem = memo[idx][pre];
    if(mem != -1) return mem;
    long long res = f(idx+1, pre), c1 = res >> 32, l1 = res&0xFFFFFFFFLL;
    if((s[idx]-'0')^pre){
        long long res2 = f(idx+1, pre^1), c2 = res2 >> 32, l2 = 1 + (res2&0xFFFFFFFFLL);
        if(l2 > l1){
            c1 = c2;
            l1 = l2;
        }
        else if(l2 == l1){
            c1 += c2;
            if(c1 >= mod) c1 -= mod; 
        }
    }
    return mem = (c1<<32)|l1;
}
 
void h(){
    memset(memo, -1, n*sizeof(memo[0]));
    long long one = f(0, 0), c_one = one >> 32, l_one = one&0xFFFFFFFFLL;
    long long zero = f(0, 1), c_zero = zero >> 32, l_zero = zero&0xFFFFFFFFLL;
    long long l = 0, c = 0;
    if(l_zero == l_one){
        l = l_one;
        int removed = n - l;
        c = factorial[removed]*((c_one + c_zero)%mod);
    }
    else if(l_zero > l_one){
        l = l_zero;
        int removed = n - l;
        c = factorial[removed]*c_zero;
    }
    else{
        l = l_one;
        int removed = n - l;
        c = factorial[removed]*c_one;
    }
    c %= mod;
    cout << n - l << " " << c << '\n';
}
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if(!precompute) start();
    int t;
    cin >> t;
    while(t--){
        cin >> s;
        n = s.length();
        h();
    }
}
