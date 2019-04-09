#include <cstdio>
#include <cstdint>
using namespace std;


union ipv4{
    uint32_t i32;
    struct
    {
        uint8_t a;
        uint8_t b;
        uint8_t c;
        uint8_t d;

    } octets;
    

};

int main(){
    union ipv4 adrs;
    adrs.octets={192,32,4,12};
    printf("addr is %d.%d.%d.%d is %08x\n",adrs.octets.a,adrs.octets.b,adrs.octets.c,adrs.octets.d,adrs.i32);

return 0;
}