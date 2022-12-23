#include <iostream>
using namespace std;

int main(void){
    unsigned long N;
    int a;
    cin >> N;
    cout << "シフト前: " << std::bitset<8>(N) << ":" << N << endl;

    for (int i = 1; i < 100; i++) {
        // N = N << 1; // これはNを左に1bitシフトするよ。の意味。1 << N と書くと,1を左にNbitシフトするよになってしまう。
        // a = (1 << i)
        cout << i << "回目のシフトをすると" << std::bitset<64>(N << i) << ":" << (N << i) << endl;
        // a++;
        // 0001
        // 0010
        // 0100
        // 1000
    }

    return 0;
}