#include<stdio.h>

int main(void)
{
  int numbers[10];
  int n;
  for (int n = 0; n <= 9; n++)
  {
    printf("Element-%d: ", n);
    scanf("%d", &numbers[n]);
  }
  printf("Elements in array are: ");
  for (int n = 0; n < 10; n++)
  {
    printf("%d ", numbers[n]);
  }
  printf("\n");
}