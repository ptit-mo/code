#include <bits/stdc++.h>
using namespace std;
void qhd(int a[],int n){
    int s=0, e = 0;
    for(int i=0;i<n;i++){
        e = max(a[i], e + a[i]);
        s = max(s, e);
    }
    cout << s <<endl;
}
main(){
    int t,a[1000],n,i;
    cin >> t;
    while(t--){
        cin>>n;
        for(i=0;i<n;i++) cin>>a[i];
        qhd(a,n);
    }
}
