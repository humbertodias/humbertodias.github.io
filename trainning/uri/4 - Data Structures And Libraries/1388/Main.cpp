#include <stdlib.h>
#include <iostream>
#include <algorithm>
 
using namespace std;
 
int main()
{
    unsigned int elements, turns, i, j;
    int *array = NULL;
    int *turns_array = NULL;
 
    while(cin >> elements >> turns && (elements != 0 && turns != 0))
    {

        array = (int*)malloc(elements*sizeof(int));
        turns_array = (int*)malloc(turns*sizeof(int));
 
        for ( i = 0; i < elements; i++)
        {
            array[i] = i + 1;
        }
 
 
        for (i = 0; i < turns; i++)
        {
            cin >> turns_array[i];
        }
 
        for (i = turns; i >= 1; i--)
        {
            for (j = 0; j < turns_array[i - 1]; j++)
            {
                swap(array[i - 1 + j], array[i + j]);
            }
        }
 
        for (i = 0; i < elements; i++)
        {
            cout << array[i] ;
            if (i < elements -1 )
              cout << " ";              
        }
        cout << "\n";
 
        free(array);
    }
}