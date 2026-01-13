#include <stdio.h>
#include <string.h>

// Simple function to check string equality
int is_match(char* s1, char* s2) {
    return strcmp(s1, s2) == 0;
}

int main() {
    // Example Data
    char* x[] = {"Circle", "Red", "Small"};
    char* y[] = {"Circle", "Blue", "Small"};
    
    int p = 3; // Total attributes
    int m = 0; // Matches

    printf("Object x: {%s, %s, %s}\n", x[0], x[1], x[2]);
    printf("Object y: {%s, %s, %s}\n", y[0], y[1], y[2]);

    for (int i = 0; i < p; i++) {
        if (is_match(x[i], y[i])) {
            m++;
        }
    }

    float dissimilarity = (float)(p - m) / p;
    
    printf("Matches (m): %d\n", m);
    printf("Dissimilarity: %.4f\n", dissimilarity);
    
    return 0;
}