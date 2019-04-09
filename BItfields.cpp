#include <cstdio>
using namespace std;
struct preferences
{
    bool likemusic:1;
    bool hashair:1;
    bool hasinternet:1;
    bool hasDinosur:1;
    unsigned int noofchilderen:4;
    /* data */
};


int main(){
    struct preferences homer;
    homer.hasDinosur=false;
    homer.hashair=true;
    homer.hasinternet=true;
    homer.likemusic=true;
    homer.noofchilderen=3;

    return 0;
}