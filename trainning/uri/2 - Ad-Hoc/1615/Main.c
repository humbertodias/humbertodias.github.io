#include <stdio.h>
#include <string.h>
 
int main(int argc, char const *argv[])
{
    int t, n, x, max,i;
    double m;
    scanf("%i", &t);
 
    while(t--)
    {
        scanf("%i %lf", &n, &m);
        int cand[n + 1]; memset(&cand, 0, sizeof cand);
        max = 0;
 
        for (i = 0; i < m; ++i)
        {
            scanf("%d", &x);
            cand[x]++;
            if(cand[max] < cand[x])
                max = x;
        }
         
        if(cand[max] > m/2) printf("%d\n", max);
        else printf("-1\n");
    }
    return 0;
}