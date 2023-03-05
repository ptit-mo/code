#include<stdio.h>
main(){
    int t, n, i;
    double kq;
    scanf("%d",&t);
    while(t--){
        scanf("%d",&n);
        kq = 0;
        if(n%2==0){
            for(i=2;i<=n;i+=2) kq = kq + (double) 1/i;
        } else {
            for(i=1;i<=n;i+=2) kq = kq + (double) 1/i;
        }
        printf("%.6f\n",kq);
    }
}

