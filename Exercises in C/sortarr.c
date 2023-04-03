#include<stdio.h>

int main(void)
{
  //define array numbers and element n in [numbers]
  int numbers[5];
  int n;
  //getting 5 inputs
  for (int n = 0; n <= 4; n++)
  {
    printf("Element-%d: ", n);
    scanf("%d", &numbers[n]);
  }
  //sorting the inputs
  for (n = 0; n <= 4; n++)
  {
    for (int m = n + 1; m <= 4; m++)
    {
      //if an element is > than the one that comes before it, swap them
      if (numbers[n] > numbers[m])
      {
        int temp = numbers[n];
        numbers[n] = numbers[m];
        numbers[m] = temp;
      }
    }
  }
  //print the inputs in the right order
  printf("Elements of array in sorted ascending order: ");
  for (n = 0; n <= 4; n++)
  {
    printf("%d", numbers[n]);
  }
  printf("\n");
}