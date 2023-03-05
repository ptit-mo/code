#include<stdio.h>
#include<string.h>
main(){
	int t; char s[20];
	scanf("%d",&t);
	while(t--){
		scanf("%s",s);
		int n = strlen(s);
		if(s[0]==s[n-2] && s[1]==s[n-1]) printf("YES\n");
		else printf("NO\n");
	}
}
