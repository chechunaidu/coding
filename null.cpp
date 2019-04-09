#include <cstdio>
using namespace std;

void func(int i){
    printf("this is int %d\n",i);
}

void func(const char *s){
    printf("this is char %p\n",s);
}

int main(){
    func(nullptr);
    return 0;
}