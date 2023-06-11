#include<bits/stdc++.h>
using namespace std;

bool chuaxet[1005];
vector<int> List[1005];
void DFS(int u){
	chuaxet[u]=false;
	for(int i=0; i<List[u].size(); i++){
        int v = List[u][i];
        if(chuaxet[v]) DFS(v);
	}
}
main(){
	int t,n,m,x,y,i;
	cin>>t;
	while(t--){
		memset(chuaxet,true,sizeof(chuaxet));
		for(i=0;i<1005;i++) List[i].clear();
		cin >> n;
		for(i=1;i<n;i++){
			cin>>x>>y;
			List[x].push_back(y);
			List[y].push_back(x);
		}
		DFS(1);
		bool check = true;
		for(i=2;i<=n;i++){
            if(chuaxet[i]) check = false;
		}
		if(check) cout << "YES" << endl;
		else cout << "NO" << endl;
	}
}
