#include <stdio.h>

int main(void){
	
	int n;
	scanf("%d",&n);
	int arr[n];
	
	for(int i=0; i<n; i++){
		scanf("%d",&arr[i]);
	}
	int min=arr[0] , max=arr[0];
	for(int j=0; j<n; j++){
		if(arr[j]<min)
		  min=arr[j];
		if(arr[j]>max)
		max=arr[j];
	}
	printf("%d %d",min,max);
}