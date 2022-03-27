// gcc -o carlcar carlcar.c -lcurses -no-pie

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>

__attribute__((constructor)) void ignore_me() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

int car_server_socket;
struct sockaddr_in server_addr;

void die() {
    printf("<<< Remote Controlled CTF 5.0 Terminated"); // Places a 'd\x00' into binary
    close(car_server_socket);
    exit(0);
}

int send_command(char* cmd) {
    printf("Sending: %s",cmd);
    sendto(car_server_socket, cmd, 1, 0, (struct sockaddr*)&server_addr, sizeof(server_addr));
}

void car_server_connect() {
    printf("<<< ------------------------------------------\n");
    printf("<<< Welcome to Remote Controlled CTF 5.0.     \n") ;
    printf("<<< ------------------------------------------\n");
    printf("<<< Connecting to local car server...\n");
    car_server_socket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(31337);
    server_addr.sin_addr.s_addr = inet_addr("127.0.0.1");
    printf("<<< Connected to local car server.\n");
}

int banner() {
    char q[16]; // CHANGED
    char buf[256];
    car_server_connect();
    printf("     Would you like to leave a complaint (Y|N) >>> ");
    fgets(q,256,stdin);  
    if (strncmp(q,"Y",1)==0) {
    printf("<<< ");
    printf(q);
    printf("\n");
    printf("     Enter your complaint >>> ");
    fgets(buf,0x256,stdin);
    puts("Thank you"); // places a 'u\x00' into binary
    } else {
        puts("Farewell"); // places an 'l\x00' into binary
    }
}
int main(int argc, char ** argv) {
    ignore_me();
    banner();
    return 0;
}

// Target Gadget
void whats_this() {
    __asm__(
"        ldp x0, x1, [sp], #0x10 \n" // Pops x0 & x1
"        ldp x29, x30, [sp], #0x10 \n" // Pops x29 & x30
"        ret \n"
    );
}
