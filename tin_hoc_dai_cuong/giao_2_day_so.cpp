#include<stdio.h>
main(){
	int A[1001]={0}, B[1001]={0}, n, m, i, x;
	scanf("%d%d", &n, &m);
	for(i=0;i<n;i++){
		scanf("%d", &x);
		A[x]++ ;
	}
	for(i=0;i<m;i++){
		scanf("%d",&x);
		B[x]++;
	}
	for(i=0;i<=1000;i++)
	     if(A[i]>0 && B[i]>0) printf("%d ",i);
}

