#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; 
    cin >> T;
    while(T--){
        int n,q;
        cin >> n >> q;
        vector<int> p(n+1), pos(n+1);
        for(int i=1;i<=n;i++){
            cin >> p[i];
            pos[p[i]] = i;
        }

        while(q--){
            int l,r,x;
            cin >> l >> r >> x;
            int px = pos[x];
            if(px<l || px>r){
                cout << -1 << " ";
                continue;
            }

            // 模拟二分查找的 m 序列
            int L=l, R=r;
            int cntL=0, cntR=0;
            int smallGood=0, largeGood=0;
            while(true){
                int m = (L+R)>>1;
                if(m==px) break;
                if(m<px){
                    cntL++;
                    if(p[m]<x) smallGood++;
                    L = m+1;
                }else{
                    cntR++;
                    if(p[m]>x) largeGood++;
                    R = m-1;
                }
            }

            // 不可能情况
            if(cntL > x-1 || cntR > n-x){
                cout << -1 << " ";
                continue;
            }
            int needL = cntL - smallGood;
            int needR = cntR - largeGood;
            int d = 2 * max(needL, needR);
            cout << d << " ";
        }
        cout << "\n";
    }
    return 0;
}
