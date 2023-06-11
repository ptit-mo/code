#include<bits/stdc++.h>
using namespace std;
bool chuaxet[1005];
vector<int> List[1005];
void DFS(int u){
	int v,i;
	chuaxet[u]=false;
	for(int v : List[u]){
        if(chuaxet[v]) DFS(v);
	}
}
main(){
	int t,i,m,n,u,v,q;
	cin>>t;
	while(t--){
		for(i=0;i<1005;i++)	List[i].clear();
		cin>>n>>m;
		for(i=0;i<m;i++){
			cin>>u>>v;
			List[u].push_back(v);
			List[v].push_back(u);
		}
		cin>>q;
        while(q--){
            memset(chuaxet,true,sizeof(chuaxet));
            cin>>u>>v;
            DFS(u);
            if(chuaxet[v]) cout<<"NO"<<endl;
            else cout<<"YES"<<endl;
        }
	}
}
