// gcc -o car car_overflow.c -lcurses -no-pie

#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <curses.h>
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
    close(car_server_socket);
    endwin();
    exit(0);
}

void car_server_connect() {
    printw("<<< ------------------------------------------\n");
    printw("<<< Welcome to Remote Controlled CTF 4.0.     \n") ;
    printw("<<< ------------------------------------------\n");
    printw("<<< Connecting to local car server...\n");
    car_server_socket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(31337);
    server_addr.sin_addr.s_addr = inet_addr("127.0.0.1");
    printw("<<< Connected to local car server.\n");
}

int send_command(char* cmd) {
    sendto(car_server_socket, cmd, 1, 0, (struct sockaddr*)&server_addr, sizeof(server_addr));
}

void driver_menu() {
    initscr();
    keypad(stdscr, TRUE);
    nodelay(stdscr, TRUE);
    car_server_connect();
    char ch = 0, k = 0;
    printw("<<< ------------------------------------------\n");
    printw("<<< Remote Controlled CTF v4.0 Driver Panel  \n");
    printw("<<< ------------------------------------------\n");
    printw("<<< Use arrow keys to drive, E to exit\n");
    printw("<<< Make sure to press ENTER after each key!\n");
    printw("<<< ------------------------------------------\n");
    printw(">>> ");
    refresh();

    while (1)
    {
        ch = getch();
        switch (ch) {
        case 2: send_command("d"); break;
        case 3: send_command("u"); break;
        case 4: send_command("l"); break;
        case 5: send_command("r"); break;
        case 101: case 69: die(); break;
        }
    }
}


void authenticate() {
    char access[8] = "DENIED";
    char contact[16];
    printf("We are sorry, but our car service is not available at this time.\n");
    printf("Please provide your contact info and we'll get back to you as soon as possible >>> ");
    fgets(contact, 24, stdin);
    if(strcmp(access, "GRANTED")==0) {
        driver_menu();
    }
    else {
        printf("<<< Thank you!\n");
    }
    return;
}

int main(int argc, char ** argv) {
    ignore_me();
    authenticate();
    return 0;
}
