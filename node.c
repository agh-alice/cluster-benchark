
// Server side implementation of UDP client-server model 
#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> 
#include <string.h> 
#include <sys/types.h> 
#include <sys/socket.h> 
#include <arpa/inet.h> 
#include <netinet/in.h> 
  
#define PORT    7070
#define MAXLINE 1024 
  
void execute(char *command);
int count_number_of_words(char *string);
char** get_tokens_from_string(char *string);
char *make_copy(char *string);

// Driver code 
int main() { 
    int sockfd; 
    char buffer[MAXLINE];  
    struct sockaddr_in servaddr, cliaddr; 
      
    // Creating socket file descriptor 
    if ( (sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0 ) { 
        perror("socket creation failed"); 
        exit(EXIT_FAILURE); 
    } 
      
    memset(&servaddr, 0, sizeof(servaddr)); 
    memset(&cliaddr, 0, sizeof(cliaddr)); 
      
    // Filling server information 
    servaddr.sin_family    = AF_INET; // IPv4 
    servaddr.sin_addr.s_addr = INADDR_ANY; 
    servaddr.sin_port = htons(PORT); 
      
    // Bind the socket with the server address 
    if ( bind(sockfd, (const struct sockaddr *)&servaddr,  
            sizeof(servaddr)) < 0 ) 
    { 
        perror("bind failed"); 
        exit(EXIT_FAILURE); 
    } 
      
    int len, n; 
  
    len = sizeof(cliaddr);  //len is value/resuslt 
  
    while(n = recvfrom(sockfd, (char *)buffer, MAXLINE,  
                MSG_WAITALL, ( struct sockaddr *) &cliaddr, 
                &len)) {
        buffer[n] = '\0'; 
        printf("Client : %s\n", buffer); 
        execute(buffer);
    }
      
    return 0;
}

void execute(char *command) {
    char *copy = make_copy(command);
    int number_of_tokens = count_number_of_words(copy);
    char** arguments = malloc(sizeof(char*) * (number_of_tokens + 3));
    char** command_words = get_tokens_from_string(command);
    arguments[0] = "sh";
    arguments[1] = "-c";
    for(int i = 0;i < number_of_tokens;i++) {
        arguments[i+2] = command_words[i];
    }
    arguments[number_of_tokens + 2] = NULL;
    printf("Before exec\n");
    int res = execv("/bin/sh", arguments);
    printf("%d\n", res);
    free(copy);
}

int count_number_of_words(char *string) {
    char *copy = make_copy(string);
    int word_counter = 0;
    char *pch;
    char *delimiters = " ,.-";
    printf ("Splitting string \"%s\" into tokens:\n", copy);
    pch = strtok (copy, delimiters);
    while (pch != NULL)
    {
        word_counter++;
        printf ("%s\n",pch);
        pch = strtok (NULL, delimiters);
    }
    free(copy);
    return word_counter;
}

char** get_tokens_from_string(char *string) {
    char *copy = make_copy(string);
    int number_of_tokens = count_number_of_words(copy);
    char **tokens = malloc(sizeof(char*) * number_of_tokens);
    char *pch;
    char *delimiters = " ,.-";
    printf ("Splitting string \"%s\" into tokens:\n", copy);
    pch = strtok (copy, delimiters);
    int index_of_tokens = 0;
    while (pch != NULL)
    {
        printf ("%s\n",pch);
        tokens[index_of_tokens] = pch;
        index_of_tokens++;
        pch = strtok (NULL, delimiters);
    }
    return tokens;
}

char *make_copy(char *string) {
    int string_length = strlen(string);
    char *copy = malloc(string_length + 1);
    strcpy(copy, string);
    return copy;
}
