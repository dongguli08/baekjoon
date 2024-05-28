#include <stdio.h>

int main(void){
	
	int price;
	int  allprice;
	int num;
	int time;
	int a = 0;
	
	//printf("가격을 입력하시오:");
	scanf("%d",&allprice);
	
	//printf("구매한 물건의 갯수를 입력:");
	scanf("%d",&num);
	
	for(int i=0; i<num; i++){
		//printf("물건 %d의가격과 갯수를 입력하시오:",i+1);
		scanf("%d %d",&price,&time);
		a += price*time;
	}
	if(a==allprice){
		printf("Yes");
}
	else 
	printf("No");
}
