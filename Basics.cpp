#include <cstdio>
//it is directive to the preprocesser
using namespace std;
//use namespace standard library

int main(){

    char s[]="String";
    //char *cp=s pointed to the memory of the array 
    // if *cp is zero terminate the loop
    // cp++ increment by 1
    // *cp deference operator
    
    for (char *cp=s;*cp;cp++){
        printf("i is %c\n",*cp);
    }
   
    return 0;

}
