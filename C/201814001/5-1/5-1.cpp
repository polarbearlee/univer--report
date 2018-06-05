#include "stdafx.h"

int main(void)
{
	int num1, num2;
	int num3, num4, result1;

	printf("ÁÂ »ó´ÜÀÇ ÁÂÇ¥ ÀÔ·Â:  ");
	scanf("%d %d", &num1, &num2);
	printf("¿ì ÇÏ´ÜÀÇ ÁÂÇ¥ ÀÔ·Â:  ");
	scanf("%d %d", &num3, &num4);

	result1 = (num3 - num1)*(num4 - num2);

	printf("ÁÂ »ó´ÜÀÇ x, y ÁÂÇ¥:%d %d \n", num1, num2);
	printf("ÁÂ »ó´ÜÀÇ x, y ÁÂÇ¥:%d %d \n", num3, num4);
	printf("µÎ Á¡ÀÌ ÀÌ·ç´Â Á÷»ç°¢ÇüÀÇ ³ÐÀÌ´Â %d ÀÔ´Ï´Ù. \n", result1);
	return 0;
}
