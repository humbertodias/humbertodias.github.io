#include <stdio.h>


#define sc3(a,b,c) scanf("%d %d %d", &a, &b, &c)

int main(void)
{
    int n, m, c, x, r;

    while(sc3(n,m,c) && (n || m || c))
    {   if(n==0&m==0&&c==0) break;
        x = (n-7)*(m-7);
        r = x/2;
        if(x%2 == 1 && c == 1) r++;
        printf("%d\n", r);
    }

    return 0;
}