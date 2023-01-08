#include <stdio.h>
#include <math.h>



int main()



{

   int total;
   char  k;
   total= 0;



   while (scanf("%c", &k) == 1)



        {

          if (k == 'C' || k == 'c')

              {

                total = total + 1;

              }

        }

          printf("The total number of cytosines is %d \n", total);



}
