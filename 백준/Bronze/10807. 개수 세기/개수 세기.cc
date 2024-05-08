#include<stdio.h>

int main(void) {

	int lenth;
	int arr[100];
	int n=0;
	int choose;

	scanf("%d", &lenth);
	for (int i = 0; i < lenth; i++) {
		//printf("정수를 입력하시오%d:", i + 1);
		scanf("%d", &arr[i]);
	
	}
	/*for (int i = 0; i < lenth; i++) {
		printf("%d", arr[i]);
	}*/
	//printf("\n");
	//printf("출력하고 싶은 숫자를 입력하시오:");
	scanf("%d", &choose);

	for (int i = 0; i < lenth; i++) {
		if (arr[i] == choose)
			n += 1;
	}
	printf("%d", n);
}