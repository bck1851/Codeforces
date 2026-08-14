// https://codeforces.com/problemset/problem/1942/B
#include <iostream>
#include <set>

int arr[200005], res[200005];

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t, n, x;
    std::cin >> t;
    while (t--) {
        std::cin >> n;
        for (int i = 0; i < n; i++) {
            std::cin >> arr[i];
        }
        std::set<int> unused;
        for (int i = 0; i <= n; i++) {
            unused.insert(i);
        }
        int last = arr[0] == 1 ? 0 : -arr[0];
        int mex = (last == 0 ? 1 : 0);

        res[0] = last;
        if (last >= 0 && last <= n) {
            unused.erase(last);
        }

        for (int i = 1; i < n; i++) {
            int new_mex = *unused.lower_bound(mex + 1);
            int elem = new_mex - arr[i];
            if (elem == mex) {
                res[i] = elem;

                if (elem >= 0 && elem <= n) {
                    unused.erase(elem);
                }
                mex = new_mex;
            }
            else {
                elem = mex - arr[i];
                res[i] = elem;
                if (elem >= 0 && elem <= n) {
                    unused.erase(elem);
                }
            }
        }

        for (int i = 0; i < n; i++) {
            std::cout << res[i] << ' ';
        }
        std::cout << '\n';
    }

    return 0;
}
