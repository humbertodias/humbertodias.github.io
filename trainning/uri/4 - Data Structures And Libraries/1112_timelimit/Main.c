#include <stdio.h>
#include <string.h>

unsigned int m[1001][1001];

int main(){
  unsigned int x,y,p,q,X,Y,N,Z,W,soma,i,j;
  char op;

  for(;;){
    scanf("%d %d %d",&x,&y,&p);
    
    if(x == 0 && y == 0 && p == 0)
      break;

    
    // for (i = 0; i <= x; ++i)
    //   for (j = 0; j <= y; ++j)
    //     m[i][j] = 0;

    for (i = 0; i <= x; ++i)
    memset(m[i], 0, sizeof(int) * y);

    scanf("%d",&q);
    
    for(;q--;){
//    while(q--){
      scanf(" %c",&op);
      if(op == 'A'){
        scanf("%d %d %d",&N,&X,&Y);
        m[X][Y] += N;
      }
      else{
        scanf("%d %d %d %d",&X,&Y,&Z,&W);
        
        //colocar o menor no x e y
        if(Z < X){
          soma = Z;
          Z = X;
          X = soma;
        }
        if(W < Y){
          soma = W;
          W = Y;
          Y = soma;
        }

        soma = 0;
        for (i = X; i <= Z; ++i)
          for (j = Y; j <= W; ++j)
            soma += m[i][j];

        printf("%d\n",soma*p);
      }
    }
    printf("\n");
  }
}