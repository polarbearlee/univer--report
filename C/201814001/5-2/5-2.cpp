
#include "stdafx.h"


int main(void)
{
	double num1, num2;
	printf("두개의 실수 입력: ");
	scanf("%lf %lf", &num1, &num2);

	printf("%lf+%lf = %lf \n", num1, num2, num1 + num2);
	printf("%lf-%lf = %lf \n", num1, num2, num1 - num2);
	printf("%lfX%lf = %lf \n", num1, num2, num1 * num2);
	printf("%lf/%lf = %lf \n", num1, num2, num1 / num2);
	return 0;
}


