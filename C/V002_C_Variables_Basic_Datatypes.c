#include <stdio.h>

int main(){
    
    char name[] = "AstraQuark";      // String - Double Quotes
    char score = 'X';                // Character - Single Quotes
    int video = 2;                   // Integer
    float version = 0.100;           // Float (Decimal)
    double code = 99.9876543210;     // Double (Decimal)
    printf("Name : %s \nScore : %c \nVid No. : %d %i \nVersion : %.2f %.1F \nCode : %.10lf",name,score,video,video,version,version,code);
    
    return 0;
}