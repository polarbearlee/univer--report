// 5_2.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

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

