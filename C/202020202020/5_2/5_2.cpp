// 5_2.cpp : �ܼ� ���� ���α׷��� ���� �������� �����մϴ�.
//

#include "stdafx.h"


int main(void)
{
	double num1, num2;
	printf("�ΰ��� �Ǽ� �Է�: ");
	scanf("%lf %lf", &num1, &num2);

	printf("%lf+%lf = %lf \n", num1, num2, num1 + num2);
	printf("%lf-%lf = %lf \n", num1, num2, num1 - num2);
	printf("%lfX%lf = %lf \n", num1, num2, num1 * num2);
	printf("%lf/%lf = %lf \n", num1, num2, num1 / num2);
    return 0;
}

