#include<stdio.h>

int flipflop(void);

int main(void)
{
  flipflop();
}

//flipflop function
int flipflop(void)
{
  //get maximum value
  int max;
  printf("Max value? ");
  scanf("%d", &max);

  //start printing
  for(int i = 1; i <= max; i++)
  {
    if ((i%15 == 0) && (i%20 != 0))
    {
      printf("flipflop ");
    }
    else if ((i%3 == 0) && (i%5 != 0) && (i%20 != 0))
    {
      printf("flip ");
    }
    else if ((i%5 == 0) && (i%3 != 0) && (i%20 != 0))
    {
      printf("flop ");
    }
    else if ((i%20 == 0) && (i%5 == 0) && (i%15 != 0))
    {
      printf("flop\n");
    }
    else if ((i%20 == 0) && (i%15 == 0))
    {
      printf ("flipflop\n");
    }
    else
    {
      printf("%d ", i);
    }
  }
}