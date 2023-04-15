#include<bits/stdc++.h>
using namespace std;
void xuly(int n){
	queue<string> q;
	q.push("6"); q.push("8");
	vector<string> kq;
	while(1){
		string temp = q.front();
		kq.push_back(temp);
		q.pop();
		if(temp.length() <= n - 1){
			q.push(temp + '6');  q.push(temp + '8');
		} 
		else break; 
	} 
	while(q.size()){
		kq.push_back(q.front());
		q.pop(); 
	} 
	for(int i = kq.size() - 1; i >= 0; i--) cout << kq[i] << ' ';
	cout << endl; 
} 

int main(){
	int t,n; cin >> t;
	while(t--){
		cin >> n;
		xuly(n);
	}
}
