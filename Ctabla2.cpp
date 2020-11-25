#include<stdio.h>

main(){
	int cont, num;
	int tabla=2;
	printf("introduce un numero: ");
	scanf("%d",&tabla);
	printf("*****************");
	printf("* Tabla del %d *", tabla);
	printf("*****************");
	for(cont=0;cont<=10;cont++) {
		//I/O
		printf("%d x %d = %d\n",tabla, cont, tabla);
	}
	return 0;
}
