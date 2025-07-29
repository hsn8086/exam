#include <bits/stdc++.h>
#define int long long
using namespace std;
int sg[101][61][41],book[100005];
void dfs(int a,int b,int c){
    if(a==0&&b==0&&c==0)return;
    int cnt=0;
    for(int i=1;i<=min(3ll,a);i++)
        book[++cnt]=sg[a-i][b][c];
    if(b)book[++cnt]=sg[a+1][b-1][c];
    if(b){
        book[++cnt]=sg[a][b-1][c];
        if(a)book[++cnt]=sg[a-1][b-1][c];
    }
    if(b>1)book[++cnt]=sg[a+1][b-2][c];
    if(c){
        book[++cnt]=sg[a+1][b][c-1];
        book[++cnt]=sg[a][b+1][c-1];
        book[++cnt]=sg[a+1][b+1][c-1];
    }
    sort(book+1,book+1+cnt);
    unique(book+1,book+1+cnt);
    for(int i=1;i<=cnt+10;i++)
        if(book[i]!=i-1||i>cnt){
            sg[a][b][c]=i-1;
            return;
        }
}
signed main()
{
    // for(int i=0;i<=60;i++)
    //     for(int j=0;j<=100;j++){
    //         dfs(j,i,0);
    //     }
    // for(int i=0;i<=40;i++)
    //     for(int j=0;j<=40;j++)
    //         for(int l=1;l<=40;l++)
    //             dfs(i,j,l);
    // for(int i=0;i<=40;i++)
    //     for(int j=0;j<=40;j++)
    //         for(int l=0;l<=40;l++)
    //             if(sg[i][j][l]==0)
    //                 cout<<i<<" "<<j<<" "<<l<<endl;
    int t;cin>>t;
    while(t--){
        int a,b,c,p=0;cin>>a>>b>>c;
        dfs(a, b, c);
        cout<<sg[a][b][c]<<endl;
        // if((a/2)%2==b%2&&a%2==0)p=1;
        // if(p)cout<<"Bob"<<'\n';
        // else cout<<"Alice"<<'\n';
    }
            
    return 0;
}
