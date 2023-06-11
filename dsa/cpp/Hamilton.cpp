#include<bits/stdc++.h>
using namespace std;
vector<int> List[25];
int m,n,check;
bool chuaxet[25];
void Haminton(int u, int count){
	if(count == n){ check = 1; return;}
	for(int i=0; i<List[u].size(); i++){
		int v = List[u][i];
		if(chuaxet[v]){
			chuaxet[v] = false;
			Haminton(v,count+1);
			chuaxet[v] = true;
		}
	}
}
main(){
	int t,u,v,i; cin>>t;
	while(t--){
		for(i=1; i<=20; i++) List[i].clear();
		memset(chuaxet,true,sizeof(chuaxet));
		cin >> n >> m;
		for(i=1; i<=m; i++){
			cin >> u >> v;
			List[u].push_back(v);
			List[v].push_back(u);
		}
		check=0;
		for(int i=1; i<=n; i++){
			chuaxet[i] = false;
			Haminton(i,1);
			chuaxet[i] = true;
		}
		cout << check << endl;
	}
}

