#include<stdio.h>

int main(void)
{
  int input;
  int sum = 0;
  float avg;
  for (int counter = 1; counter <= 10; counter++)
  {
    printf("Number %d: ", counter);
    scanf("%d", &input);
    sum = sum + input;
  }
  avg = sum/10.00;
  printf("The sum of 10 numbers is: %d\n The average of 10 numbers is %.2f\n", sum, avg);
}