#include <stdio.h>
#include <time.h>

int main(){
    int year;
    printf("Enter the year: ");
    scanf("%d", &year);

    struct tm time_in = {
    .tm_year = year - 1900,
    .tm_mday = 13
    };

    printf("Checking for Friday the 13th in the year %d...\n", year);

    for(time_in.tm_mon = 0; time_in.tm_mon < 12; ++time_in.tm_mon){
        mktime(&time_in);
        if(time_in.tm_wday == 5){
            printf("In year %d, there is a Friday the 13th in month %d", year, time_in.tm_mon);
            return 0;
        }
    }
    printf("It is impossible to not have a Friday the 13th in a given year, so our algorithm is wrong if this message is ever printed");
    return 0;
}