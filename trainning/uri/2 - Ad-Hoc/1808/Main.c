#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[])
{
  char s[101];
  int tmp, count = 0, sum = 0, i;
  gets(s);
  int l = strlen(s);

  for (i = 0; i < l; ++i)
  {
    tmp = (int)s[i] - 48;
    if(!tmp) { sum += 9; count--; } else{ sum += tmp; }
    count++;
  }

  printf("%.2f\n", (float) sum/count);

  return 0;
}
