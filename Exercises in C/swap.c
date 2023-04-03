#include <stdio.h>

void swap(int *x, int *y);

int main(void)
{
  int num1, num2;
  //get the two inputs
  printf("Input 1st number: ");
  scanf("%d", &num1);
  printf("Input 2nd number: ");
  scanf("%d", &num2);

  //swap the inputs
  printf("Before swapping: n1 = %d, n2 = %d\n", num1, num2);
  swap(&num1, &num2);
  printf("After swapping: n1 = %d, n2 = %d\n", num1, num2);
}
//swap function
void swap(int *x, int *y)
{
  int temp = *x;
  *x = *y;
  *y = temp;
}