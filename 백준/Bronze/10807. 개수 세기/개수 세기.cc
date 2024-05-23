#include <stdio.h>

int main(void) {
	
	int num=0;
	int check=0;
	int count = 0;
	
	//printf("입력받고 싶은 숫자의 갯수를 입력:");
	scanf("%d", &num);
		int arr[num];

	for (int i = 0; i < num; i++) {
		scanf("%d", &arr[i]);
	}
	
	scanf("%d", &check);
	for (int j = 0; j < num; j++) {
		if (arr[j] == check)
		count++;
	}
	printf("%d", count);
}
