
#include <iostream>
using namespace std;

int main() {
    const int ROWS = 4;
    const int COLS = 3;
    int arr[ROWS][COLS] = {};

    for (int i = 0; i < ROWS; i++) {
        arr[i][1] = i + 1;
    }

    for (int j = 0; j < ROWS; j++) {
        int *start = &arr[j][1];
        arr[j][0] = *start;
        if (j > 0) {
            int *end = &arr[j-1][1];
            arr[j][2] = *end;
        }
    }

    for (int r = 0; r < ROWS; r++) {
        for (int c = 0; c < COLS; c++) {
            cout << arr[r][c] << " ";
        }
        cout << endl;
    }

    return 0;
}
