// https://codeforces.com/contest/1861/problem/B
#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool f(int idx, string& a, string& b, vector<int>& memo){
    if(idx == a.length()){
        return true;
    }
    if(memo[idx] != -1){
        return memo[idx];
    }
    int res = 0;
    char ca = a[idx], cb = b[idx];
    if(ca != cb){
        return res;
    } 
    res |= f(idx+1, a, b, memo);
    for(int j = idx+1; j < a.length(); j++){
        if(a[j] == ca && b[j] == cb){
            res |= f(j+1, a, b, memo);
        }
    }
    return memo[idx] = res;
}

int main() 
{
    int n;
    string a,b;
    cin >> n;
    vector<int> memo(5000, -1);
    for(; n > 0; n--){
        cin >> a;
        cin >> b;
        fill(memo.begin(), memo.begin() + a.length(), -1);
        bool res = f(0, a, b, memo);
        cout << (res ? "YES": "NO") << '\n';
    }
    return 0;
}
