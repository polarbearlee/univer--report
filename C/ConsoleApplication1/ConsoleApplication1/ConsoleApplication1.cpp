// ConsoleApplication1.cpp : �ܼ� ���� ���α׷��� ���� �������� �����մϴ�.
//

#include "stdafx.h"


int main(void)
{
	int i = 1;
	int num = 0;
	int a = 1;

	printf("���� �Է�: ");
	scanf("%d", &num);
	while (i <= num) {
		a *= i;
		i++;
	}
	printf("%d \n", a);
    return 0;
}

