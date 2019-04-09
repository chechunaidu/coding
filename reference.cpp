#include <cstdio>
using namespace std;

int &f( int & i){

    return ++i;

}
int main(){

    int i =5;
    int & ir =i;
    i=10;
    
    printf("%d\n",i);
    printf("%d\n",f(i));//it will be will 11
    printf("%d\n",i); //it will be 11  becuase it is call by reference.
    return 0;


}