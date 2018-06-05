// ConsoleApplication1.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"


int main(void)
{
	int i = 1;
	int num = 0;
	int a = 1;

	printf("정수 입력: ");
	scanf("%d", &num);
	while (i <= num) {
		a *= i;
		i++;
	}
	printf("%d \n", a);
    return 0;
}

