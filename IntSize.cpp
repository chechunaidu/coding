#include <cstdio>
using namespace std;

constexpr size_t byte =8;

int main(){
    printf("the size of int is %d\n",sizeof(int)*byte);
    printf("the size of char is %d\n",sizeof(char)*byte);
    printf("the size of the long int is %d\n",sizeof(long int)*byte);
    printf("the size of short int is %d\n",sizeof(short int)*byte);
    
}
