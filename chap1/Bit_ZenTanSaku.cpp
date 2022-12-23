#include <iostream>
using namespace std;

int main() {
    int N, K, A[22];
    cin >> N >> K;
    for (int i = 1; i <= N; i++){
        cin >> A[i];
    }

    bool Answer = false;
    for (int i = 0; i < (1 << N); i++){
        int sum = 0;
        for (int j = 1; j <= N; j++){
            int wari = (1 << (j - 1));
            if ((i / wari) % 2 == 1){
                sum += A[j];
            }
        }
        if (sum == K){
            Answer = true;
        }
    }

    if (Answer == true){
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    return 0;
}