#include <iostream>
using namespace std;
int fib(int terms) {
    int t1 = 0, t2 = 1, nextTerm = 0;
    for (int i = 1; i <= terms; ++i) {
        if(i == terms) {
            return t1;
        }
        nextTerm = t1 + t2;
        t1 = t2;
        t2 = nextTerm;
    }
    return -1; // This line should never be reached
}

int main() {
    int terms;
    cout << "Enter the number of terms: ";
    cin >> terms;
    if(terms <= 0) {
        cout << "Please enter a positive integer." << endl;
    } else {
        cout << "Fibonacci Series: ";
        for (int i = 1; i <= terms; ++i) {
            cout << fib(i) << " ";
        }
        cout << endl;
    }
    return 0;
}