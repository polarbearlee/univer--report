// 3_5.cpp : �ܼ� ���� ���α׷��� ���� �������� �����մϴ�.
//

#include "stdafx.h"


int main()
{
	int num1, num2, num3, result;
	printf("�� ���� ���� �Է�: ");
	scanf("%d %d %d", &num1, &num2, &num3);

	result = (num1 - num2)*(num2 + num3)*(num3%num1);
	printf("%d", result);
    return 0;
}

