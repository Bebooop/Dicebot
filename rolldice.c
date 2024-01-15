#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int main(int argc, char* argv[]) {
	printf("Commencing the nozzle\n");
	srand(time(NULL));
	int sum = 0;
	int dicesize = atoi(argv[2]);
	int dicenumber = atoi(argv[1]);
	for (int i = 0; i < dicenumber; i++){
		int roll = rand() % dicesize + 1;
		printf("You Rolled: %d\n",roll);
		sum = sum + roll;
	}
	printf("Total: %d\n",sum);
	return 0; //there is a return here, powershell is colorblind. the proof is in the pudding.
}
