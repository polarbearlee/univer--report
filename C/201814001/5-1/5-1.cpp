#include "stdafx.h"

int main(void)
{
	int num1, num2;
	int num3, num4, result1;

	printf("�� ����� ��ǥ �Է�:  ");
	scanf("%d %d", &num1, &num2);
	printf("�� �ϴ��� ��ǥ �Է�:  ");
	scanf("%d %d", &num3, &num4);

	result1 = (num3 - num1)*(num4 - num2);

	printf("�� ����� x, y ��ǥ:%d %d \n", num1, num2);
	printf("�� ����� x, y ��ǥ:%d %d \n", num3, num4);
	printf("�� ���� �̷�� ���簢���� ���̴� %d �Դϴ�. \n", result1);
	return 0;
}
