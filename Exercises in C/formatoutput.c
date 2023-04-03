#include<stdio.h>

int main(void)
{
  // Compute total owed, assuming 8% tax and 15% tip
  float subtotal = (38+40+30);
  float tax = 0.08*subtotal;
  float tip = 0.15*subtotal;
  float total = tax + tip + subtotal;
  printf("Subtotal: $%.02f\n Tax: $%.02f\n Tip: $%.02f\n Total: $%.02f\n", subtotal, tax, tip, total);
  return 0;
}