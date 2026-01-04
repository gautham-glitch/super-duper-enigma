#include <iostream>
using namespace std;
bool myxor(bool a, bool b) {
    return (a && !b) || (!a && b);
}
//xor operation



int main() {
    cout << boolalpha;
    bool result = myxor(true,false);
    bool *val =  &result;
    cout << val << endl;
    return 0;

}