#include<bits/stdc++.h>
#define int long long
using namespace std;
void solve()
{
    int n;cin>>n;vector<int>a(n),b(n);int last1=0,last2=0,ans1=0,last3=0,last4=0,ans2=0;
    for(int i=0;i<n;i++)cin>>a[i];
    for(int i=0;i<n;i++)cin>>b[i];
    for(int i=0;i<n;i++)
    {
        if(a[i]==b[i])
        last1=max(last1,i+1);
    }
    map<int,int>mp1,mp2;
    for(int i=n-1;i>=0;i--)
    {
        if(mp1[a[i]]&&(mp1[a[i]]-i)%2)
        {
            last2=max(last2,i+1);
        }
        if(mp2[a[i]]&&(mp2[a[i]]-i)%2==0)
        {
            last2=max(last2,i+1);
        }
        if(mp1[b[i]]&&(mp1[b[i]]-i)%2==0)
        {
            last2=max(last2,i+1);
        }
        if(mp2[b[i]]&&(mp2[b[i]]-i)%2)
        {
            last2=max(last2,i+1);
        }
        mp1[a[i]]=i;mp2[b[i]]=i;
    }
    map<int,int>mp3,mp4;
    for(int i=n-1;i>=0;i--)
    {
        if(mp3[a[i]]&&(mp3[a[i]]-i)%2==0)
        {
            last2=max(last2,i+1);
        }
        if(mp4[a[i]]&&mp4[a[i]]-i>1&&(mp4[a[i]]-i)%2)
        {
            last2=max(last2,i+1);
        }
        if(mp3[b[i]]&&mp3[b[i]]-i>1&&(mp3[b[i]]-i)%2)
        {
            last2=max(last2,i+1);
        }
        if(mp4[b[i]]&&(mp4[b[i]]-i)%2==0)
        {
            last2=max(last2,i+1);
        }
        mp3[a[i]]=i;mp4[b[i]]=i;
    }
    cout<<max(last1,last2)<<'\n';
}
signed main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t=1;cin>>t;
    while(t--)
    {
        solve();
    }
    return 0;
}