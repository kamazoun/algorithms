#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <unistd.h>

void *task(void *vargp){
    sleep(1);
    printf("from function");
    return NULL;
}

int main(){
    pthread_t thread_id;
    printf("Before threading...");

    pthread_create(&thread_id, NULL, task, NULL);
    pthread_join(thread_id, NULL);
    printf("After threading...");

    exit(0);
}