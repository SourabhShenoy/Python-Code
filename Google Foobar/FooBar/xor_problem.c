#include <stdio.h>

unsigned int xor_1_to_n(unsigned int N){
    unsigned int check = N & (N % 2 ? 0 : ~0) | ( ((N & 2)>>1) ^ (N & 1) );
    return check;
}

unsigned int xor_probelm(int start, int checkpoint){
    int i;
    unsigned int sum = 0;
    int check_temp_for_loop = checkpoint;
    for ( i = 0; i < check_temp_for_loop; i++){
        unsigned int a = xor_1_to_n(start - 1);
        unsigned int b = xor_1_to_n(start + checkpoint -1);
        sum = sum ^ a ^ b;
        start = start + check_temp_for_loop;
        checkpoint --;
    }
    return sum;
}

int main(){
    printf("%u\n", xor_probelm(17, 4));
    return 0;
}
