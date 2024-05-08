#include<stdio.h>

int main(){
	
	int a[10000];
	int n ,x;
	
	//printf("숫자의 갯수를 입력하시오:");
	scanf("%d %d",&n, &x);
	for(int i=0; i<n; i++){
		//printf("숫자%d:",i+1);
		scanf("%d",&a[i]);
	}
	//printf("숫자를 입력하시오:");
	
	for(int i=0; i<n; i++)
		if(a[i]<x)
    
	 	printf("%d ",a[i]);
    return 0;
}