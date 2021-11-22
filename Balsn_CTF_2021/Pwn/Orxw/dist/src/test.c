#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main(){
    
    char buffer[10];
    close(0);
    int fd1 = open("/dev/pts/0", 2);
    printf("fd1    : %d\n", fd1);
    printf("read   : %d\n" , read(0, buffer, 10));
    printf("buffer : \"%s\"\n", buffer);
}
