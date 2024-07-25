#include <stdio.h>
int main() {
	int celc;
	int farh;
	int choice;
	printf ("Enter 1 for fahrenheit to celcius or Enter 2 for celcius to fahrenheit: ");

	scanf("%d",&choice);
	if (choice == 1) {
		printf ("Enter the temperature in fahrenheit: ");
		scanf("%d",&farh);
		celc= ((farh - 32.0)*(5.0/9.0));
		printf ("%d", celc);
	} else if (choice == 2) {
		printf ("Enter the  temperature in Celcius: ");
		scanf("%d",&celc);
		farh = (celc * (9.0/5.0)+32.0);
		printf ("%d", farh);
	} else {
		printf ("Wrong choice!");

	}
	return 0;
}