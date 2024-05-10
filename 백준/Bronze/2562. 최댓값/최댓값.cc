#include <stdio.h>

int main(void){
	
	int a[9],max=0,check;
	 
	for(int i=0; i<9; i++){
		scanf("%d",&a[i]);
		if(max<a[i]){	
		max = a[i];
		check = i;
	 }
	}
	printf("%d\n%d",max,check+1);
}
