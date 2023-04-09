#include<bits/stdc++.h>
using namespace std;
int qhd(int a[], int n, int S){
    int F[S+1] = {0}, i, j;
    F[0] = 1;
    for(i = 1; i <= n; i++){
        for(j = S; j >= a[i]; j--){
            if(F[j] == 0 && F[j - a[i]] == 1)
                F[j] = 1;
        }
    }
    return F[S];
}
main(){
    int n, S, i, t;
    cin >> t;
    while(t--){
        cin >> n >> S;
        int a[n];
        for(i = 1;i <= n;i++) cin >> a[i];
        if(qhd(a, n, S)) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
}
