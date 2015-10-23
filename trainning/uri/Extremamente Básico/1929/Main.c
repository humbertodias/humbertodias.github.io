#include <stdio.h>

int main()
{
    /**
     * Escreva a sua solução aqui
     * Code your solution here
     * Escriba su solución aquí
     */
    unsigned long comb[21];
    int a, b;
    
    comb[0] = 1;
    for(int i = 1; i < 21; i++)
        comb[i] = i*comb[i-1];
    
    while(scanf("%d %d", &a, &b) != '\0')
        printf("%d\n",comb[a] + comb[b]);
    return 0;
}
