#include <stdio.h>

void swap(int *x, int *y);

int main(void)
{
  //get total elements in array
  int arr[5000];
  int size;
  printf("Input the number of elements to be stored in the array: ");
  scanf("%d", &size);

  //ask for the values of each element
  printf("Input %d elements in the array: \n", size);
  for (int n = 0; n < size; n++)
  {
    printf("element-%d: ", n);
    scanf("%d", &arr[n]);
  }

  //sort the values in the array
  for (int n = 0; n < size; n++)
  {
    for (int m = n + 1; m < size; m++)
    {
      //keep swapping elements until they're in order
      if (arr[n] > arr[m])
      {
        swap(&n, &m);
      }
    }
  }
  //print the largest
  printf("The largest element in the array is: %d\n", arr[size-1]);
}

//swap function
void swap(int *x, int *y)
{
  int temp = *x;
  *x = *y;
  *y = temp;
}