#include<bits/stdc++.h>
#define ll long long 
#define yes cout<<"Yes"<<endl
#define no cout<<"No"<<endl
using namespace std;
ll a[200005],b[200005];
ll n,m;
bool judge(){
	for(int i=2;i<=n;i++){
		if(a[i]<a[i-1])return 0;
	}
	return 1;
}
void aaa(){
	cin>>n>>m;
	for(int i=1;i<=n;i++)cin>>a[i];
	for(int i=1;i<=m;i++)cin>>b[i];
	
	if(n==1){
		yes;
		return;
	}
	sort(b+1,b+m+1);
	
	int now=b[1]-a[1];
	if(now<a[1])a[1]=now;
	for(int i=2;i<=n;i++){
		if(b[m]-a[i]<a[i-1]&&a[i]<a[i-1]){
			no;
			return;
		}
		if(b[m]-a[i]<a[i-1])continue;
		int now=lower_bound(b+1,b+m+1,a[i]+a[i-1])-b;
		if(a[i]>=a[i-1])a[i]=min(a[i],b[now]-a[i]);
		else a[i]=b[now]-a[i];
		if(a[i]<a[i-1]){
			no;
			return;
		}
	}
	if(judge())yes;
	else no;
}

int main(){
	int n;cin>>n;
	while(n--)aaa();
}