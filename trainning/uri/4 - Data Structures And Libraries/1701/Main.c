#include <stdio.h>

int fibonacci(int pos) {
    int p1 = 0, p2 = 1, pA = 0;
    int cont;
    for(cont = 0; cont < pos; cont++) {
        p1 = p2;
        p2 = pA;
        pA = p1 + p2;
    }

    return pA;
}

int main() {
    int a, b, n, retorno, cont;
    long long num;

    while(1) {
        num = 0;

        retorno = scanf("%d %d %d", &a, &b, &n);
        if((a == 0 && b == 0 && n == 0) || retorno == EOF)
            break;

        for( cont = -1; cont < n; cont++) {
            num += fibonacci(a + cont + 1) * fibonacci(b + cont + 1);
        }

        printf("%lld\n", num);
    }

    return 0;
}