#include <stdio.h>

int main(){
    
    char name[] = "AstraQuark";      // String - Double Quotes
    char score = 'X';                // Character - Single Quotes
    int video = 02;                   // Integer
    float version = 0.100;           // Float (Decimal)
    double code = 99.9876543210;     // Double (Decimal)
    print("Name : %s", name);
    print("%c \n", score);
    print("Video : %d \n", video);
    print("Version : v%.1f \n", version);
    print("Code : %.10lf", code);
    
    return 0;
}
