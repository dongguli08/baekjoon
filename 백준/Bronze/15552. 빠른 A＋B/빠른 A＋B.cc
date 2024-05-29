#include <stdio.h>

int main(void){
	int num;
	int a,b;
	//printf("갯수를 입력하시오:");
	scanf("%d",&num);
	
	for(int i=0; i<num; i++){
		scanf("%d %d",&a,&b);
		printf("%d\n",a+b);
	}
}