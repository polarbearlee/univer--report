
#include "stdafx.h"


int main(void)
{
	int num1, num2;

	printf("두개의 정수 입력: ");
	scanf("%d %d", &num1, &num2);

	printf("%d곱하기%d는 %d\n", num1, num2, num1*num2);
	printf("%d빼기%d는 %d\n", num1, num2, num1 - num2);

	return 0;
}
