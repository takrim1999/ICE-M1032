#include <stdio.h>
#include <math.h>

int main() {
    float x[] = {1.0, 1.0};
    float y[] = {1.0, 0.0};
    int n = 2;
    
    float dot = 0.0, mag_x = 0.0, mag_y = 0.0;
    
    for(int i=0; i<n; i++) {
        dot += x[i] * y[i];
        mag_x += x[i] * x[i];
        mag_y += y[i] * y[i];
    }
    
    mag_x = sqrt(mag_x);
    mag_y = sqrt(mag_y);
    
    float sim = dot / (mag_x * mag_y);
    
    printf("Vector x: (1, 1)");
    printf("Vector y: (1, 0)");
    printf("Cosine Similarity: %.4f", sim);
    
    return 0;
}