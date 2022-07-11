#include <stdio.h>

int main() {

    int num;
    int digit;
    int tot=0;
    printf("Sayi Giriniz: ");
    scanf("%d",&num);
    int temp=num;
    
    while(num!=0)
    {
        digit=num%10; 	//Get last digit of number
        num=num/10;		//prepare number for next iteration		 
        tot=tot+(digit*digit*digit);
    }
    if(temp!=tot)
    {
        printf("Armstrong Degildir.");
    }else
    {
        printf("Armstrongdur.");
    }
    
    
    return 0;
}
