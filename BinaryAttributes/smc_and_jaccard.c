#include <stdio.h>

int main() {
    // Example Data
    int x[] = {1, 0, 0, 1};
    int y[] = {1, 0, 1, 0};
    int n = 4;

    int q = 0, r = 0, s = 0, t = 0;

    for(int i = 0; i < n; i++) {
        if(x[i] == 1 && y[i] == 1) q++;
        else if(x[i] == 1 && y[i] == 0) r++;
        else if(x[i] == 0 && y[i] == 1) s++;
        else if(x[i] == 0 && y[i] == 0) t++;
    }

    float smc = (float)(r + s) / (q + r + s + t);
    float jaccard = (float)(r + s) / (q + r + s);

    printf("x: {1, 0, 0, 1}\n");
    printf("y: {1, 0, 1, 0}\n");
    printf("q=%d\nr=%d\ns=%d\nt=%d\n", q, r, s, t);
    printf("SMC Distance: %.4f\n", smc);
    printf("Jaccard Distance: %.4f\n", jaccard);

    return 0;
}