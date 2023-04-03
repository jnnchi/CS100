#include<stdio.h>

int main(void)
{
  int i = 0;
  int sum = 0;
  for(int i = 1; i <= 10; i++)
  {
    sum = sum + i;
  }
  printf("The sum of the first 10 natural numbers is: %d\n",sum);
}