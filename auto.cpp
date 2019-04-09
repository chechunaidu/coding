#include <cstdio>
#include <vector>
using namespace std;

int main(){
    vector <int> vi={1,2,3,4,5};
    for (auto i=vi.begin();i!=vi.end();++i){
        printf("%d\n",*i);
    }
    return 0;
}