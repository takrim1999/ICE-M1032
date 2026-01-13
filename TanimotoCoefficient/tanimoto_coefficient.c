#include <stdio.h>

int main() {
    float x[] = {1.0, 1.0};
    float y[] = {1.0, 0.0};
    int n = 2;
    
    float dot_xy = 0.0, dot_xx = 0.0, dot_yy = 0.0;
    
    for(int i=0; i<n; i++) {
        dot_xy += x[i] * y[i];
        dot_xx += x[i] * x[i];
        dot_yy += y[i] * y[i];
    }
    
    float sim = dot_xy / (dot_xx + dot_yy - dot_xy);
    
    printf("Vector x: (1, 1)");
    printf("Vector y: (1, 0)");
    printf("Tanimoto Coefficient: %.4f", sim);
    
    return 0;
}