#include <cstdio>
using namespace std;
struct Employee
{
    int id;
    const char *name;
    const char *role;
};

int main(){
Employee joe={42,"joe","boss"};
Employee *e=&joe;
printf("%s is the %s of the id %d\n",joe.name,joe.role,joe.id);
printf("%s is the %s of the id %d\n",e->name,e->role,e->id);
return 0;
}