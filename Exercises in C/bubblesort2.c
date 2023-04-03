#include <stdio.h>

void swap(int *x, int *y);

int main(void)
{
  int numbers[8] = {40,35,80,75,60,90,70,75};
  int i = 1;
  int j = 0;
  int counter = 0;
  int n = 0;

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
    printf("Pass %d had %d comparisons\n", i, counter);
    counter = 0;
  }
  
  printf("Sorted Array is: ");
  for (int n = 0; n <= 7; n++)
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