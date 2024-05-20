#include <stdio.h>

int main(void) {
    int count = 0;
    char arr[100];
    int i;

    scanf("%s", arr);
    for(i = 0; arr[i] != '\0'; i++) {
        count += i;
    }
    printf("%d", i);

    return 0;
}