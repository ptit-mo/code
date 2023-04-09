#include<bits/stdc++.h>
using namespace std;
int F[1005][1005], N, M, A[1005], C[1005];
int qhd(){
    int i,j;
    memset(F,0,sizeof(F));
    for(i=1;i<=N;i++){
        for(j=1;j<=M;j++){
            F[i][j] = F[i-1][j];
            if(j >= A[i]){
                F[i][j] = max(F[i][j], F[i-1][j-A[i]] + C[i]);
            }
        }
    }
    return F[N][M];
}
main(){
    int t, i;
    cin >> t;
    while(t--){
        cin >> N >> M;
        for(i=1;i<=N;i++) cin >> A[i];
        for(i=1;i<=N;i++) cin >> C[i];
        cout << qhd() << endl;
    }
}
