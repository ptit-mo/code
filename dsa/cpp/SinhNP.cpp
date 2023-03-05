#include<iostream>
using namespace std;
int OK = 0, B[30], n;
void in(){
	for(int i=1;i<=n;i++) cout << B[i] << " ";
	cout << endl;
}
void sinh(){
	int i = n;
	while(B[i]){ 
		B[i] = 0; i--;
	}
	if(i==0) OK = 1;
	else B[i] = 1;
}
main(){
	cin >> n;
	while(!OK){
		in();
		sinh();
	}
}
