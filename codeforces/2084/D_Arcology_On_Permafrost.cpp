int main{
int t; 
cin >> t;
while(t--){
    int n, m, k;
    cin >> n >> m >> k;
    int R = (n-1)/(m+1);
    if((n-1) % (m+1) == 0) R++;
    vector<int> a(n);
    for (int i = 0; i < n; i++){
        a[i] = i % R;
    }

}}
