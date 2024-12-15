#include <bits/stdc++.h>
#define lint long long
using namespace std;
int T;
lint n,k;
lint calc0(lint u){
    lint v=min(n,(u+k-1)/k*k);
    lint up=(u-1)/k+1;
    u+=(v-u)/up*up;
    return u;
}
lint calc1(lint u){
    lint v=0;
    while((u+k-1)/k>(v+k-1)/k){
        lint tmp=(u+k-1)/k-(v+k-1)/k;
        v=u;u+=tmp;
    }
    return u;
}
int main(){
    scanf("%d",&T);
    while(T--){
        scanf("%lld%lld",&n,&k);
        lint u=1;
        while(true){
            lint v=calc0(u);
            if(v<=n)u=v;
            v=calc1(u);
            if(v>n)break;
            u=v;
        }
        printf("%lld\n",u);
    }    
    return 0;
}