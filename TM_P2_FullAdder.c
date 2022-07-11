#include <stdio.h>

int main() {


    char num1[8];
    char num2[8];
    int a[8]={0,0,0,0,0,0,0,0};  
	int i;
	int j;
	int b[8]={0,0,0,0,0,0,0,0};  
	int s[8]={0,0,0,0,0,0,0,0};
	int c;
	
    printf("Birinci binary sayisi Giriniz: ");
    scanf("%s",&num1);
    printf("ikinci binary sayi Giriniz: ");
    scanf("%s",&num2);
    

	//Convert char array to int array 
	for (i = 0; num1[i] != 0; i++)
	{
    a[i] = num1[i] - '0';
	}
	
	//Convert char array to int array 
	for (i = 0; num2[i] != 0; i++)
	{
    b[i] = num2[i] - '0';
	}
	
	
	//Full Adder Logic Unit
	c=0;
	for(i=7;i>=0;i--)
	{
		s[i]=(a[i]^b[i])^c;
		c=(a[i]&b[i]) |  ((a[i]|b[i])&c); 
	}
    
    printf("Binary toplam sonucu: "); 
	
	//Print Result  
    for(i=0;i<=7;i++)    
	{    
	printf("%d",s[i]);    
	} 
    
    
    return 0;
}
