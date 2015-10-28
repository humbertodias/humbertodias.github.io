#include <stdio.h>

int main() {
  char c, ant='a'; 
  while ((scanf("%c",&c)) != EOF)  {
    switch (c) {
        case 'P': printf("F"); break;
        case 'S': printf("F"); break;
        case 'V': printf("F"); break;
        case 'X': printf("F"); break;
        case 'J': printf("F"); break;
        case 'B': printf("F"); break;
        case 'Z': printf("F"); break;
        case 'p': printf("f"); break;
        case 's': if (ant!='s') printf("f"); break;
        case 'v': printf("f"); break;
        case 'x': printf("f"); break;
        case 'j': printf("f"); break;
        case 'b': printf("f"); break;
        case 'z': printf("f"); break;
        default: printf("%c",c); break;
    } 
    ant=c;
  }
  return 0;
}