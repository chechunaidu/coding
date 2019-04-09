#include <cstdio>
using namespace std;

int func(){
   static int  x=7;
   return ++x;

}
int junk(){
    int x=7;
    return ++x;
}
int main(){

int i=42;
i=func();
printf("%02d\n",i);//output will 8
int j=junk();
printf("%02d\n",j);//output will 8
j=junk();
printf("%02d\n",j);//output will be 8
j=junk();
printf("%02d\n",j); //outpur will be 8

i=func(); 
printf("%02d\n",i);// output will 9
i=func(); 
printf("%02d\n",i);// output will be 10
return 0; 

}

