#include<stdio.h>
#include<math.h>
int ngto(int n){
	if(n<2) return 0;
	for(int i=2;i<=sqrt(n);i++)
		if(n%i==0) return 0;
	return 1;
}
main(){
	int t, i, x, n;
	scanf("%d",&t);
	while(t--){
		int  b[1001]={0};
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%d",&x);
			b[x]++;
		}
		for(i=2;i<1000;i++) if(b[i]>0 && ngto(i)) printf("%d ",i);
		printf("\n");
	}
}
