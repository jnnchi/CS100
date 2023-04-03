#include <stdio.h>

void swap(int *x, int *y);

int main(void)
{
  int numbers[8] = {14, 33, 27, 10, 35, 19, 42, 44};
  int i, j;
  int counter = 0;
  for (i = 1; i <= 8; i++)
  {
    for (j = 0; j < 8; j++)
    {
      if (numbers[j] > numbers[j+1])
      {
        counter++;
        swap(&numbers[j], &numbers[j+1]);
      }
    }
    printf("Pass %d had %d comparisons\n", j, counter);
    counter = 0;
  }
  printf("Sorted Array is: ");
  for (int n = 0; n < 8; n++)
  {
    printf("%d ", numbers[n]);
  }
  printf("\n");
}

void swap(int *x, int *y)
{
  int temp = *x;
  *x = *y;
  *y = temp;
}