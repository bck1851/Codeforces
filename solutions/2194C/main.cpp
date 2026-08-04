//https://codeforces.com/contest/2194/problem/C
#include <iostream> 
#include <string>

int mask[50001];
int bit_mask = (1<<26)-1;

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t,n,k;
    std::string s;
    std::cin >> t;
    while(t--){
        std::cin >> n;
        std::cin >> k;
        for(int i = 0; i < n; i++){
            mask[i] = 0;
        }
        for(int i = 0; i < k; i++){
            std::cin >> s;
            for(int j = 0; j < n; j++){
                int bit = s[j] - 'a';
                mask[j] |= 1 << bit;
            }
        }
        int res = n;
        for(int i = 1; i < n; i++){
            if(n%i) continue;
            int ok = 1;
            for(int start = 0; start < i; start++){
                int t = bit_mask;
                for(int j = start; j < n; j += i){
                    t &= mask[j];
                }
                if(t == 0){
                    ok = false;
                    break;
                }
            }
            if(ok){
                res = i;
                break;
            }
        }
        std::string str(n, '$');
        for(int start = 0; start < res; start++){
            int t = bit_mask;
            for(int i = start; i < n; i += res){
                t &= mask[i];
            }
            char ch;
            for(int bit = 0; bit < 26; bit++){
                if(((t>>bit)&1) == 0) continue;
                ch = char(bit + 97);
                break;
            }
            for(int j = start; j < n; j += res){
                str[j] = ch;
            }
        }
        std::cout << str << '\n';
    }
}
